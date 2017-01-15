#i love hacking

import midi
import random
import json
import os
import chord_transition as ct
import testing_rhythm as tr
import bass_line as bl
import name

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

    # number of bars
    n = 16

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

    # adding end of tracks to the drums tracks and changing instrument from default piano to drums
    hats.append(midi.ProgramChangeEvent(tick=0, channel=10, data=[35]))
    hats.append(midi.ControlChangeEvent(tick=0, channel=10, data=[0,120]))
    hats.append(midi.ControlChangeEvent(tick=0, channel=10, data=[32,0]))
    hats.append(midi.ProgramChangeEvent(tick=0, channel=10, data=[1]))
    snare.append(midi.ProgramChangeEvent(tick=0, channel=10, data=[38]))
    kick.append(midi.ProgramChangeEvent(tick=0, channel=10, data=[42]))
    

    chords = midi.Track()
    oursong.append(chords)
    chords.append(midi.ProgramChangeEvent(tick=0, channel=0, data=[82]))

    bass = midi.Track()
    oursong.append(bass)

    for k in range(0,2):

        rand_hats = random.randint(1, 4)
        rand_snare = random.randint(1, 4)
        rand_kick = random.randint(1, 2)

        for i in range(0, n):
            addToTrack(hats, drum_beats_dict["hats"][str(rand_hats)], tpb)
            addToTrack(snare, drum_beats_dict["snare"][str(rand_snare)], tpb)
            addToTrack(kick, drum_beats_dict["kick"][str(rand_kick)], tpb)

        
        

        # making chords dude
        (key_note, maj) = ct.pick_key()
        begin = 0
        roots = ct.root_list(key_note, maj, n)
        begin = makeChords(chords, chordList(roots), begin, tpb)
        

        # making da bass man
        for root in roots:
            addToTrack(bass,bl.make_bass(root),tpb)

    hats.append(midi.EndOfTrackEvent(tick = 1))
    snare.append(midi.EndOfTrackEvent(tick = 1))
    kick.append(midi.EndOfTrackEvent(tick = 1))
    chords.append(midi.EndOfTrackEvent(tick = 1))
    bass.append(midi.EndOfTrackEvent(tick = 1))

    songname = name.makeName()
    print songname

    # printing and writing midi file
    # print oursong
    midi.write_midifile(songname, oursong)

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


# take a list of roots and turn it into a list of chords
def chordList(roots):
    new = []
    for i in roots:
        new.append(rootToChord(i[0],i[1]))
    return new

def makeChords(track, chords, begin, tpb):
    start = begin

    for chord in chords:
        (bar, start) = tr.make_chord_rhythms(tr.make_chord_beat(), chord, start)
        addToTrack(track, bar, tpb)
    return start


if __name__ == "__main__":
    main()
