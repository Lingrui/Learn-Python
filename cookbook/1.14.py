#!/usr/bin/python 
class User:
	def __init__(self,user_id):
		self.user_id = user_id
	def __repr__(self):
		return 'User({})'.format(self.user_id)

users = [User(23),User(3),User(99)]
print (users)
print (sorted(users,key=lambda k:k.user_id))
	
# use operator.attrgetter() instead of using lambda

from operator import attrgetter 
print (sorted(users, key=attrgetter('user_id')))

#allowing multiple field to be extracted simultaneously
'''
rows = [ 
	{'fname':'Brain','lname':'Jones','uid':1003},
	{'fname':'David','lname':'Beazley','uid':1002},
	{'fname':'John','lname':'Cleese','uid':1001},
	{'fname':'Big','lname':'Johes','uid':1004}
]

by_name = sorted(rows, key=attrgetter('lname','fname'))
print(by_name)
'''
print(min(users,key= attrgetter('user_id')))
print(max(users,key= attrgetter('user_id')))
