#Miriam Sack
#Problem 2

#also, what if urn had more or less balls in it?

if __name__ == '__main__':
	import math
	import random
	import sys
	import numpy as np
	for i in range(5):
		N = 100
		RRc = 0
		GGc = 0
		RGc = 0
		GRc = 0
		count = 0
	#making urn
		x = random.randint(1,100)
		urn = []
		for i in range(x):
			urn.append("R")
		for j in range(100-x):
			urn.append("G")

	#simulation

		for k in range(N):
			random.shuffle(urn)
		#picking first ball
			ball1 = random.choice(urn)
			urn.remove(ball1)
		#print("First ball: ", ball1)
		#picking second ball
			ball2 = random.choice(urn)
			urn.remove(ball2)
		#print("Second ball: ", ball2)
		#counting things
			if ball1 == "R" and ball2 == "R":
				RRc += 1
			if ball1 == "G" and ball2 == "R":
				GRc += 1
			if ball1 == "R" and ball2 == "G":
				RGc += 1
			if ball1 == "G" and ball2 == "G":
				GGc += 1
		#reset urn
			urn.append(ball1)
			urn.append(ball2)
			count += 1
#expected number of red/green???
#expected RG = x(100-x)/(100)(99)
#expected RR = x(x-1)/(100)(99)
#expected GG = (100-x)(99-x)/(100)(99)
#expected RG = x(100-x)/(100)(99)
		exGR = (x*(100-x)/9900)*100
		exRR = (x*(x-1)/9900)*100
		exGG = ((100-x)*(99-x)/9900)*100
		exRG = (x*(100-x)/9900)*100
		print("Number of red balls in urn: ", x)
		print("RG: ", RGc)
		print("Expected RG: ", exRG)
		print("RR: ", RRc)
		print("Expected RR: ", exRR)
		print("GG: ", GGc)
		print("Expected GG: ", exGG)
		print("GR: ", GRc)
		print("Expected GR: ", exGR)
		#print("number of first ball red: ", RGc + RRc)
		#print("red then red: ", exRR/(exRG + exRR))
		#print("red then green: ", exRG/(exRG +exRR))
	#print("count: ", count)
