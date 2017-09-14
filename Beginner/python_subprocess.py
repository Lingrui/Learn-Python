#!/usr/bin/python 

from subprocess import Popen,PIPE

process = Popen(['cat','test.py'],stdout=PIPE,stderr=PIPE)
stdout,stderr = process.communicate()
print stdout


print "#####subprocess call()######"
import subprocess 
#full definition is :
#subprocess.call(arg,*,stdin=None,stdout=None,stderr=None,shell=False)
subprocess.call(['ls','-l'])

print "####save process output(stout)#####"
#subprocess.check_output(arg,*,stdin=None,strerr=None,shell=False,universal_newlines=False)
s = subprocess.check_output(['echo','Hello World!'])
print("s = " + s)
