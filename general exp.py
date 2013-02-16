def sq(x): print 'sq called',x; return x * x

g = (sq(x) for x in range(10) if x%2 == 0)
next(g)
next(g)


for x2 in (sq(x) for x in range(10) if x%2 == 0): pass

print list((sq(x) for x in range(20) if x%2 == 0))