import random

def make_chord_beat():
	NUM_BEATS = 16

	r_prob = [0.8, 0.15, 0.4, 0.15, 0.75, 0.1, 0.5, 0.2, 0.85, 0.2, 0.45, 0.15, 0.7, 0.3, 0.55, 0.09]

	randoms = []
	beats = []

	for i in range(NUM_BEATS):
		randoms.append(random.random())

	for i in range(NUM_BEATS):
		if randoms[i] <= r_prob[i]:
			beats.append(True)
		else:
			beats.append(False)

	# print beats 
	return beats


def make_chord_rhythms(beats, chord, start=0):
	'''
	takes in list of 16 booleans and a list of notes
	returns list of objects to use in track writer
	'''

	len_rest = start

	chord_rhythm = []

	for note_num, beat in enumerate(beats):
		if not beat:
			len_rest += 1
		else: 
			chord_rhythm.append([chord, 0.25*len_rest, 0.25])
			len_rest = 0

	# print chord_rhythm
	return (chord_rhythm, len_rest)

beats = make_chord_beat()
# print beats
chord_rhythm = make_chord_rhythms(beats , ['C', 'E', 'G'])




