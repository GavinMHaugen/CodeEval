#Gavin Haugen
#Max Range Sum CodeEval problem

import sys

#opening the test case that codeeval gives us
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	#if the line contains nothing then we want nothing to do with it
	if test.strip() == '':
		continue

	#using this to store the max sum
	result = 0
	#Taking(and converting since we parse through it as a string) the integer before the semicolon in the input which is the number of days
	#we use to find the max range sum of the array.
	NumOfDays = int(test.split(';')[0])
	#Taking the RHS of the semicolon and splitting it, "integerizing" it, and packing it into and array
	NumArray = [int(x) for x in test.splt(';')[1].split(' ')]

	#Now that the parsing of the input is done its time to do the meat of the assignment, which is finding the max sum within our given domain
	for i in range(0, len(NumArray)-NumOfDays+1):
		#I find the max sum by using the built in function max() which returns the largest of two arguments
		#the first argument is the new sum being calculated and the second being the last returned MaxSum from max()

		#I used list slicing here with the array to easyily find the sum we are looking to compare with
		MaxSum = max(sum(NumArray[i:i+NumOfDays]), MaxSum)

	#Prints the MaxSum of the given input and repeats for the next test case
	print MaxSum