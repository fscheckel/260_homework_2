Python 2.7.16 (default, Jan 26 2020, 23:50:38) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.31)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
import numpy as np
>>> A = 58
>>> Z = 28
>>> 
>>> a1 = 15.8
>>> a2 = 18.3
>>> a3 = 0.714
>>> a4 = 23.2
>>> 
>>> if A % 2 != 0:
	a5 = 0

	
>>> if A % 2 == 0 and Z % 2 == 0:
	a5 = 12.0

	
>>> if A % 2 == 0 and Z != 0:
	a5 = -12.0
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> 
>>> 
>>> B = (a1*A)-(a2*A**(2/3))-(a3*(Z**(2)/A**(1/3)))-(a4*((A-(2*Z))**(2)/A))+(a5/A**(1/2))
>>> print("total binding energy")
total binding energy
>>> print(B)
350.324
>>> T_B_E = B / A
>>> print("binding energy")
binding energy
>>> print(B)
350.324
>>> T_B_E = B / A
>>> print("total binding energy")
total binding energy
>>> print(T_B_E)
6.04006896552
>>> (A, A=Z)
SyntaxError: invalid syntax
>>> #ahhhhhhhhhhh
>>> for A range(Z*1,Z*3):
	
SyntaxError: invalid syntax
>>> for A in range(Z*1, Z*2):
	max(list)
	A[]
	
SyntaxError: invalid syntax
>>> print("maximum binding energy")
maximum binding energy
>>> print(list)
<type 'list'>
>>> def binding_energy_per_nucleon(Z):
	max = 0
	maxA = 0.0

	
>>> def binding_energy_per_nucleon(Z):
	max = 0
	maxA = 0.0

	
>>>     for A in range(Z*1, Z*3):
	    
  File "<pyshell#49>", line 1
    for A in range(Z*1, Z*3):
    ^
IndentationError: unexpected indent
>>> for A in range(Z*1, Z*3):
	if max < T_B_E
	
SyntaxError: invalid syntax
>>> 
for A in range(Z*1, Z*3):
	if max < T_B_E:
		max = T_B_E
		maxA = A

		
>>> def max_binding_energy():
	maxZ = 0
	max = 0.0

	
>>> for Z in range(1,100):
	if max < maxA:
		max = maxA
		maxZ = Z

		

Traceback (most recent call last):
  File "<pyshell#64>", line 2, in <module>
    if max < maxA:
NameError: name 'maxA' is not defined
>>> 
