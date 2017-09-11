#!/usr/bin/python 

#string input and output 
s = "hello world"
print(s)

#get text from keyboard 
name = raw_input("Enter name:")
print(name)

#string comparison
sentence = "The cat is brown"
q = "cat"
if q == sentence:
	print('strings equal')

if q != sentence:
	print('strings not equal')
