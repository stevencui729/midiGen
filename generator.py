#i love hacking

import midi
import random
import json
import os

drum_beats_dict = {}


for root, dirs, files in os.walk(os.getcwd()):
    print files
    for file in files:
        if ".json" in file:
            print file

            with open() as json_f:
                drum_beats_dict = json.loads(json_f)
    
print drum_beats_dict

#initialize tempo
random.seed()
tempo = random.uniform(120,125)

# ticks per beat
tpb = 220

# drum part
# [[NOTES], start length (beats), chord length (beats)]
hat1 = [[[107, 110, 114],0,1],[[107],0,1],[[107, 111, 114],0,1],[[107],0,1]]
#snr1 = [[1,2,1]

# track is the track to add a sequence to
# note is the note in midi.G_3 or equivalent
# notelen in beats, not ticks
# seq is sequence of beats to append, e.g. hat1
def addToTrack(track, seq):
	l = len(seq)
	for i in range(0,l):
		temp = seq[i]
		notes  = temp[0]
		start  = int(temp[1]*tpb)
		length = int(temp[2]*tpb)

		m = len(notes)
		# put them in
		for j in range(0,m):
			if j == 0:
				on = midi.NoteOnEvent(tick = start, velocity = 127, pitch = notes[j])
			else:
				on = midi.NoteOnEvent(tick = 0, velocity = 127, pitch = notes[j])
			track.append(on)
		# take them out
		for j in range(0,m):
			if j == 0:
				off = midi.NoteOffEvent(tick = length, pitch = notes[j])
			else:
				off = midi.NoteOffEvent(tick = 0, pitch = notes[j])
			track.append(off)

# make major 9 or minor 9 chords
def rootToChord(root, maj):
	# major 9
	if maj == 1:
		return [root, root+4, root+7, root+11, root+14]
	elif maj == 0:
		return [root, root+3, root+7, root+10, root+14]



oursong = midi.Pattern()

#drums
drums = midi.Track()
oursong.append(drums)

addToTrack(drums, hat1)
#addToTrack(drums, snr1)

drums.append(midi.EndOfTrackEvent(tick = 1))

print oursong
midi.write_midifile("test.mid", oursong)

