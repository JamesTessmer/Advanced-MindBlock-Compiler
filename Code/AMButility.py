# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:57:46 2019

@author: james
"""


"""
Takes a list of parsed terms and a dictionary of labels and their types to create a string file
Utilizes helper functions for cases such as printing and taking input
"""
import TokenClasses as tc
def parseListToCString(c_list, label_type, func_list):
    text = ""
    inMain = False
    bracketCt = 0
    i = 0
    inPrint = False
    inScan = False
    inGS = False
    for i in range(0, len(c_list)):
        """
        Handling specific cases
        """
        
        word = c_list[i]
        
        if c_list[i-1] == "char ":
            text += word + "[50]"
            continue
        
        if inPrint:
            if word == ';':
                inPrint = False
                continue
            else:
                continue
            
        if inScan:
            if word == ';':
                inScan = False
                continue
            else:
                continue
            
        if inGS:
            if word == ';':
                inGS = False
                continue
            else:
                continue
            
        #checking for input
        if i+2 < len(c_list) and c_list[i+2] == "scanf":
            inScan = True
            scanStatement = scanInC(c_list, i, label_type)
            text += scanStatement
            continue
        
        #if a semicolon is encountered then that must be the last character, so tack that plus a newline on and then continue
        if word == ';':
            text += word + "\n"
            continue
        
        #only occurs once at the start of the program, and it's the only thing in the line
        if word == "#include <stdio.h>":
            text += word + "\n"
            
            #we will also declare functions here
            for func_name in func_list:
                text += func_name + "(); \n"
            
            continue
        
        if word == '':
            continue
        
        if c_list[i-1] == "void ":
            continue
        
        #checks to see if the main is the method, by checking on 'void' to see if the next word is main.
        #this is also why it skips the next word in the list which should be main
        if(checkIfMain(c_list, i)):
            text += "int main(int argc, char * argv[])"
            inMain = True
            continue
        
        if word == "{":
            text += word + "\n"
            bracketCt +=1
            continue
        
        if word == "}":
            bracketCt -= 1
            if inMain and bracketCt == 0:
                inMain = False
                text += "return 0; \n"
            text+= word + "\n"
            continue
        
        #checking if a word is a function name
        if word == "void ":
            text += "void " + c_list[i+1] + "()"
            continue
            
        if word == "printf":
            inPrint = True
            printStatment = printInC(c_list, i, label_type)
            text += printStatment
            continue
        
        if word == "GOSUB":
            inGS = True
            text += c_list[i+1] + "(); \n"
            continue
        
        #case for if and when statements
        if word == "){":
            bracketCt += 1
            text += word + "\n"
            continue
            
        text += word
    return text

#Detects if a method name is the main or not
def checkIfMain(c_list, index):
    word = c_list[index]
    if word != 'void ':
        return False
    elif (c_list[index+1] != 'main'):
        return False
    else: 
        return True
        
        
def printInC(c_list, index, label_type):
    printStr = 'printf("'
    variables = [] # hold the variables for when we plug them back in
    index += 2 #getting the index past the printf and (
    #stop at closing parenthesis so that we can add the labels back in to substitute form %d and %c
    while c_list[index] != ')':
        word = c_list[index]
        #if the item is a label
        if word in label_type.keys():
            variables.append(word)
            #adding %d or %c depending on var type
            print(label_type[word])
            if label_type[word] == "INT":
                printStr += "%d "
            else:
                printStr += "%s "
                
        else:
            printStr += word + " "
        index += 1
    
    printStr +=  ' \\n"'
    
    for label in variables:
        printStr += "," + label
    printStr += "); \n"
    return printStr
        
def scanInC(c_list, index, label_type):
    printStr = "scanf("
    
    word = c_list[index]
    #adding %d or %c depending on var type
    print(label_type[word])
    if label_type[word] == "INT":
        printStr += '"%d'
    else:
        printStr += '"%s' 
        
    printStr += '", &' + word + "); \n"
    return printStr
    