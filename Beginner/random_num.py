#!/usr/bin/python 
##random number between 0 and 1 
from random import * 
print random()

#generate a random number between 1 and 100
from random import * 
print randint(1,100)  ##pick a random number between 1 and 100 

#store it in a vairable 
from random import * 
x = randint(1,100)
print x

##random number between 1 and 10 
from random import * 
print uniform(1,10)

##fun with list 
#shuffle a list 
from random import * 
items = [1,2,3,4,5,6,7,8,9,10]
shuffle(items)
print items 

#pick a random number from a list 
from random import * 
items = [1,2,3,4,5,6,7,8,9,10]
x = sample(items, 1)
print x[0]
y = sample(items,4)
print y 

## same thing with a list of strings 
items = ['Alissa','Alice','Marco','Melissa','Sandra','Steve']
x = sample(items,1)
print x[0]

y = sample(items,2)
print y
