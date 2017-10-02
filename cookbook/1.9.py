#!/usr/bin/python3 
#Usage : python3 $0

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
common = a.keys() & b.keys()
print (common)

#Find keys in a that are not in b 
diff = a.keys() - b.keys()
print (diff)

#find (key,value)pairs in common
pair = a.items() & b.items()
print (pair)

#make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys()-{'z','w'}}
print (c)
