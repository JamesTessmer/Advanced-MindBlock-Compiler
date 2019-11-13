# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:52:41 2019

A list of token classes to be used with the tokenizer. Each class is a subclass of
the token class, and may contain a value. These classes are used to identify the
tokens for the use with the parser.

Each node has a dump_node function that will return the node in C syntax for conversion into a C file
@author: james
"""


class Token:
    def __init__(self):
        self.value = None

"""
Keywords
"""

class START_PROGRAM(Token):
    def __init__(self):
        super()  
        self.value = None
        
    #putting include stdio H here because it's needed for many functions such as printing
    def dump_node(self): 
        return "#include <stdio.h>" 

        
class END_PROGRAM(Token):
    def __init__(self):
        super()
        self.value = None
        
    def dump_node(self): 
        return ""

class START_SUB(Token):
    def __init__(self):
        super()
        self.value = None
        
    #all funcs based off this language have no return type
    def dump_node(self): 
        return "void "

class END_SUB(Token):
    def __init__(self):
        super()
        self.value = None
        
    #The closing bracket for the func
    def dump_node(self): 
        return "}"
        
class GOSUB(Token):
    def __init__(self):
        super()
        self.value = None
        
    def dump_node(self): 
        return "GOSUB"

class CODE(Token):
    def __init__(self):
        super()
        self.value = None
        
    def dump_node(self): 
        return ""

class IF(Token):
    def __init__(self):
        super()
        self.value = None
        
    def dump_node(self): 
        return "if("

class THEN(Token):
    def __init__(self):
        super()
        self.value = None
    
    #The closing part of an if statement
    def dump_node(self): 
        return "){"

class ELSE(Token):
    def __init__(self):
        super()
        self.value = None
        
    def dump_node(self): 
        return "}else{"

class END_IF(Token):
    def __init__(self):
        super()
        self.value = None
        
    #the closing bracket of the else
    def dump_node(self): 
        return "}"

class WHILE(Token):
    def __init__(self):
        super()
        self.value = None
        
    def dump_node(self): 
        return "while("

class DO(Token):
    def __init__(self):
        super()
        self.value = None
    
    #The closing bracket of the while condition
    def dump_node(self): 
        return "){"

class END_WHILE(Token):
    def __init__(self):
        super()
        self.value = None
        
    #closing bracket of while statement
    def dump_node(self): 
        return "}"

class INT(Token):
    def __init__(self):
        super()
        self.value = None
        
    def dump_node(self): 
        return "int "

class STRING(Token):
    def __init__(self):
        super()
        self.value = None
        
    def dump_node(self): 
        return "char "

class PRINT(Token):
    def __init__(self):
        super()
        self.value = None
        
    def dump_node(self): 
        return "printf"

class INPUT(Token):
    def __init__(self):
        super()
        self.value = None

    def dump_node(self): 
        return "scanf"
"""
Symbols, ops in these are strings to determine what the operation stored in that token is
"""

class SoftOpen(Token):
    def __init__(self):
        super()
        self.value = None
        
    def dump_node(self): 
        return "("
    
class SoftClose(Token):
    def __init__(self):
        super()
        self.value = None
        
    def dump_node(self): 
        return ")"
        
class Quote(Token):
    def __init__(self):
        super()
        self.value = None
        
    def dump_node(self): 
        return '"'
        
class Semicolon(Token):
    def __init__(self):
        super()
        self.value = None
        
    def dump_node(self): 
        return ";"
    
class Assignment(Token):
    def __init__(self):
        super()
        self.value = None
        
    def dump_node(self): 
        return "="
        
class Colon(Token):
    def __init__(self):
        super()
        self.value = None
    #used for the opening bracket of functions
    def dump_node(self): 
        return "{"
        
class MultOp(Token):
    def __init__(self, op = None):
        super()
        self.value = op
        
    def dump_node(self): 
        return str(self.value)
        
class AddOp(Token):
    def __init__(self, op = None):
        super()
        self.value = op
        
    def dump_node(self): 
        return str(self.value)
        
class CompOp(Token):
    def __init__(self, op = None):
        super()
        self.value = op
        
    def dump_node(self): 
        if self.value == "=":
            return "=="
        return str(self.value)
        
class HardOpen(Token):
    def __init__(self):
        super()
        self.value = None
        
    def dump_node(self): 
        return "["
        
class HardClose(Token):
    def __init__(self):
        super()
        self.value = None
        
    def dump_node(self): 
        return "]"
        
"""
Symbol Collections
"""

class Integer(Token):
    def __init__(self, value=None):
        super()
        self.value = value
        
    def dump_node(self): 
        return str(self.value)
        
class Label(Token):
    def __init__(self, value=None):
        super()
        self.value = value
        
    def dump_node(self): 
        return self.value
        
class CharacterString(Token):
    def __init__(self, value=None):
        super()
        self.value = value
        
    def dump_node(self): 
        return self.value

"""
Print func for each subclass to print it as it would appear in C
"""