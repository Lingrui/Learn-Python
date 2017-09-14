#!/usr/bin/python  
def sum(list):
	sum = 0 

	for i in range(0, len(list)):
		sum = sum + list[i]

	return sum
print(sum([5,7,3,8,10]))


def sum(list):
	if len(list) == 1:
		return list[0]
	else:
		return list[0] + sum(list[1:])
print(sum([2,3,4,5,6,7]))

###factorial with recursion###
print "factorial: n!=n*(n-1)!"
def factorial(n):
	if n == 1:
		return 1 
	else:
		return n * factorial(n-1)
print factorial(3)

##limitations of recursions###
print "Python stops the function calls after a depth of 1000 calls"
print factorial(3000)


