#i love hacking

import midi
import random
import json
import os


def main():
    drum_beats_dict = {}


    with open("drums.json") as json_f:
        drum_beats_dict = json.load(json_f)

    # visualization of json
    #for drum in drum_beats_dict.keys():
    #    print drum
    #    for pattern in drum_beats_dict[drum].keys():
    #        print pattern
    #        print drum_beats_dict[drum][pattern]
    #    print "\n"

    #initialize tempo
    random.seed()
    tempo = random.uniform(120,125)

    # ticks per beat
    tpb = 220

    # drum part
    # [[NOTES], start length (beats), chord length (beats)]
    #hat1 = [[[107, 110, 114],0,1],[[107],0,1],[[107, 111, 114],0,1],[[107],0,1]]
    #snr1 = [[1,2,1]




    # START OF MIDI CONSTRUCTION
    ## ===========================================================

    oursong = midi.Pattern()

    # creation of drums tracks
    hats = midi.Track()
    snare = midi.Track()
    kick = midi.Track()
    oursong.append(hats)
    oursong.append(snare)
    oursong.append(kick)

    rand_hats = random.randint(1, 4)
    rand_snare = random.randint(1, 4)
    rand_kick = random.randint(1, 2)

    for i in range(0, 10):
        addToTrack(hats, drum_beats_dict["hats"][str(rand_hats)], tpb)
        addToTrack(snare, drum_beats_dict["snare"][str(rand_snare)], tpb)
        addToTrack(kick, drum_beats_dict["kick"][str(rand_kick)], tpb)

    # adding end of tracks to the drums tracks
    hats.append(midi.EndOfTrackEvent(tick = 1))
    snare.append(midi.EndOfTrackEvent(tick = 1))
    kick.append(midi.EndOfTrackEvent(tick = 1))

    # printing and writing midi file
    print oursong
    midi.write_midifile("test.mid", oursong)

    ## ============================================================



# track is the track to add a sequence to
# note is the note in midi.G_3 or equivalent
# notelen in beats, not ticks
# seq is sequence of beats to append, e.g. hat1
def addToTrack(track, seq, tpb):
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



if __name__ == "__main__":
    main()
