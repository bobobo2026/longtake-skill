#!/usr/bin/env python3
# longtake · based on onetake (© 2026 Patrick, PolyForm Noncommercial 1.0.0) · this file added by bobobo2026
"""beat_grid.py — the music's clock, before the beat sheet: tempo, beat grid, silent gaps, energy per beat.

    python3 scripts/beat_grid.py track.m4a                 # summary
    python3 scripts/beat_grid.py track.m4a --json grid.json

numpy + scipy + ffmpeg only (no librosa). Tempo comes from the autocorrelation of spectral flux; the grid's phase
is the offset that collects the most flux. Short loud clips (20 s 高潮段) often hide a half-time feel: check the
`kicks` list against `beats` and pick the grid that the kicks sit on. A `gap` (near-silence inside the track) is
where the picture should stop dead; the first strong kick after it is the drop.
"""
import argparse, json, subprocess
import numpy as np
from scipy.signal import find_peaks

def load(path, sr=22050):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-ac', '1', '-ar', str(sr), '-f', 'f32le', '-'], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32), sr

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('track'); ap.add_argument('--json'); ap.add_argument('--min-bpm', type=float, default=70); ap.add_argument('--max-bpm', type=float, default=180)
    a = ap.parse_args(); y, sr = load(a.track); hop = 512; n = 2048; fps = sr / hop
    fr = np.lib.stride_tricks.sliding_window_view(y, n)[::hop] * np.hanning(n)
    S = np.log1p(np.abs(np.fft.rfft(fr, axis=1)) * 10)
    flux = np.r_[0, np.maximum(np.diff(S, axis=0), 0).sum(1)]; flux = (flux - flux.mean()) / (flux.std() + 1e-9)
    ac = np.correlate(flux, flux, 'full')[len(flux) - 1:]; lags = np.arange(len(ac)); bpm = 60 * fps / np.maximum(lags, 1)
    m = (bpm >= a.min_bpm) & (bpm <= a.max_bpm); L = int(lags[m][np.argmax(ac[m])])
    phase = max(range(L), key=lambda p: flux[p::L].sum()); beats = np.arange(phase, len(flux), L) / fps
    rms = np.sqrt((fr ** 2).mean(1)); t = np.arange(len(rms)) / fps; db = 20 * np.log10(rms + 1e-9)
    quiet = db < db.max() - 30; gaps, i = [], 0
    while i < len(quiet):
        if quiet[i]:
            j = i
            while j < len(quiet) and quiet[j]: j += 1
            if (j - i) / fps >= 0.08 and 0.3 < t[i] < t[-1] - 0.5: gaps.append([round(float(t[i]), 3), round(float(t[min(j, len(t) - 1)]), 3)])
            i = j
        else: i += 1
    low = np.abs(np.fft.rfft(fr, axis=1))[:, 1:12].sum(1)
    pk, _ = find_peaks(low, height=np.percentile(low, 90), distance=int(fps * 0.2)); kicks = [round(float(x), 3) for x in t[pk]]
    energy = [round(float(rms[(t >= b) & (t < b + L / fps)].mean()), 3) if ((t >= b) & (t < b + L / fps)).any() else 0 for b in beats]
    out = dict(duration=round(len(y) / sr, 3), bpm=round(60 * fps / L, 2), beat=round(L / fps, 4), first_beat=round(float(beats[0]), 3),
               beats=[round(float(b), 3) for b in beats], gaps=gaps, kicks=kicks, energy_per_beat=energy)
    print(f"{a.track}: {out['duration']} s · {out['bpm']} BPM (beat {out['beat']} s) · first beat {out['first_beat']} s")
    print('gaps (stop the picture here):', gaps or 'none'); print('kicks:', kicks[:40], '…' if len(kicks) > 40 else '')
    if a.json: json.dump(out, open(a.json, 'w'), indent=1); print('wrote', a.json)

if __name__ == '__main__':
    main()
