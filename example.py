from fakelisp import *

# And now you can start mixing Python and LISP
X = (BEGIN
        (SET (F) (LAMBDA (X)
            (IF (EQ (X) (1))
                (1)
                (MUL (X) (F (SUB (X) (1)))))))

        (LIST (F (4)) (42)))

# Back to Python any time
print "x: ", str(X)

# It prints [24, 42]
