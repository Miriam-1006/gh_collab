#Miriam Sack
#generating a seating chart

#import
import numpy as np
from numpy import random
#program
if __name__ == '__main__':
	#getting input from user
	n = int(input("Enter the number of rows (less than 5): "))
	m = int(input("Enter the number of columns (less than 5): "))
	#setting up grid
	grid = np.array ( [] )
	#16 names
	nameList = ["Miriam", "Xandra", "Jasper", "Nacci", "Felix", "Bentley", "Sophie", "Emmett", "Francis", "Comet", "Alex", "Austin", "Donna", "Ethan", "Danny", "Jenny"]
	for i in range(n):
		for j in range(m):
			randName = random.choice(nameList)
			#append randName to grid
			grid = np.append(grid, randName)
			#remove randName from randList
			nameList.remove(randName)
	#done loop
	#reshape grid as nxm
	grid = grid.reshape(n,m)
	#position in the classroom
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			print(grid[i][j],"(",i,",",j,")",end=' ')
		print()
