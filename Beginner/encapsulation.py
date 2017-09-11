#!/usr/bin/python
class Car:
	def __init__(self):
		self.__updateSoftware()

	def drive(self):
			print 'driving'

	def __updateSoftware(self):
		print 'updating software'

redcar = Car()
redcar.drive()

###private vairable 
#a private vaiable can only be changed within a class method and not outside of the class

print '#####Private vaiable######'
class pvcar:
	__maxspeed = 0
	__name = ""

	def __init__(self):
		self.__maxspeed = 200
		self.__name = "Supercar"

	def drive(self):
		print 'driving. maxspeed ' + str(self.__maxspeed)
		print self.__name

redcar = pvcar()
redcar.drive()
redcar.__maxspeed = 10 
redcar.drive()

##set the value of a private vairable
print '###change the value of a private variable'
class change:
	__maxspeed = 0 
	__name = ""

	def __init__(self):
		self.__maxspeed = 200 
		self.__name = "SuperCar"
	
	def drive(self):
		print 'driving. maxspeed ' + str(self.__maxspeed)
	
	def setMaxSpeed(self,speed):
		self.__maxspeed = speed 

redcar = change()
redcar.drive()
redcar.setMaxSpeed(320)
redcar.drive()

###description 
print '#####Descriptions#######'
print 'public methods:'
print '		Accessible from anywhere'
print 'private methods:'
print '		Accessible only in their own class, starts with two underscores'
print 'public variables'
print '		Accessible from anywhere'
print 'private variables'
print '		Accessible only in their own class or by a method is defined, starts with two underscores'
