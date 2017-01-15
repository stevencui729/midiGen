import random
import numpy as np

def pick_key():
	key = random.randint(48,59)
	maj = random.randint(0,1)
	print (key, maj)
	return (key, maj)

def define_viable_chords(key_note, maj):
	viable = []
	major_steps = [0,2,4,5,9]
	minor_steps = [0,3,5,7,8]
	if_major = [1, 0, 0, 1, 0]
	if_minor = [0, 1, 0, 0, 1]

	if maj:
		for i, step in enumerate(major_steps):
			viable.append([key_note+step, if_major[i]])
	elif not maj:
		for i, step in enumerate(minor_steps):
			viable.append([key_note+step, if_minor[i]])


	print viable 
	return viable 

def chord_transition(viable_chords):
	bins = [0,0.2,0.4,0.6,0.8,1]
	trans_var = random.random()
	counter = 0
	while trans_var > bins[counter + 1]:
		counter += 1
	new_chord = viable_chords[counter]

	return new_chord



def root_list(n):
	(key_note, maj) = pick_key()
	viable_chords = define_viable_chords(key_note, maj)
	roots = [[key_note,maj]]
	for i in range(n):
		roots.append(chord_transition(viable_chords))
	return roots
