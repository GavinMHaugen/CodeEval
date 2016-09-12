#Gavin Haugen
#BayBridges

import sys
from re import sub
from itertools import combinations

#implementing the Coordinate Point and Line Segment classes that
#I will be using in order to determine if a bridge is crossing another
class Point:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "[%r, %r]" % (self.x, self.y)


class Bridge:

	def __init__(self, i, a, b):
		self.i = i
		self.a = a
		self.b = b

	def __str__(self):
		return "%d: (%s, %s)" % (self.i, self.a, self.b)

#takes in 3 points and checks if they are counter clockwise of each other
def IsCounterClockwise(A, B, C):
	return (C.y - A.y)*(B.x - A.x) > (B.y - A.y)*(C.x - A.x)

#takes in 4 points and returns whether the points are intersecting or not in 
#boolean form
def IsIntersecting(A, B, C, D):
	return IsCounterClockwise(A, C, D) != IsCounterClockwise(B, C, D) and IsCounterClockwise(A, B, C) != IsCounterClockwise(A, B, D)


#declaring variables for holding our test cases and bridges that will be made
test_cases = open(sys.argv[1], 'r')
bridges = list()

for test in test_cases:

	#base case, checking if the line is empty
	if test.strip() == '':
		continue

	#The input of this challenge gives the number of the bridge as the first character
	#We need to split that and save the leftmost part of the string to be split later as well so we
	#put a restMark to basically put a bookmark

	#And we create a list to store all the coordinate points for our bridges in the problem
	BridgeNum, restMark = test.split(':')
	BridgePoints = list()

	#Now we are parsing through the points given through the input and appending them
	#to the BridgePoints list.
	#Side note: the input is given as 1:([A, B], [C, D]), 2:...
	for point in restMark.split(','):
		#using the sub function from the RE library here to make it a bit easier since its a string initially
		#and we need to change it to a float type
		BridgePoints.append(float(sub("[^0-9.-]", "", point)))


	#Now we are simply creating objects for the points and bridges using the input given
	a = Point(BridgePoints[0], BridgePoints[1])
	b = Point(BridgePoints[2], BridgePoints[3])
	BridgeNum = Bridge(int(BridgeNum), a, b)
	#appending the Bridge numbers to the # of bridges list
	bridges.append(BridgeNum)

#Printing helper functions to print out the bridge location
def PrintBridges(bridges):
	for bridge in bridges:
		print bridge

#and the bridge number
def PrintBridgeNum(bridges):
	Bnum = list()

	for bridge in bridges:
		Bnum.append(bridge.i)
	Bnum.sort()

	for num in Bnum:
		print num


#closing the test cases 
test_cases.close()

#returns the number of intersections a Bridge obj has in a list
#will be using this function to determine which bridges are "safe" and "unsafe"
def NumOfIntersections(BridgeNum, bridges):
	count = 0

	for BridgeNum2 in bridges:

		if BridgeNum.i == BridgeNum2.i:
			continue

		if IsIntersecting(BridgeNum.a, BridgeNum.b, BridgeNum2.a, BridgeNum2.b):
			count += 1


	return count


#implementing lists to hold our safe and unsafe bridges
SafeBridges = list()
UnsafeBridges = list()

#After we initiated our Safe and Unsafe bridge lists 
# we need to sort the bridges that are safe(have no intersections)
#and the bridges that are not safe(have more than 1 intersection)
while len(bridges) > 0:

	MaxIntersect = 0
	MaxBridge = {}

	for x in bridges:

		count = NumOfIntersections(x, bridges)

		#if the count of number of intersections is 0
		# add to the safe bridge list
		if count == 0:
			SafeBridges.append(x)

		#else if the count of intersections is higher than the previously set max
		#number of intersects, that number is now the max and that bridge is also the max
		elif count >= MaxIntersect:
			MaxIntersect = count
			MaxBridge = x

	#if there was a bridge made the max bridge in the previous loop
	#then we are going to remove it from the original bridges list
	#and add it to the unsafe bridge list
	if MaxBridge:
		bridges.remove(MaxBridge)
		UnsafeBridges.append(MaxBridge)

	#just double checking that there are no bridges in both the safe bridge list
	#and the original bridge list because if its safe it should only be in the safe bridge list
	for x in SafeBridges:
		if x in bridges:
			bridges.remove(x)


#now we print!
PrintBridgeNum(SafeBridges)