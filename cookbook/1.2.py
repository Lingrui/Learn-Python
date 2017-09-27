#!/usr/bin/python 
#"star expression"
'''
def drop_first_last(grades):
	first, *middle, last = grades 
	return avg(middle)
'''

*trailing,current = [10,8,7,1,9,5,10,3]
print trailing
print current 
trailing_avg = sum(trailing)/len(trailing)
print trailing_avg

