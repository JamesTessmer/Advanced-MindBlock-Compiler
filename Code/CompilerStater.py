# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:14:05 2019

@author: james
"""

import Tokenizer as tok
import ParseTreeGenerator as PTG
import TokenClasses as tc
import AMButility as util
import os

def ambToC(filename):
    tokens = tok.tokenize_file(filename)
    true_tokens = [i for i in tokens if i] 
    label_type = {}
    
    #creating a dictionary to correlate each label to its type, used for input and printing 
    #also creating a list of function names so that functions can be declared and called in any order
    for i in range (0,len(true_tokens)):
        token = true_tokens[i]
        if isinstance(token,tc.Label):
            if type(true_tokens[i-1]) == tc.INT:
                label_type[token.value] = "INT"
            else:
                label_type[token.value] = "STRING"
        
        #when CODE keyword is encountered no more variables are declared
        if type(token) == tc.CODE:
            break
    func_list = []
    for i in range(0,len(true_tokens)):
        token = true_tokens[i]
        if isinstance(token,tc.START_SUB):
            func_list.append(true_tokens[i+1].value)
            

    parseTree = PTG.parse(true_tokens)
    #parseTree.printTree()
    c_list = []
    parseTree.dumpTree(c_list)
    #print("printing list")
    #print(c_list)
    #print("Printing label_type dict")
    #print(label_type)
    returned_string = util.parseListToCString(c_list, label_type, func_list)
    print(returned_string)
    #code_parts = returned_string.split("\n")
    #print(code_parts)

    #writing to C file
    f = open("tempCfile.c", "w")
    f.write(returned_string)
    f.close()
    
    #running the file
    #print(os.system("gcc tempCfile.c -o tempCfile && ./ tempCfile.exe"))
    
ambToC("test.amb")