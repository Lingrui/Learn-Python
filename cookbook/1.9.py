#!/usr/bin/python 
a = {
	'x':1,
	'y':2,
	'z':3
}

b = {
	'w':10,
	'x':11,
	'y':2
}

#Find keys in common
#a.keys() & b.keys() #{'x','y'}

c = {key:a[key] for key in a.keys()-{'z','w'}}
