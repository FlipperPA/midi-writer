# midi-writer Introduction

## Introduction

`midi-writer` is a pure Python library that allows one to write multi-track
Musical Instrument Digital Interface (MIDI) files from within Python
programs (both format 1 and format 2 files are now supported).
It is object-oriented and allows one to create and write these
files with a minimum of fuss.

## Installation

Eventually, you'll be able to install this from PyPI with something like `pip install midi-writer`. But for now, do a `git clone https://github.com/FlipperPA/midi-writer.git`, and `pip install -e midi-writer`.

## Quick Start

In this example we'll create a one track MIDI File, assign a tempo to the track, and write a C-Major scale. Then we write it to disk.

```python
from midi_writer import MIDIFile, Notes

_ = Notes()  # The Notes class maps notes to their MIDI equivalents
degrees = [_.C4, _.D4, _.E4, _.F4, _.G4, _.A4, _.B4, _.C5]
track = 0
channel = 0
time = 0  # In beats
duration = 1  # In beats
tempo = 60  # In BPM
velocity = 100  # 0-127, as per the MIDI standard - often used for VOLUME

MyMIDI = MIDIFile(1)  # One track
MyMIDI.add_tempo(track, time, tempo)

for i, pitch in enumerate(degrees):
    MyMIDI.add_note(track, channel, pitch, time + i, duration, velocity)

with open("major-scale.mid", "wb") as output_file:
    MyMIDI.write_file(output_file)

print("The MIDI file has been written successfully.")
```

There are several additional event types that can be added and there are
various options available for creating the MIDIFile object, but the above
is sufficient to begin using the library and creating note sequences.

The above code is found in machine-readable form in the examples directory.
A detailed class reference and documentation describing how to extend
the library is provided in the documentation directory.

Have fun!

## A Note on Channels

Due to ancient MIDI conventions, it is typical to use two channels. Since we're using zero-based indexing:

* `Channel 0` is typically used by all instruments other than percussion.
* `Channel 9` is typically reserved for percussion instruments, I.e. the drum set.

Tracks can be used within those channels. For example, you might want one track for the high hat, and another track to handle the bass, snare, and toms.

## Release Notes and Contributors

* [Release notes](https://github.com/flipperpa/midi-writer/releases)
* [Our wonderful contributors](https://github.com/flipperpa/midi-writer/graphs/contributors)

## Maintainer & Original Author

* [Timothy Allen](https://github.com/flipperpa): maintainer
* [Mark C. Wirt](https://github.com/MarkCWirt): author of the original; thank you for all of your work!
