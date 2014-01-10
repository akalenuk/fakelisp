from fakelisp import *

(BEGIN
	(SET (F) (LAMBDA (X)
		(IF (EQ (X) (1))
			(1)
			(MUL (X) (F (SUB (X) (1)))))))

	(SET (X) (QUOTE (F (4)) (42))))

print X

# Yes, it does print [24, 42].
#
# Isn't it awesome?
