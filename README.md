fakelisp
========

This is a fake Lisp implementation in the Python itself. It is not only written in Python, but it works in the Python as well. I mean, you don't have to run anything, just do this:
```python
from fakelisp import *

# and now you can write lisp
X = (BEGIN
		(SET (F) (LAMBDA (X)
			(IF (EQ (X) (1))
				(1)
				(MUL (X) (F (SUB (X) (1)))))))

		(QUOTE (F (4)) (42)))

# back to Python
print "x: ", X
```

It prints

    [24, 42]
    
Yes, you do have to enclose every list element in a bracket. More brackets - more fun!

And you can only use one letter identifiers without further declarations. But who needs all that monstrous naming anyway.

Otherwise, it is a perfect lisp inside Python. It looks like lisp, it works like lisp, so by duck typing principle, it is lisp. It has no dependencies, doesn't use "eval" and the core code is only a hundred lines including license!

But seriously, it is fake after all. If you are looking for a lisp implementation in Python, see http://norvig.com/lispy.html

And if you want a python with lispish syntax, try http://julien.danjou.info/blog/2013/lisp-python-hy

My fakelisp is literally _fake Lisp_. It is just a bunch of hacks making valid python code look lisp-ish. Check the code, it's really tiny!


P. S. For another example of Python syntax misuse check ArrPL: https://github.com/akalenuk/arrpl It's an array processing library inspired by APL.
