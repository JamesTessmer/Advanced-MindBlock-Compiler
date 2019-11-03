# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:14:05 2019

@author: james
"""

import Tokenizer as tok
import ParseTreeGenerator as PTG

def ambToC(filename):
    tokens = tok.tokenize_file(filename)
    true_tokens = [i for i in tokens if i] 

    for token in true_tokens:
        print(type(token))
        if token is not None:
            print(token.value)  
    

    parseTree = PTG.parse(true_tokens)
    parseTree.printTree()
    

ambToC("test.amb")