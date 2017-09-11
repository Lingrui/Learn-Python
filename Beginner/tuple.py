#!/usr/bin/python 
#define an empty tuple
tuple = ()
#a comma is required for a tuple with one item
tuple = (3,)

personInfo = ("Diana",32,"New York")

#data access 
print(personInfo[0])
print(personInfo[1])
	
#assign multiple variables at once
name,age,country,career = ('Diana',32,'Canada','CompSci')
print(country)

#append to an existing tuple
x = (3,4,5,6)
x = x + (1,2,3)
print(x)



