"""
This example writes two files, "major-scale.mid" and "chromatic-scale.mid".
"""

# Import the MIDIFile class
from midi import MIDIFile

# Import all note mappings for use in scales.
from midi.constants import *

degrees = {}
degrees["major"] = [C4, D4, E4, F4, G4, A4, B4, C5]
degrees["chromatic"] = [C4, Cs4, D4, Ds4, E4, F4, Fs4, G4, Gs4, A4, As4, B4, C5]
track = 0
channel = 0
time = 0  # In beats
duration = 1  # In beats
tempo = 60  # In BPM
volume = 100  # 0-127, as per the MIDI standard

for loop in ("major", "chromatic"):
    MyMIDI = MIDIFile(1)  # One track
    MyMIDI.add_tempo(track, time, tempo)

    for i, pitch in enumerate(degrees[loop]):
        MyMIDI.add_note(track, channel, pitch, time + i, duration, volume)

    with open(f"{loop}-scale.mid", "wb") as output_file:
        MyMIDI.write_file(output_file)

print("The MIDI files have been written successfully.")
