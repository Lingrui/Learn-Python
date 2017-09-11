#!/usr/bin/python 
###class######
## The __init__()  method is called the constructor and is always called when creating an object.
class User:
	name = ""
	def __init__(self,name):
		self.name = name
	
	def sayHello(self):
		print "Hello, my name is " + self.name
#creat virtual objects 
james = User("James")
david = User("David")
eric = User("Eric")


#call methods owned by virtual objects
james.sayHello()
david.sayHello()

###class variables
class CoffeeMachine:
	name = ""
	beans = 0 
	water = 0 

	def __init__(self,name,beans,water):
		self.name = name 
		self.beans = beans 
		self.water = water

	def addBean(self):
		self.beans = self.beans + 1 

	def removeBean(self):
		self.beans = self.beans - 1 

	def addWater(self):
		self.water = self.water + 1 
	
	def removeWater(self):
		self.water = self.water - 1 

	def printState(self):
		print "Name = " + self.name
		print "Beans = " + str(self.beans)
		print "Water = " + str(self.water)

pythonBean = CoffeeMachine("Python Bean", 83,20)
pythonBean.printState()
print ""
pythonBean.addBean()
pythonBean.printState()
