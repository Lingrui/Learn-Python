#!/usr/bin/python 

p = (4,5)
x,y = p 
print x
print y

data = ['ACME',50,91.1,(2012,12,21)]
name,shares,price,date = data
print name
print date

name,shares,price,(year,mon,day) = data 
print name 
print year 
print mon 
print day

##unpacking with tuples, lists, strings,iterators, and generators
s = 'Hello'
a,b,c,d,e = s 
print a 
print b 
print e 

##discard certain values 
data = ['ACME',50,91.1,(2012,12,21)]
_, shares, price, _ = data 
print shares
print price 
