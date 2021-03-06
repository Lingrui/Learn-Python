#!/usr/bin/python 

rows = [ 
	{'fname':'Brain','lname':'Jones','uid':1003},
	{'fname':'David','lname':'Beazley','uid':1002},
	{'fname':'John','lname':'Cleese','uid':1001},
	{'fname':'Big','lname':'Johes','uid':1004}
]

from operator import itemgetter 
print('sort by fname')
rows_by_fname = sorted(rows,key=itemgetter('fname'))
print(rows_by_fname)

print('sort by uid')
rows_by_uid = sorted(rows,key=itemgetter('uid'))
print(rows_by_uid)

print('sort by multiply keys: lname and fname')
rows_by_lfname = sorted(rows,key=itemgetter('lname','fname'))
print(rows_by_lfname)

###itemgetter sometimes replaced by lambda expression 
print('##lambda expresion###')
rows_by_fname = sorted(rows,key=lambda r:r['fname'])
print(rows_by_fname) 
rows_by_lfname = sorted(rows,key=lambda r:(r['lname'],r['fname']))

###min and max 
print("max")
print(min(rows,key=itemgetter('uid')))
print("min")
print(max(rows,key=itemgetter('uid')))

