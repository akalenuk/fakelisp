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

MAX_REC = 42

common_id = 0 
fun_map = {}
really = True

class Fun:
	def __init__(self, fun, chain = [], co_id = None):
		if co_id != None:
			self.co_id = co_id
		else:
			global common_id
			common_id += 1
			self.co_id = common_id
			fun_map[self.co_id] = fun		
		self.chain = chain
	def __call__(self, a):
		return Fun(None, self.chain + [a], self.co_id)
	def __repr__(self):
		return str(s(self))
		
class Var:
	def __init__(self, val = None):
		self.chain = [self]
		self.val = val
	def __call__(self, a):
		if hasattr(self.val, '__call__'):
			return self.val(a)
		self.chain += [a]
		return self
	def __repr__(self):
		return str(self.val)		
	
rc = 0
class LAMBDA:
	def __init__(self, args):
		self.args = [a for a in args.chain]
		for arg in args.chain:
			arg.chain = [arg]
	def __call__(self, body):
		def l(args, body, x):
			old_x = [arg.val for arg in args]
			for arg, xi in zip(args, x):
				arg.val = s(xi)
			
			global rc
			rc += 1
			if rc < MAX_REC:
				r = s(body)
			else:
				r = 0
			rc -= 1

			for arg, old_xi in zip(args, old_x):
				arg.val = old_xi
			return r
		return Fun(lambda *x: l(self.args, body, x))

	
class SET:
	def __init__(self, var):
		self.var = var
	def __call__(self, value):
		if isinstance(self.var, Var):
			self.var.val = value 
		elif isinstance(self.var, Fun):
			fun_map[self.var.co_id] = fun_map[value.co_id]
		return None

def s(x):
	if isinstance(x, list):
		return [s(xi) for xi in x]
	if isinstance(x, Fun):
		return fun_map[x.co_id]( *s(x.chain) )
	if isinstance(x, Var):
		return x.val
	else:
		return x

		
ADD = Fun(lambda *x: sum(s(x)))
EQ = Fun(lambda a, b: a == b)
SUB = Fun(lambda *x: (s(x[0]) - s(x[1])))
MUL = Fun(lambda *x: reduce(lambda a,b: s(a)*s(b), x))

QUOTE = Fun(lambda *x: list(s(x)))
BEGIN = Fun(lambda *x: (x[-1]))
IF = Fun(lambda c, r1, r2: r1 if c else r2)

X = Var()
Y = Var()
Z = Var()

G = Fun(None)
F = Fun(None)

if __name__ == '__main__':
	PLUS = Var()
	TWICE = Var()
		
	print "subsub 3 =", (SUB (4) (SUB (3) (2)))
		
	(SET (Z) (3))
	print "set Z 3 =", (Z)
		
	print "begin 5 =", (BEGIN 
		(SET (X) (2)) 
		(SET (Y) (3)) 
		(ADD (X) (Y)))
		
	print "if 0 =", (IF (EQ (X) (3)) (1) (0))
		
	print "quote [1,7] =", (QUOTE (1) (ADD (4) (SUB (6) (3))) )
	
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
	
	T = Var()
	(SET (T) (LAMBDA (X) (TWICE (X))))
	print "\\ x reuse 8 =", (T (4))

	
	F = Fun(None)
	(SET (F) (LAMBDA (X) 
		(IF (EQ (X) (1))
			(1)
			(MUL (X) (F (SUB (X) (1)))))))

	print "fact 24 =", (F (4))
