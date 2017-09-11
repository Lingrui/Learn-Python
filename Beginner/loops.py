#!/usr/bin/python 

items = ["Abby","Brenda","Cindy","Diddy"]

for item in items:
	print(item)

for i in range(1,10):
	print(i)

correctNumber = 5 
guess = 0 

##while loop 
while guess != correctNumber:
	guess = int(input("Guess the number: "))
	if guess != correctNumber:
		print('False guess ')
print('You guessed the correct number')


###nested loops
for x in range(1,10):
	for y in range(1,10):
		print("(" + str(x) + "," + str(y) + ")")

