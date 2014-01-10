fakelisp
========

This is a fake Lisp implementation in the Python itself. It is not only written in Python, but it works in the Python as well. I mean, you don't have to run anything, just do this:

    from fakelisp import *

    # and now you can write lisp!
    (BEGIN
      (SET (F) (LAMBDA (X)
        (IF (EQ (X) (1))
          (1)
          (MUL (X) (F (SUB (X) (1)))))))

      (SET (X) (QUOTE (F (4)) (42))))

    print X

It prints

    [24, 42]
    
Yes, you do have to enclose every list element in a bracet. More bracets, isn't it wonderful!

And you can use only X, Y and Z as a variable and F and G as a function without further declarations. But who needs all that other names anyway.


Seriously, if you are looking for a lisp implementation in Python, see http://norvig.com/lispy.html

And if you want a python with lispish syntax, try http://julien.danjou.info/blog/2013/lisp-python-hy

My fakelisp is literally _fake Lisp_. It's a bunch of hacks making valid python code look a little like lisp, no more than that. Check the code!


P. S. For another example of Python syntax misuse check ArrPL: https://github.com/akalenuk/arrpl It's an array processing library inspired by APL.
