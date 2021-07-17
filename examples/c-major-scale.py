from midi import MIDIFile

degrees = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
track = 0
channel = 0
time = 0  # In beats
duration = 1  # In beats
tempo = 60  # In BPM
volume = 100  # 0-127, as per the MIDI standard

print("Import and variables done.")

MyMIDI = MIDIFile(1)  # One track
MyMIDI.addTempo(track, time, tempo)

print("File created with one track")

for i, pitch in enumerate(degrees):
    MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

print("Added notes to file")

print(MyMIDI)

with open("major-scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)

print("Wrote File")