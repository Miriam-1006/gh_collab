#Miriam Sack
#Final Project
#Urn puzzle
#we have 100 urns each containing 99 balls.
# In 99 urns, there is 1 red ball and 98 green balls. In 1 urn, there is 99 red balls.
#You pick an urn at random and draw a red ball. and discard the ball
#in the same urn, the next ball you draw is probably: red, green, or equally likely

if __name__ == '__main__':
	import math
	import random
	import sys
	import numpy as np
#simulation
	N = 100
	rgcount = 0
	rrcount = 0
	i = 0
	while i < N:
		#set up listA
		listA = []
		listA = ["G"]*98
		listA.append("R")
		random.shuffle(listA)
		#set up listB(the 1 urn)
		listB = []
		listB = ["R"]* 99
		#set up urns
		urn = []
		n = 99
		for x in range(n):
			random.shuffle(listA)
			urn.append(listA)
		urn.append(listB)
		random.shuffle(urn)
		random.shuffle(listA)
	#choose things
		#choose our urn
		ourUrn = random.choice(urn)
        	#print(ourUrn)
		#pick ball
		ball1 = random.choice(ourUrn)
		if ball1 == 'R':
			ourUrn.remove(ball1)
			ball2 = random.choice(ourUrn)
			#print(ball2)
			i += 1
		if ball1 == 'R' and ball2 == 'R':
			rrcount += 1
			#print("red and red")
		if ball1 == 'R' and ball2 == 'G':
			rgcount += 1
			#print("red and green")
	print("Red and Red Count:", rrcount)
	print("Red and Green Count:", rgcount)
	#print("number urn A:", Ac)
	#print("number urn B:", Bc)
	#print(len(listA))
	#print(len(listB))
	#print(len(urn))
#set up listA(the 99 urns)
        #listA = []
        #listA = ["G"]*98
        #listA.append("R")
        #random.shuffle(listA)
#set up listB(the 1 urn)
        #listB = []
        #listB = ["R"]* 99
#set up urns
        #n = 99
        #urn = []
        #for x in range(n):
        #       random.shuffle(listA)
#       urn.append(listA)
        #urn.append(listB)
        #random.shuffle(urn)
#pick an urn
        #ourUrn = random.choice(urn)
        #print(ourUrn)
#pick a ball from our urn
        #ball1 = random.choice(ourUrn)
        #print(ball1)
#pick a second ball if first ball was red
        #if ball1 == 'R':
        #       ourUrn.remove(ball1)
        #       ball2 = random.choice(ourUrn)
        #       print(ball2)
