
 #    There are five houses.
 #    The Englishman lives in the red house.
 #    The Spaniard owns the dog.
 #    Coffee is drunk in the green house.
 #    The Ukrainian drinks tea.
 #    The green house is immediately to the right of the ivory house.
 #    The Old Gold smoker owns snails.
 #    Kools are smoked in the yellow house.
 #    Milk is drunk in the middle house.
 #    The Norwegian lives in the first house.
 #    The man who smokes Chesterfields lives in the house next to the man with the fox.
 #    Kools are smoked in the house next to the house where the horse is kept. [should be "... a house ...", see discussion below]
 #    The Lucky Strike smoker drinks orange juice.
 #    The Japanese smokes Parliaments.
 #    The Norwegian lives next to the blue house.

	# Now, who drinks water? Who owns the zebra? 
	
import itertools

def imright(h1,h2):
	return h1-h2==1

def nextto(h1,h2):
	return abs(h1-h2)==1

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