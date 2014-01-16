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

MAX_RECURSION_DEPTH = 42

common_id = 0 
fun_map = {}

class Fun:
    def __init__(self, fun = None, chain = [], uid = None):
        if uid != None:
            self.uid = uid
        else:
            global common_id
            common_id += 1
            self.uid = common_id
            fun_map[self.uid] = fun        
        self.chain = chain
    def __call__(self, next_arg):
        return Fun(None, self.chain + [next_arg], self.uid)
    def __repr__(self):
        return str(s(self))
        
class Var:
    def __init__(self, val = None):
        self.chain = [self]
        self.val = val
    def __call__(self, next_var):
        self.chain += [next_var]
        return self
    def __repr__(self):
        return str(self.val)        
    
rc = 0
class LAMBDA:
    def __init__(self, args):
        self.args = [a for a in args.chain]
    def __call__(self, body):
        def l(args, body, x):
            def assign_val((a, x)):
                a.val = x

            old_x = [arg.val for arg in args]
            map(assign_val, zip(args, x))
            
            global rc
            rc += 1
            if rc < MAX_RECURSION_DEPTH:
                r = s(body)
            else:
                r = 0
            rc -= 1
            
            map(assign_val, zip(args, old_x))
            return r
        return Fun(lambda *x: l(self.args, body, s(list(x))))

class SET:
    def __init__(self, var):
        self.var = var
    def __call__(self, value):
        if isinstance(self.var, Var):
            self.var.val = s(value)
        elif isinstance(self.var, Fun):
            fun_map[self.var.uid] = fun_map[value.uid]
        return None

def s(x):
    if isinstance(x, list):
        return [s(xi) for xi in x]
    if isinstance(x, Fun):
        return s(fun_map[x.uid]( *(x.chain) ))
    if isinstance(x, Var):
        return x.val
    else:
        return x
        

QUOTE = Fun(lambda *x: s(list(x)))
BEGIN = Fun(lambda *x: s(list(x))[-1])
IF = Fun(lambda c, r1, r2: r1 if s(c) else r2)

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

I = Var(); J = Var(); K = Var(); L = Var(); M = Var(); N = Var(); O = Var(); P = Var(); 
Q = Var(); R = Var(); S = Var(); T = Var(); U = Var(); V = Var(); W = Var(); 
X = Var(); Y = Var(); Z = Var()


if __name__ == '__main__':
    PLUS = Fun()
    TWICE = Fun()
        
    print "subsub 3 =", (SUB (4) (SUB (3) (2)))
        
    (SET (Z) (3))
    print "set Z 3 =", (Z)
        
    print "begin 5 =", (BEGIN 
        (SET (X) (2)) 
        (SET (Y) (3)) 
        (ADD (X) (Y)))
        
    print "if 0 =", (IF (EQ (X) (3)) (1) (0))
        
    print "quote [1, 7] =", (QUOTE (1) (ADD (4) (SUB (6) (3))) )
    
    (SET (TWICE) (LAMBDA (Z) (MUL (Z) (2))))
    print "lambda1 2 =", (TWICE (1))
    print "lambda1 4 =", (TWICE (2))
    print "lambda1 12 =", (TWICE (TWICE (3)))
    print "Z after 3 =", (Z)
    

    (SET (PLUS) (LAMBDA ((X) (Y)) (ADD (X) (Y))))

    print "lambda2 5 =", (PLUS (2) (3))

    print "2x twice 4 =", (TWICE (TWICE (1)))
    
    (SET (TWICE) (LAMBDA (X) (MUL (X) (2))))
    print "x reuse 2 =", (TWICE (1))
    
    T = Fun()
    (SET (T) (LAMBDA (X) (TWICE (X))))
    print "\\ x reuse 8 =", (T (4))
    

    F = Fun(None)
    (SET (F) (LAMBDA (X) 
        (IF (EQ (X) (1))
            (1)
            (MUL (X) (F (SUB (X) (1)))))))

    print "fact 24 =", (F (4))
