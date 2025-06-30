# Copyright 2025 Raine Edgar
# SPDX-License-Identifier: Apache-2.0

import subprocess
from pathlib import Path
from tkinter.filedialog import askopenfilenames

from pydub import AudioSegment

def main():
    """
    1. Prompts the user to choose the target true-peak level and all .wav files to normalise.
    2. Overwrites the selected wav files with the normalised versions.

    Defaults to a bit-depth of 16 and a sample-rate of 48000hz.

    Requires FFmpeg to be installed in PATH. Built for version 2025-03-27-git-114fccc4a5-full_build-www.gyan.dev

    Known Issues:
        Downsampling not properly addressed - adding dither would be an improvement.
        Introduces a miniscule amount of digital noise. When one file is normalised approx. 20 times the noise becomes
        noticeable if placed under close comparison with the original.
        When bit_depth set to 3 (24bit) viewing file properties shows it as 32 bit.
    """
    bit_depth: int = 2 # In bytes, 1 byte == 8 bits. Defaults to 2 (16bit).
    sample_rate: int = 48000 # Sets sample rate.

    target_level = input("Enter target true-peak normalisation level: ")
    target_level = float(target_level) # Casts user input as a float.

    true_peak: float = 10  # Arbitrary temporary value to prevent issues later.

    if target_level <= 0: # Prevents eardrum destruction.
        files = askopenfilenames(title="Select Assets...",
                                 defaultextension=".wav",
                                 filetypes=(("Waveform Audio File Format", ".wav"),))

        files = [Path(file) for file in files] # Casts file locations as paths.

        for file in files:
            # Runs FFmpeg in command line to extract volume information.
            cmd = [
                'ffmpeg',
                '-i', Path(file),
                '-filter_complex', 'volumedetect',
                '-f', 'null',
                '-'
            ]
            result = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
            # Gets the info back and uses split to find the current true-peak.
            for line in result.stderr.splitlines():
                if 'max_volume' in line:
                    true_peak = float(line.split()[-2])
            if true_peak != 10: # Ensures true-peak level has changed before continuing.
                audio_file = AudioSegment.from_wav(file=file)
                gain_change = target_level - true_peak
                print(f"Current true peak: {true_peak}, "
                      f"Target true peak: {target_level}, "
                      f"Change in gain: {gain_change} "
                      f"File Path: {file}")
                normalized_file = audio_file.apply_gain(volume_change=gain_change)
                normalized_file = normalized_file.set_sample_width(bit_depth)
                normalized_file = normalized_file.set_frame_rate(sample_rate)
                normalized_file.export(file, format="wav") # Change 'file' to a different path to change export location
    else:
        raise (ValueError("Normalisation target must be less than or equal to 0."))

if __name__ == '__main__':
    main()
