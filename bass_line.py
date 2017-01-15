import random

def make_bass(root):

	NUMBEATS = 8
	b_prob = [1, 0.15, 0.4, 0.25, 0.75, 0.1, 0.5, 0.25]

	randoms = []
	is_note = []

	for i in range(NUM_BEATS):
		randoms.append(random.random())

	for i in range(NUM_BEATS):
		if randoms[i] <= r_prob[i]:
			is_note.append(True)
		else:
			is_note.append(False)


	notes = []

	for i, boolean in enumerate(is_note):
		note_len = 0
		if boolean:
			note = [[root], 0]
			if len(notes) == 0:
				notes.append(note)
			else:
				notes[i-1].append(note_len)
				notes.append(note)
				note_len = 0
		else:
			note_len += 1

	notes[-1].append(note_len)

	return notes

