#!/usr/bin/python 

words = [
	'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
	'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
	'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
	'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_counts = Counter(words)
print (word_counts)
top_three = word_counts.most_common(3)
print(top_three)

print(word_counts['not'])
print(word_counts['eyes'])

morewords = ['why','are','you','not','looking','in','my','eyes' ]
for word in morewords:
	word_counts[word] += 1 

print(word_counts['eyes'])

##or use the update() method
update_data = ['why','looking','eyes','eyes']
word_counts.update(update_data)
print(word_counts)

##operation##
a = Counter(words)
b = Counter(morewords)
print("Counter a is: " + str(a))

print("Counter b is: " + str(b))

##combine counts 
c = a + b 
print("c = a + b\nc is:" + str(c))

##subtract counts 
d = a - b 
print('d = a - b\nd is:' + str(d))
	
