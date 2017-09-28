#!/usr/bin/python 

prices = {
	'ACME':45.23,
	'AAPL':612.78,
	'IBM':205.55,
	'HPQ':37.20,
	'FB':10.75
}

print '#invert the keys and values of the dictionary using zip()###'
min_price = min(zip(prices.values(),prices.keys()))
print 'min price is:' , min_price

max_price = max(zip(prices.values(),prices.keys()))
print 'max price is:' , max_price

prices_sorted = sorted(zip(prices.values(),prices.keys()))
print 'sorted price is:' , prices_sorted

print '\n##zip()creats an iterator that can only be consumed once##'
prices_and_names = zip(prices.values(),prices.keys())
print( min(prices_and_names))
prices_and_names = zip(prices.values(),prices.keys())
print (max(prices_and_names))


print '##only process the keys##'
print min(prices)
print max(prices)

print '##perform a calculation involving the dictionary values##'
print min(prices.values())
print max(prices.values())

print '##get the key corresponding to the min or max value##'
print min(prices, key= lambda k:prices[k])
print max(prices, key= lambda k:prices[k])

print '##to get the minimum value'
min_value = prices[min(prices,key=lambda k:prices[k])]
print min_value
