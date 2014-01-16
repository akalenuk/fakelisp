from fakelisp import *

# And now you can write lisp
X = (BEGIN
	(SET (F) (LAMBDA (X)
		(IF (EQ (X) (1))
			(1)
			(MUL (X) (F (SUB (X) (1)))))))

	(QUOTE (F (4)) (42)))

# Back to Python any time
print "x: ", X

# It does print [24, 42], but better check it yourself
