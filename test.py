from fakelisp import *
import sys

sys.setrecursionlimit(100)  # to fail faster

def check(a, x, s):
    if str(x) == str(s):
        print "Check! " + a + "."
    else:
        print a + " failed. - found " + str(x) + " instead of " + str(s)


check("Nested Fun", (SUB (4) (SUB (3) (2))), 3)

check("BEGIN (X=2, Y=3, Z=3)", BEGIN
    (SET (Z) (3))
    (SET (X) (2))
    (SET (Y) (3)) 
    (ADD (X) (Y)), 5)

check("SET Z", (Z), 3)

check("IF X==3", (IF (EQ (X) (3)) (1) (0)), 0)

check("LIST", (LIST (1) (ADD (4) (SUB (6) (3)))), [1, 7] )

TWICE = Fun()
s(SET (TWICE) (LAMBDA (Z) (MUL (Z) (2))))

check("Fun as value", (TWICE (1)), 2)
check("Nested Fun", (TWICE (TWICE (3))), 12)
check("Global Z after", (Z), 3)

PLUS = Fun()
s(SET (PLUS) (LAMBDA ((X) (Y)) (ADD (X) (Y))))

check("2-arg Fun", (PLUS (2) (3)), 5)

s(SET (TWICE) (LAMBDA (X) (MUL (X) (2))))
check("Global var reuse", (TWICE (1)), 2)

T = Fun()
s(SET (T) (LAMBDA (X) (TWICE (X))))
check("Global LAMBDA reuse", (T (4)), 8)

F = Fun(None)
s(SET (F) (LAMBDA (X)
    (IF (EQ (X) (1))
        (1)
        (MUL (X) (F (SUB (X) (1)))))))

check("Recursion", (F (4)), 24)

check("List operations", (CAT 
		(LIST (HEAD (LIST (1) (2) (3) (4)))) 
		(TAIL (LIST (1) (2) (3) (4))) 
		(LIST (5))), [1,2,3,4,5])

A2X = Fun()
s(SET (A2X) (LAMBDA (X)
(IF (EQ (X) (LIST))
	(LIST)
	(CAT 
		(LIST (MUL (2) (HEAD (X))))
		(A2X (TAIL (X)))))))
check("Array processing", (A2X (LIST (1) (2) (3))), [2,4,6])

TWICE = Fun()
s(SET (TWICE) (MUL (2)))    
check("Pointless notation", (TWICE (6)), 12)

s(SET (F) (LAMBDA (X) (ADD (X) (21))))
s(SET (G) (LAMBDA (X) (X (12))))
check("1-class LAMBDAS", (G (F)), 33)
