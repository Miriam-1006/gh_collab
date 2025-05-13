#Miriam Sack
#Problem 2

#also, what if urn had more or less balls in it?

if __name__ == '__main__':
	import math
	import random
	import sys
	import numpy as np
	for i in range(10):
		N = 100
		RRc = 0
		GGc = 0
		RGc = 0
		GRc = 0
		count = 0
	#making urn
		#k=0
		#while k < N:
		x = random.randint(1,100)
		urn = []
		for i in range(x):
			urn.append("R")
		for j in range(100-x):
			urn.append("G")

	#simulation
		k = 0
		while k < N:
			random.shuffle(urn)
		#picking first ball
			urn.remove("R")
			#ball1 = 
			#print("ball1: ", ball1)
			#if ball1 == 'R':
			#print("First ball: ", ball1)
		#picking second ball
			ball2 = random.choice(urn)
			k += 1
		#print("Second ball: ", ball2)
		#counting things
			if ball2 == "R":
				RRc += 1
			if ball2 == "G":
				RGc += 1
		#reset urn
			count += 1
			#print("k: ", k)
			urn.append("R")
#expected number of red/green???
#expected RG = x(100-x)/(100)(99)
#expected RR = x(x-1)/(100)(99)
#expected GG = (100-x)(99-x)/(100)(99)
#expected RG = x(100-x)/(100)(99)
		exRR = ((x-1)/99)*100
		exRG = ((100-x)/99)*100
		print("Number of red balls in urn: ", x)
		print("RG: ", RGc)
		print("Expected RG: ", exRG)
		print("RR: ", RRc)
		print("Expected RR: ", exRR)
		#print("number of first ball red: ", RGc + RRc)
		#print("red then red: ", exRR/(exRG + exRR))
		#print("red then green: ", exRG/(exRG +exRR))
		#print("count: ", count)
