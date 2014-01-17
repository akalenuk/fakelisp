#!/usr/bin/python
#
# Copyright 2014 Alexandr Kalenuk.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# mailto: akalenuk@gmail.com


# W A R N I N G ! This is not an actual Lisp.

class Fun:
    def __init__(self, fun_stack = None, chain = []):
        if isinstance(fun_stack, list):
            self.fun_stack = fun_stack
        else:
            self.fun_stack = [fun_stack]
        self.chain = chain
    def __call__(self, next_arg):
        return Fun(self.fun_stack, self.chain + [next_arg])
    def __repr__(self):
        return str(s(self))
    def push_fun(self, fun):
        self.fun_stack += [fun]
    def pop_fun(self):
        self.fun_stack = self.fun_stack[:-1]


def l(args, body, x):
    map (lambda (arg, val): arg.push_fun( lambda *a : val ), zip(args, x))
    r = s(body)
    map (lambda arg: arg.pop_fun(), args)
    return r

def a(var, value):
    if isinstance(value, Fun):
        var.fun_stack[-1] = value.fun_stack[-1]
    else:
        var.fun_stack[-1] = lambda *x: value

def s(x):
    if isinstance(x, list):
        return [s(xi) for xi in x]
    if isinstance(x, Fun):
        return s(x.fun_stack[-1]( *(x.chain) ))
    else:
        return x


LAMBDA = lambda args: lambda body: Fun(lambda *x: l([args] + args.chain, body, s(list(x))))
SET = Fun(lambda var, value: a(var, value))
IF = Fun(lambda c, r1, r2: r1 if s(c) else r2)

QUOTE = Fun(lambda *x: s(list(x)))
BEGIN = Fun(lambda *x: s(list(x))[-1])
HEAD = Fun(lambda x: s(x)[0])
TAIL = Fun(lambda x: s(x)[1:])
CAT = Fun(lambda *x: reduce(lambda a, b: s(a) + s(b), x))

EQ = Fun(lambda a, b: s(a) == s(b))
NEQ = Fun(lambda a, b: s(a) != s(b))
LS = Fun(lambda a, b: s(a) < s(b))
GR = Fun(lambda a, b: s(a) > s(b))
LSE = Fun(lambda a, b: s(a) <= s(b))
GRE = Fun(lambda a, b: s(a) >= s(b))
NOT = Fun(lambda a: not s(a))
OR = Fun(lambda a, b: s(a) or s(b))
AND = Fun(lambda a, b: s(a) and s(b))
ADD = Fun(lambda *x: sum(s(list(x))))
SUB = Fun(lambda a, b: (s(a) - s(b)))
MUL = Fun(lambda *x: reduce(lambda a,b: s(a)*s(b), x))
DIV = Fun(lambda a, b: (s(a) / s(b)))


A = Fun(); B = Fun(); C = Fun(); D = Fun(); E = Fun(); F = Fun(); G = Fun(); H = Fun(); 
I = Fun(); J = Fun(); K = Fun(); L = Fun(); M = Fun(); N = Fun(); O = Fun(); P = Fun(); 
Q = Fun(); R = Fun(); S = Fun(); T = Fun(); U = Fun(); V = Fun(); W = Fun(); 
X = Fun(); Y = Fun(); Z = Fun()


if __name__ == '__main__':
    def check(a, x, s):
        if str(x) == str(s):
            print a+"      \tok"
        else:
            print a+" - found " + str(x) + " instead of " + str(s)


    check("subsub", (SUB (4) (SUB (3) (2))), 3)
    
    check("begin", BEGIN
        (SET (Z) (3))
        (SET (X) (2))
        (SET (Y) (3)) 
        (ADD (X) (Y)), 5)

    check("set Z", (Z), 3)

    check("if X==3", (IF (EQ (X) (3)) (1) (0)), 0)
    
    check("quote", (QUOTE (1) (ADD (4) (SUB (6) (3)))), [1, 7] )

    TWICE = Fun()
    s(SET (TWICE) (LAMBDA (Z) (MUL (Z) (2))))
    
    check("lambda1", (TWICE (1)), 2)
    check("lambda1", (TWICE (2)), 4)
    check("lambda1", (TWICE (TWICE (3))), 12)
    check("Z after", (Z), 3)

    PLUS = Fun()
    s(SET (PLUS) (LAMBDA ((X) (Y)) (ADD (X) (Y))))

    check("lambda2", (PLUS (2) (3)), 5)

    check("2x twice", (TWICE (TWICE (1))), 4)

    s(SET (TWICE) (LAMBDA (X) (MUL (X) (2))))
    check("x reuse", (TWICE (1)), 2)
   
    T = Fun()
    s(SET (T) (LAMBDA (X) (TWICE (X))))
    check("\\ x reuse", (T (4)), 8)


    F = Fun(None)
    s(SET (F) (LAMBDA (X)
        (IF (EQ (X) (1))
            (1)
            (MUL (X) (F (SUB (X) (1)))))))

    check("fact", (F (4)), 24)
   
    check("lists", (CAT 
			(QUOTE (HEAD (QUOTE (1) (2) (3) (4)))) 
			(TAIL (QUOTE (1) (2) (3) (4))) 
			(QUOTE (5))), [1,2,3,4,5])

    A2X = Fun()
    s(SET (A2X) (LAMBDA (X)
	(IF (EQ (X) (QUOTE))
		(QUOTE)
		(CAT 
			(QUOTE (MUL (2) (HEAD (X))))
			(A2X (TAIL (X)))))))
    check("array", (A2X (QUOTE (1) (2) (3))), [2,4,6])
