#!/usr/bin/python 
from collections import deque

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print q 
q.append(4)
print q	
q.append(5)
print q


###############
q = deque()
q.append(1)
q.append(2)
q.append(3)
print q
q.appendleft(4)
print q 
j = q.pop()
print j 
print q 
i = q.popleft()
print i 

