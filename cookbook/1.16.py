#!/usr/bin/python 

mylist = [1,4,-5,10,-7,2,3,-1]
a = [n for n in mylist if n > 0]
print(a)
b = [n for n in mylist if n < 0]
print(b)
# use generator expressions to produce the filtered values iteratively
for x in b:
	print(x)

#if the filtering criteria cannot be easily expressed in a list 
values = ['1','2','-3','-','4','N/A','5']

def is_int(val):
	try:
		x = int(val)
		return True
	except ValueError:
		return False
###filter(criteria_function,data)
ivals = list(filter(is_int,values))
print(ivals)


import math 
c = [math.sqrt(n) for n in mylist if n > 0]
print(c)

## clip bad values 
clip_neg = [n if n > 0 else 0 for n in mylist]
print (clip_neg)

clip_pos = [n if n < 0 else 0 for n in mylist]
print (clip_pos)

##itertools.compress() takes an iterable and an caaompanying Boolean selector sequence as input 
addresses = [
	'5412 N CLARK',
	'5148 N CLARK',
	'5800 E 58TH', 
	'2122 N CLARK',
	'5645 N RAVENSWOOD'
	'1060 W ADDISON',
	'4801 N BROADWAY'
	'1039 W GRANVILLE',
]

counts = [0,3,10,4,1,7,6,1]

from itertools import compress 
more5 = [n > 5 for n in counts]
print(more5)
x = list(compress(addresses,more5))
print (x)

#filter(), compress() normally returns an iterator, usually need to use list() to turn the result into a list 
