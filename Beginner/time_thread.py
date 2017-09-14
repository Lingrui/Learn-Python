#!/usr/bin/python 

from threading import *
def hello():
	print "hello,world"
t = Timer(10.0,hello)
t.start()
