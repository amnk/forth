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
    if len(args)<>1:
            sys.exit(f_error.format(f="PUT"))
    f_stack.append(_value(args[0]))

def f_add(f_stack, args=None):
    """
    Returns a summary of f_stack[-1] and f_stack[-2]
    """
    if len(f_stack)<2:
        sys.exit(s_error)
    try:
        print(f_stack[-1] + f_stack[-2])
    except TypeError:
        sys.exit(f_error.format(f="ADD"))

def f_sub(f_stack, args=None):
    """
    Substracts two last values in the f_stack (simple list).
    """
    if len(f_stack)<2:
         sys.exit(s_error)
    try:
        print(f_stack[-1] - f_stack[-2])
    except TypeError:
        sys.exit(f_error.format(f="SUB"))
    pass

def f_print(f_stack, args=None):
    """
    Accepts f_stack (simple list) and prints value in it
    """
    if len(f_stack)<1:
        sys.exit(s_error)
    print(f_stack[-1])

def f_pop(f_stack, args=None):
    """
    Accepts f_stack (simple list) and removed one value
    """
    if len(f_stack)<1:
        sys.exit(s_error)
    f_stack.pop()

def run_line(s, v_dict):
    s.strip()
    line=s.split()
    
    if (line[0] not in def_commands.keys()):
        sys.exit("Bad command syntax in \n\t{0}".format(s))
    command = line[0]
    arguments = line[1:]
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


