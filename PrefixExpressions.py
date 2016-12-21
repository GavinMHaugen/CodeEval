#Gavin Haugen
#CSCI 174
#11/14/2016
#CodeEval Hard Challenge: Prefix Expressions

import sys
#needed operator in order to use the .add, .mul, and .truediv operations
import operator

#using a dictionary to store the operations needed for problem
operators = {
	'+': operator.add,
	'*': operator.mul,
	'/': operator.truediv
}

#opening and iterating through test cases
test_cases = open(sys.argv[1], 'r')
for test in test_cases:

	#splitting the given input expression into a list
	expression = test.split()
	#allocating a stack to store the expression values
	expressionStack = []

	#iterating through the reversed expression
	for val in expression[::-1]:

		#If val isnt an operator it is a number, so turn that into an int and append to the expressionStack 
		if val not in operators:
			expressionStack.append(int(val))

		#If val is an operator defined in our dictionary, we pop the top two integer values off expressionStack,calculate either the
		# sum, product, or quotient of the two integer values, and then append that value to the expressionStack to be calculated with 
		#the next value
		else:
			A = expressionStack.pop()
			B = expressionStack.pop()
			total = operators[val](A,B)
			expressionStack.append(total)

	#printing the calculated value
	print int(round(expressionStack.pop()))
