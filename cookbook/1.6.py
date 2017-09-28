#!/usr/bin/python 
###list preserve the insertion order of the items
d = {
	'a':[1,2,3],
	'b':[4,5]
}

##set eliminate the duplicate and don't care about the orders
e = {
	'a':{1,2,3},
	'b':{4,5}
}

print d 
print e 

##defaultdict could automatically initialized the first value 
from collections import defaultdict 
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
d['c'].append(5)
print '####defaultdict list####'
print d 

d = defaultdict(set)
d['a']
print 'defauldict set test '
print d 
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print '####defaultdict set####'
print d

d = {}
print '######'
d.setdefault('a',[])
print d
d.setdefault('a',[]).append(1)
d.setdefault('a',[]).append(2)
d.setdefault('b',[]).append(4)
print '####set default###'
print d

#######example####
d = defaultdict(list)
for key, value in pairs:
	d[key].append(value)




