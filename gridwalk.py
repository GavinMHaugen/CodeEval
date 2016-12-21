#Gavin Haugen
#grid walk challenge

from collections import deque

#This function:
#takes in an integer number
#returns the sum of its digits
#ex) 123 = 6, 789 = 24
def SumOfDigits(num):
	total = 0
	while num > 0:
		total += num % 10
		#using the // operator in order to make sure we only deal with integer operations
		num //= 10
	return total

#This function:
#takes in a coordinate pair
#finds the SumOfDigits of each value of the coordinate pair
#and checks to see if that sum is less than or equal to 19
#if that sum is <= 19, return True
#Otherwise return False
def IsValid(coord):
	return sum(SumOfDigits(abs(x)) for x in coord) <= 19

#This function: 
#takes in a coordinate pair
#returns a list of the surrounding neighbor coordinates pairs
def CheckNeighbors(coord):
	x,y = coord
	return [(x+1,y), (x,y+1), (x-1, y), (x,y-1)]

#This function:
#Takes in a starting coordinate pair
#Validates the starting coordinate
#Creates a set for Already visited coordiantes and a deque for the Unexplored coordinates 
	# I used a deque for this problem so I could utilize the pop and append features for this data structure
	# since a deque is mutable from both ends unlike a regular queue
#Now, we check the UnexploredCoords deque to see if there are points to explore and validate
	#while that statement is true, we pop the top coord off the deque and find the list of neighbor coords
	#now we traverse through the list of neighbor coords and check
		#1) if the neighbor coord is valid
		#2) the neighbor coord is NOT in the visitedcoords set already
	#If true, we add that neighbor coord to the visitedcoords set AND we append the current coord we are checking
	#to the UnexploredCoords deque so we can check its neighbor coords for their validity.
#After we are unable validate neighbor coordinates there will be nothing left to pop off the UnexploredCoords deque and the 
#function will return the VisitedCoords set
def IsAccessible(start):
	assert IsValid(start)
	VisitedCoords = set([start])
	UnexploredCoords = deque([start])


	while UnexploredCoords:
		point = UnexploredCoords.pop()
		for neighbor in CheckNeighbors(point):
			if IsValid(neighbor) and neighbor not in VisitedCoords:
				VisitedCoords.add(neighbor)
				UnexploredCoords.append(neighbor)
	return VisitedCoords

#Now we just print the length of the IsAccessible function starting at coordinate (0,0)
if __name__ == '__main__':
	print len(IsAccessible((0,0)))
