from __future__ import division
import string, re, itertools, time
from test_module import timedcall #importing function "timedcall" from file in the directory "test_module"
from compile_word import compile_word

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

def faster_solve(formula):
    """Given a formula like 'ODD + ODD == EVEN',fill in digits tp solve it/
    Input formula is a string; output is a digit-filled-in string or None.
    This version precompiles the formula; only 1 eval per formula """
    f, letters = compile_formula(formula)
    for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
        try:
            if f(*digits) is True:
                table = string.maketrans(letters,''.join(map(str, digits)))
                return formula.translate(table)
        except ArithmeticError:
            pass

def compile_formula(formula, verbose=False):
    """Compile formula into a function. Also return letters found, as a str,
    in some order as parms of function. For example, 'YOU == ME**2' returns
    (lamda Y,M,R,U,O: (U+10*O+100*Y) == (E+10*M)**2),'YMEUO')"""
    letters = ''.join(set(re.findall('[A-Z]',formula)))
    parms = ','.join(letters)
    tokens = map(compile_word,re.split('([A-Z]+)',formula))
    body = ''.join(tokens)
    f = 'lambda %s: %s' % (parms, body)
    if verbose: print f
    return eval(f), letters



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
        print '%6.4f sec:    %s '%timedcall(faster_solve,example)
    print '%6.4f tot.' %(time.clock()-t0)
test()

#import cProfile
#cProfile.run('test()') # or it could be done in cmd "python -m cProfile 'brute_force.py' "