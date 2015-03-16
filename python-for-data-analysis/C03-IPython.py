# -*- coding: utf-8 -*-

# Chapter 2 of python for data analysis
"""
Created on Fri Feb 20 15:12:18 2015

@author: mwakeman
"""

# import libraries using import
import json
import numpy as np

# assign random values using np.random.randn()
data = {i : np.random.randn() for i in range(7)}

# always try to use the iPython console
# show results by naming the object
data
# print isn't as useful
print data
# python is 0-based indexing

# assignments using equals
an_apple = 27
an_example = 42

# uses auto-completion
an_

b = [1, 2, 3]

# structure using ?
# b?

# defining a function
def add_numbers(a, b):
    """
    Add two numbers together
    
    Returns
    -------
    the_sum : type of arguments
    """
    return a + b

# Show a function's source code in the console
??add_numbers

# can use ? to find all functions like a wildcard
np.*load*?

# %run executes an entire file as a python program inside the environment of 
## your IPython session
# runs in an empty namespace
## the behavior should be identical to running the program on the command line.
## all variables in the file (imports, functions, and globals) will then be 
## accessible in the IPython shell
# %run - i to use all the variables already defined in the IPython namespace

## Ctrl-C causes a KeyboardInterrupt to be raised - stopping the Python 
## programs (assuming control is at the interpreter already)

# exceptions and Tracebacks
## IPython prints a full call stack trace with a few lines of context around 
## the position at each point in the stack
## control the amount of context using the %xmode magic command:
### minimal - same as the standard python interpreter
### verbose - inlines function argument values and more
## step into the stack using %debug or %pdb magics after an error has occurred

# magic commands
## facilitate common tasks and enable you to easily control the behavior
## any command prefixed by the percent symbol %
### check the execution time of a statement using %timeit magic function

a = np.random.randn(100, 100)

%timeit np.dot(a, a)

# they all have additional options, which can be viewed using the ? operator

## can be used by default without the percent sign, as long as no variable
## is defined with the same name
## called "automagic" - change status with %automatic

# list all the automagic commands
%quickref
%magic

# open a special prompt to manually paste Python code to be executed
%cpaste
# clear/delete all variables & names defined in the interactive namespace
%reset

# execute a statement with cProfile and report the profiler output
%prun

# display the list of variables defined in the interactive namespace, with
## varying levels of invormation / verbosity
%prun %who
%prun %who_ls
%prun %whos

# delete a variable and attempt to clear any references to the object in the
## IPython internals
%xdel

# PyQT console combines terminal-only apps with a rich text widget
## (embedded images, multiline editing, syntax highlighting)

?%gui