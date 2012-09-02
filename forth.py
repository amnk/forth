#!/usr/bin/env python

"""
Very basic and robust Forth interpreter.
See def_commands for full list of available commands
"""

import sys
import fileinput

f_error = "Operation error for {f} command. Exiting."
s_error = "Not enough elements in stack. Exiting"

def _value(value):
    """
    Function is used as a helper, to define if value is an int or a string
    """
    if not value.isdigit():
        return value
    elif value.isdigit() or value.lstrip('-').isdigit():
        return int(value) 

def f_put(f_stack, args):
    """
    Should be called with two values: stack and a value to append to the stack
    """
    f_stack.append(_value(args))

def f_add(f_stack, args=None):
    """
    Takes two values from f_stack (simple list), and puts their summary back
    """
    if len(f_stack)<2:
        sys.exit(s_error)
    try:
        summary = f_stack[-1] + f_stack[-2]
    except TypeError:
        sys.exit(f_error.format(f="ADD"))
    finally:
        f_pop(f_stack, n=2)
        f_put(f_stack, str(summary))

def f_sub(f_stack, args=None):
    """
    Takes two values from f_stack (simple list), and puts their difference back
    """
    if len(f_stack)<2:
         sys.exit(s_error)
    try:
        sub=f_stack[-1] - f_stack[-2]
    except TypeError:
        sys.exit(f_error.format(f="SUB"))
    finally:
        f_pop(f_stack, n=2)
        f_put(f_stack, str(sub))
        

def f_print(f_stack, args=None):
    """
    Accepts f_stack (simple list), pops a value from it and prints that value
    """
    if len(f_stack)<1:
        sys.exit(s_error)
    print(f_stack.pop())

def f_pop(f_stack, args=None, n=1):
    """
    Accepts f_stack (simple list), deletes n elements and returns them 
    """
    if len(f_stack)<n:
        sys.exit(s_error)
    elements = f_stack[-n::]
    del(f_stack[-n::])
    return elements

def run_line(s, v_dict):
    s.strip()
    line = s.split()
    check = len(line)
    if (line[0] not in def_commands.keys()) or (check>2):
        sys.exit("Bad command syntax in \n\t{0}".format(s))
    command = line[0]
    if check>1:
        arguments = line[1]
    else:
        arguments = None
 
    def_commands[command](f_stack=v_dict, args=arguments)


def_commands = {'put':f_put, 'add':f_add, 'sub':f_sub, 'print':f_print, 'pop':f_pop}
stack = []

if len(sys.argv)<>2:
    print("Input file was not specified!")
    print("Going to command line mode. Enter 'q' or 'quit' to exit.")
    while True:
        command = raw_input("Please enter a command: ")
        if command=='q' or command=='quit':
          sys.exit("Bye!")
        else:
          run_line(command, stack)


for line in open(sys.argv[1], 'r'):
    run_line(line, stack)
    print(stack)


