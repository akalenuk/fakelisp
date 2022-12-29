fakelisp
========

This is a fake Lisp implementation in Python. No-no-no, not written in Python, it *is in Python*. You just have to import it:
```python
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
```

It prints

    [24, 42]
    
Yes, you do have to enclose every list element in a bracket. More brackets - more fun!

And you can only use one letter identifiers without further declarations. But who needs all that monstrous naming anyway.

Otherwise, it is a perfect Lisp inside Python. It looks like Lisp, it works like Lisp, so in spirit or Python typing, it is Lisp. It has no dependencies, doesn't use "eval" and the core code is only a hundred lines including license!

But seriously, it is fake after all. If you are looking for a nice and small Lisp implementation in Python, see http://norvig.com/lispy.html

And if you want a Python with Lisp-ish syntax, try http://julien.danjou.info/blog/2013/lisp-python-hy

My fakelisp is literally _fake Lisp_. It is just a bunch of hacks making valid python code look lisp-ish. Check the code, it's really tiny!


P. S. For another example of Python syntax misuse check ArrPL: https://github.com/akalenuk/arrpl It's an array processing library inspired by APL.

P. S. S. Yes. it's in Python 2. I wrote it about a decade ago and never bothered to redo it in Python 3. They took my `reduce` away from the core, packed it into a library, and this broke the compatibility. And the pureness of the implementation :-(
