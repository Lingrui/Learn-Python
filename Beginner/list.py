#!/usr/bin/python 
#define list with brackets[]
l = ["Drake","Derp","Derek","Dominique"]
print(l) ## print all elements
print(l[0]) # print first element
print(l[1])

#add/remove
l.append("Victoria") #add element
print(l)
l.remove("Derp")
l.remove("Drake")
print(l)

#sort list 
l.sort()   # sort the list in alphabetical order 
print(l)

#descending order 
l.sort() 
l.reverse() #reverse order 
print(l)
