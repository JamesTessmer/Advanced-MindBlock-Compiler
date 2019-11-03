# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:52:41 2019

A list of token classes to be used with the tokenizer. Each class is a subclass of
the token class, and may contain a value. These classes are used to identify the
tokens for the use with the parser.

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

        
class END_PROGRAM(Token):
    def __init__(self):
        super()
        self.value = None

class START_SUB(Token):
    def __init__(self):
        super()
        self.value = None

class END_SUB(Token):
    def __init__(self):
        super()
        self.value = None
        
class GOSUB(Token):
    def __init__(self):
        super()
        self.value = None

class CODE(Token):
    def __init__(self):
        super()
        self.value = None

class IF(Token):
    def __init__(self):
        super()
        self.value = None

class THEN(Token):
    def __init__(self):
        super()
        self.value = None

class ELSE(Token):
    def __init__(self):
        super()
        self.value = None

class END_IF(Token):
    def __init__(self):
        super()
        self.value = None

class WHILE(Token):
    def __init__(self):
        super()
        self.value = None

class DO(Token):
    def __init__(self):
        super()
        self.value = None

class END_WHILE(Token):
    def __init__(self):
        super()
        self.value = None

class INT(Token):
    def __init__(self):
        super()
        self.value = None

class STRING(Token):
    def __init__(self):
        super()
        self.value = None

class PRINT(Token):
    def __init__(self):
        super()
        self.value = None

class INPUT(Token):
    def __init__(self):
        super()
        self.value = None

        
"""
Symbols, ops in these are strings to determine what the operation stored in that token is
"""

class SoftOpen(Token):
    def __init__(self):
        super()
        self.value = None
    
class SoftClose(Token):
    def __init__(self):
        super()
        self.value = None
        
class Quote(Token):
    def __init__(self):
        super()
        self.value = None
        
class Semicolon(Token):
    def __init__(self):
        super()
        self.value = None
    
class Assignment(Token):
    def __init__(self):
        super()
        self.value = None
        
class Colon(Token):
    def __init__(self):
        super()
        self.value = None
        
class MultOp(Token):
    def __init__(self, op = None):
        super()
        self.value = op
        
class AddOp(Token):
    def __init__(self, op = None):
        super()
        self.value = op
        
class CompOp(Token):
    def __init__(self, op = None):
        super()
        self.value = op
        
"""
Symbol Collections
"""

class Integer(Token):
    def __init__(self, value=None):
        super()
        self.value = value
        
class Label(Token):
    def __init__(self, value):
        super()
        self.value = value
        
class CharacterString(Token):
    def __init__(self, value):
        super()
        self.value = value
