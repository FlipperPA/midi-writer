from midi import MIDIFile, Notes

_ = Notes()  # The Notes class maps notes to their MIDI equivalents
degrees = [_.C4, _.D4, _.E4, _.F4, _.G4, _.A4, _.B4, _.C5]
track = 0
channel = 0
time = 0  # In beats
duration = 1  # In beats
tempo = 60  # In BPM
volume = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track
MyMIDI.add_tempo(track, time, tempo)

for i, pitch in enumerate(degrees):
    MyMIDI.add_note(track, channel, pitch, time + i, duration, volume)

with open("major-scale.mid", "wb") as output_file:
    MyMIDI.write_file(output_file)

print("The MIDI file has been written successfully.")
