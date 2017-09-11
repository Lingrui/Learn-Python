#!/usr/bin/python 

x = 3 
if x < 10: 
	print("x smaller than 10")
else:
	print("x is bigger than 10 or equal")


#guess age game
age = 24 
print "Guess y age, you have 1 chances!"
guess = int(raw_input("Guess:"))

if guess != age:
	print("Wrong!")
else:
	print("Correct")

##Nesting 
a = 12 
b = 33 

if a > 10: 
	if b > 20: 
		print("Good")

guess = 24 
if guess > 10 and guess < 20:  ##combine conditions 
	print("In range")
else: 
	print("Out of range")
