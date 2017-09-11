#!/usr/bin/python
class Employee:
	def __init__(self,name,salary):
		self.salary = salary
		self.name = name

james = Employee("James","1200")

print (james.name)
print (james.salary)
