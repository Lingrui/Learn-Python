#!/usr/bin/python 
#bin()  binary  0bxxxx
#bitwise left operator(<<) to shift left and bitwise right operate(>>) to shift right 
inputA = int('0101',2) 

print "Before shifting " + str(inputA) + " " + bin(inputA)
print "After shifting in binary: " + bin(inputA << 1)
print "After shifting in decimal: " + str(inputA << 1)

# the AND operator 
print "the AND operator"
inputA = 1 
inputB = 1 
print inputA & inputB ##Bitwise AND 

inputA = int('00100011',2)
inputB = int('00101101',2)
print bin(inputA & inputB)

# the OR operator 
print "the OR operator"
print bin(inputA)
print bin(inputB)
print bin(inputA | inputB)

#the XOR operator 
print "the Exclusive OP or shortly XOR"
print bin(inputA ^ inputB)
