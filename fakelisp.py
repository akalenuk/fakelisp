#!/usr/bin/python

# W A R N I N G ! This is not an actual Lisp.

class Fun:
    def __init__(self, fun_or_fun_stack = None, arity = 0, chain = []):
        if isinstance(fun_or_fun_stack, list):
            self.fun_stack = fun_or_fun_stack   # in recursive Fakelisp LAMBDAs you have to pass the whole fun_stack
        else:
            self.fun_stack = [fun_or_fun_stack] # but it is cleaner to declare Fun by simple Pythons lambda,
        self.chain = chain
        self.arity = arity
    def __call__(self, next_arg): # instead of execution, it builds a chain of arguments
        return Fun(self.fun_stack, self.arity, self.chain + [next_arg] )
    def __repr__(self):
        return str(s(self))
    def push_fun(self, val):
        self.fun_stack += [None]   # this is a trick to reuse assigning function
        a(self, val)               #
    def pop_fun(self):
        self.fun_stack = self.fun_stack[:-1]

        
def l(args, body, x):   # fakelisp lambda body
    map (lambda (arg, val): arg.push_fun( val ), zip(args, s(x)))   # pushing new lexical context
    r = s(body)
    map (lambda arg: arg.pop_fun(), args)   # poping old lexical context
    return r
    
def a(var, value):  # assigning a fakelisp value
    if isinstance(value, Fun):
        var.fun_stack[-1] = value.fun_stack[-1] # reassigning a Fun object (LAMBDA)
        var.chain = [link for link in value.chain]
        var.arity = value.arity
    else:
        var.fun_stack[-1] = lambda *x: value    # reassigning value. Values are also Fun objects
        var.chain = []
        var.arity = 0

def s(x):   #   evaluating s-expression
    if isinstance(x, list):
        return [s(xi) for xi in x]
    if isinstance(x, Fun):
	if x.arity <= len(x.chain):
            return s(x.fun_stack[-1]( *(x.chain) )) # normal case
        else:
            return Fun(lambda y: x(y), x.arity - len(x.chain), x.chain) # when evaluation returns a Fun, like in LAMBDA assignment
    return x


LAMBDA = lambda args: lambda body: Fun(lambda *x: l([args] + args.chain, body, list(x)), len(args.chain)+1)
SET = Fun(lambda var, value: a(var, value))
IF = Fun(lambda c, r1, r2: r1 if s(c) else r2)
    
LIST = Fun(lambda *x: s(list(x)))
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
