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
