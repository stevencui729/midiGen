import random
import numpy as np

def pick_key():
	key = random.randint(58,69)
	maj = random.randint(0,1)
	print (key, maj)
	return (key, maj)

def define_viable_chords(key_note, maj):
	viable = []
	
	major_steps = [0, 2, 4, 5, 9, -3, -7, -8, -10]
	if_major =    [1, 0, 0, 1, 0,  0,  1,  0, 0]
	
	minor_steps = [0, 3, 5, 7, 8, -4, -5, -7, -9]
	if_minor =    [0, 1, 0, 0, 1,  1,  0,  0,  1]

	if maj:
		for i, step in enumerate(major_steps):
			viable.append([key_note+step, if_major[i]])
	elif not maj:
		for i, step in enumerate(minor_steps):
			viable.append([key_note+step, if_minor[i]])


	print viable 
	return viable 

def chord_transition(viable_chords):
	'''
	bins = [0,0.2,0.4,0.6,0.8,1]
	trans_var = random.random()
	counter = 0
	while trans_var > bins[counter + 1]:
		counter += 1
	new_chord = viable_chords[counter]
	'''
	i = random.randint(0,len(viable_chords)-1)

	return viable_chords[i]



def root_list(key_note, maj, n):
	
	viable_chords = define_viable_chords(key_note, maj)
	roots = [[key_note,maj]]
	for i in range(1,n):
		roots.append(chord_transition(viable_chords))
	return roots
