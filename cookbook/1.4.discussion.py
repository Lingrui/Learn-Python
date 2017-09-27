#!/usr/bin/python 
import heapq 
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
print heap

x = heapq.heappop(heap)
print x 
y = heapq.heappop(heap)
print y
z = heapq.heappop(heap)
print z 
