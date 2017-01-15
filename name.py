import random

f = open("noun.txt","r")
nouns = f.read().splitlines()#f.readlines()
f.close()

f = open("adj.txt","r")
adjectives = f.read().splitlines()
f.close()

f = open("conn.txt","r")
connectors = f.read().splitlines()
f.close()

def makeName():
	random.seed()
	ln = len(nouns)
	b = nouns[random.randint(0,ln)]
	a = adjectives[random.randint(0,len(adjectives))]
	c = connectors[random.randint(0,len(connectors))]
	d = nouns[random.randint(0,ln)]
	return a + " " + b + " " + c + " " + d + ".mid"
