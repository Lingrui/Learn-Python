#!/usr/bin/python 
######   '0123456789012345678901234567890123456789012345678901234567890'
record = '....................100          .......513.253    ..........'
cost = int(record[20:32]) * float(record[40:48])
print cost

##name the slices
SHARES = slice(20,32)
PRICE  = slice(40,48)

cost = int(record[SHARES]) * float(record[PRICE])
print cost


##built-in slice()
print "#####built-in slice#####"
items = [0,1,2,3,4,5,6]
a = slice(2,4)
print items[2:4]
print items[a]
items[a] = [10,11]
print items

del items[a]
print items


### slice instance s 
print "#####slice instance s####"
a = slice(10,50,2)
print a.start
print a.stop 
print a.step


###indices(size) method###
print "###indices(size) method ####"
s = 'HelloWorld'
print a.indices(len(s))
print '###########################'
for i in range(*a.indices(len(s))):
	print(s[i])
