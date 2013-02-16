import itertools

#imright = 

def zebra_puzzle():
	houses = [first,_,midle,_,_] = [1, 2, 3, 4, 5]
	orderings = list(itertools.permutations(houses))
	return next((WATER, ZEBRA)
		for (red, green, ivory, yellow, blue) in orderings
		if imright(green, ivory)			#6
		for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
		if Englishman is red 				#2
		if Norwegian is first				#10
		if nextto(Norwegian,blue)			#15
		for (coffee, tea, milk, oj, WATER) in orderings
		if coffee is green
		if Ukranian is tea 
		if milk is midle
		for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
		if Kools is yellow
		if LuckyStrike is oj 
		if Japanese is Parliaments
		for (dog, snails, fox, horse, ZEBRA) in orderings
		if Spaniard is dog
		if OldGold is snails
		if nextto(Chesterfields, fox)
		if nextto(Kools, horse)
		)




import time

def t():
	t0 = time.clock()
	zebra_puzzle()
	t1 = time.clock()
	return t1-t0

def timecall(fn):
	"Call function and return time"
	t0 = time.clock()
	fn()
	t1 = time.clock()
	return t1-t0

def timedcall(fn, *args):
	"Call function with args; return the time in seconds and result"
	t0 = time.clock()
	result = fn(*args)
	t1 = time.clock()
	return t1-t0, result


print timedcall(zebra_puzzle)