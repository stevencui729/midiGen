#i love hacking

import midi
import random

#initialize tempo
random.seed()
tempo = random.uniform(120,125)

# ticks per beat
tpb = 220

# drum part
# [0,1,2,3] implies downbeats, so 0 is beat 1, 1 is beat 2, 0,5 would be 1&
hat1 = [0,1,2,3]
snr1 = [1,3]

# track is the track to add a sequence to
# note is the note in midi.G_3 or equivalent
# notelen in beats, not ticks
# seq is sequence of beats to append, e.g. hat1
def addToTrack(track, note, notelen, seq):
	l = len(seq)
	current = 0
	for i in range(0,l):
		t = int(seq[i]*tpb)
		#on = midi.NoteOnEvent(tick = t, velocity = 127, pitch = note)
		on = midi.NoteOnEvent(tick = 110, velocity = 127, pitch = note)
		track.append(on)
		#off = midi.NoteOffEvent(tick = int(t + notelen*tpb), pitch = note)
		off = midi.NoteOffEvent(tick = 110, pitch = note)
		track.append(off)


oursong = midi.Pattern()

#drums
drums = midi.Track()
oursong.append(drums)

addToTrack(drums, midi.D_3, 0.5, hat1)
#addToTrack(drums, midi.C_3, 1, snr1)

drums.append(midi.EndOfTrackEvent(tick = 1))

print oursong
midi.write_midifile("test.mid", oursong)

