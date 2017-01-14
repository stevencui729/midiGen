#i love hacking

import midi
import random

#initialize tempo
random.seed()
tempo = random.uniform(120,125)

# ticks per beat
tpb = 220

# drum part
# first item in list is the starting beat index of the first note
# the subsequent items are note lengths
# everything is held at full length
hat1 = [0,1,1,1,1]
snr1 = [1,2,1]

# track is the track to add a sequence to
# note is the note in midi.G_3 or equivalent
# notelen in beats, not ticks
# seq is sequence of beats to append, e.g. hat1
def addToTrack(track, note, seq):
	l = len(seq)
	start = seq[0]*tpb
	for i in range(1,l):
		t = int(seq[i]*tpb)
		if i == 1:
			on = midi.NoteOnEvent(tick = start, velocity = 127, pitch = note)
		else:
			on = midi.NoteOnEvent(tick = 0, velocity = 127, pitch = note)
		track.append(on)
		#off = midi.NoteOffEvent(tick = int(t + notelen*tpb), pitch = note)
		off = midi.NoteOffEvent(tick = t, pitch = note)
		track.append(off)


oursong = midi.Pattern()

#drums
drums = midi.Track()
oursong.append(drums)

addToTrack(drums, midi.D_4, hat1)
addToTrack(drums, midi.C_6, snr1)

drums.append(midi.EndOfTrackEvent(tick = 1))

print oursong
midi.write_midifile("test.mid", oursong)

