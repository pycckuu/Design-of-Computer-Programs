from __future__ import division
import string, re, itertools, time
from test_module import timedcall #importing function "timedcall" from file in the directory "test_module"

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for f in fill_in(formula):
        if valid(f):
            return f
    
def fill_in(formula):
    "Generate all possible fillings-in of letters in formula with digits."
    letters = ''.join(set(re.findall('[A-Z]',formula))) #usin RegExp to make a set of letters from formula
    for digits in itertools.permutations('1234567890', len(letters)): #intereate through all posibilities in gigits to letters
        table = string.maketrans(letters, ''.join(digits)) #making like dictionary for let:dig map
        yield formula.translate(table) #returning the formula in digit manner
    
def valid(f):
    """Formula f is valid if and only if it has no 
    numbers with leading zero, and evals true."""
    try: 
        return not re.search(r'\b0[0-9]', f) and eval(f) is True 
    except ArithmeticError:
        return False


examples = """TWO + TWO == FOUR
A**2 + B**2 == C**2
A**2 + BE**2 == BY**2
X/X == X
A**N + B**N == C**N and N > 1
ATOM**0.5 == A + TO + M
GLITTERS is not GOLD
ONE < TWO and FOUR < FIVE
ONE < TWO < THREE
RAMN == R**3 + RM**3 == N**3 + RX**3
sum(range(AA)) == BB
sum(range(POP)) == BOBO
ODD + ODD == EVEN
PLUTO not in set([PLANETS])""".splitlines()

def test():
    t0 = time.clock()
    for example in examples:
        print 
        print '              ', example
        print '%6.4f sec:    %s '%timedcall(solve,example)
    print '%6.4f tot.' %(time.clock()-t0)

test()