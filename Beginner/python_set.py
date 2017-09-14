#!/usr/bin/python 
x = set(["Postcard","Radio","Telegram"])
print(x)
#simplified notation
y = {"Postcard","Radio","Telegram"}
print(y)

#clear elements from set 
print "####clear element from set####"
x = set(["Postcard","Radio","Telegram"])
x.clear()
print(x)

#remove element from set
print "####remove element from set####"
x = set(["Postcard","Radio","Telegram"])
x.remove("Radio")
print(x)

print "####difference between two sets###"
x = set(["Postcard", "Radio", "Telegram"])
y = set(["Radio","Television"])
print (x) 
print (y)
print (x.difference(y))
print (y.difference(x))
	
print "###to test if a set is a subset###"
x = set(["a","b","c","d"])
y = set(["c","d"])
print(x.issubset(y))
print(y.issubset(x))

print "###to test if a set is a super set####"
print(x.issuperset(y))
print(y.issuperset(x))

print "####to test for intersection###"
print(x.intersection(y))
print(y.intersection(x))
