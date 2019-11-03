# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:49:16 2019

A tokenizer for use with the Advanced MindBlock parser and compiler. Takes in
a file with a .amb extension and returns a list of objects where the object is 
type of the token and *may* contain a value depending on what the token is

@author: james
"""


"""
Function to open the AMB file and read in the text. Returns a list where each
index is a line of the file
"""

import TokenClasses
import re


def read_amb_file(file_name):
    #checking to make sure the file is valid

    #if something other than a string is entered
    if type(file_name) is not str:
        raise Exception("Error: A string must be entered as the file name")
    extension = file_name.split(".");
    #there should be 2 indices in extension - one for the name of the file and
    #another for the extension
    #if there are not 2 indices then the string is invalid, or if index 1 is not AMB the file is invalid
    
    if len(extension) == 1:
        raise Exception("Error: Input is not a valid file name")
        
    if extension[1] != "amb":
        raise Exception("Error: File extension is " + extension[1] + " and should be amb")
    
    """
    At this point the file should be a valid amb file, so we can open it and pull the text
    """
    line_list = []
    with open(file_name, "r") as file:
        line_list = file.readlines();
        
    #Each index of line_list should now contain one line from the file as a string, in order
    return line_list

"""
Takes in a line of text from an AMB file and tokenizes it, returning a list of tokens, in order
Uses classes for each type of token
"""
def tokenize_line(current_line):
    token_list = []
    text_list = current_line.split()
    isCharString = False # used for when the current words are part of a character string
    charString = ""
    
    current_symbol = ''
    isLabel = False
    currentLabel = ""
    isInt = False
    currentInt = ""

   
    #this gives us a list separated by whiespace, each index should be a separate token
    #apart from character strings, but there's a case for that
    
    #iterate through each index and assign a token identity
    for word in text_list:
        #covering the case that the token is a keyword
        if isCharString == False:
            tempWord = re.sub(r'\W+', '', word)
            print(word)
            token = isKeyword(tempWord)
            token2 = isKeyword(tempWord + ".")
            if token is not None:
                token_list.append(token)
            elif token2 is not None:
                token_list.append(token2)
                
        """
        Since this function splits on white space there can be cases where an
        index of text_list could be a combination of symbols and symbol collections
        
        This is solved by indexing the 'word' and detecting non-alphanumeric characters
        
        In the case of character strings if a " is detected then all characters are concatenated until
        another quotation mark is detected
        """
       
        #keeping spaces where they should be in charString
        if isCharString == True:
            charString = charString + " "
        
        
        for index in range(0, len(word)):
            keywords = ["START_PROGRAM","END_PROGRAM.","START_SUB","END_SUB.","GOSUB","CODE","IF","THEN","ELSE","END_IF","WHILE","DO","END_WHILE","INT","STRING","PRINT","INPUT"]

            character = word[index]
            if character == None:
                break
            
            """
            If there is a " then switch the bool so that all characters from this point
            are put into a string. when a second " is detected it returns the string as a charString token
            and continues regular tokenization
            """
            if character == '"':
                if isCharString == False:
                    isCharString = True
                    continue
                else:
                    isCharString = False
                    token = TokenClasses.CharacterString(charString)
                    token_list.append(token)
                    charString = ""
                    continue
                   
                
            if isCharString == True:
                charString = charString + character
                continue
                
                
            #at this point it should be tokenizing for normal other symbols, labels, or integers
            
            """
            Case for labels and integers
            If a digit is encountered before an alpha character then it must be an int and not a label
            """
            if character.isnumeric() == True:
                
                #addressing case from symbol
                if len(current_symbol) == 1:
                    token = isSymbol(current_symbol)
                    if token is not None:
                        token_list.append(token)
                        current_symbol = ''
                        
                    
                if isLabel == True:
                    currentLabel = currentLabel + character
                else:
                    isInt = True
                    
                if isInt == True:
                    currentInt = currentInt + character
                    
            elif isInt == True: #if isInt is true and the current character is not a number
                token = TokenClasses.Integer(currentInt)
                token_list.append(token)
                currentInt = ""
                isInt = False
                
                
                
            if character.isalpha() == True:
                 #addressing case from symbol
                if len(current_symbol) == 1:
                   token = isSymbol(current_symbol)
                   token_list.append(token)
                   current_symbol = ''
                   
                isLabel = True
                currentLabel = currentLabel + character
            elif character.isalnum() == False and isLabel == True:
                if currentLabel in keywords or currentLabel + "_" in word or "_" + currentLabel in word:
                    isLabel = False
                    currentLabel = ""
                
                else:
                    isLabel = False
                    token = TokenClasses.Label(currentLabel)
                    token_list.append(token)
                    currentLabel = ""
               
 
                
                
                
           
            
            
            """
            case for symbols
            Some are 2 characters long which is managed by a 'current symbol' string
            """
            
                
            if character.isalnum() == False: #if it's not a letter or number
                
                current_symbol = current_symbol + character
                if len(current_symbol) > 2:  
                    #if a symbol is 3 or more characters long then it is not part of the language
                    raise Exception("Bad symbol")
                
                token = isSymbol(current_symbol)
                if token is None:
                    continue
                if token is None and len(current_symbol) == 2:
                    raise Exception("Invalid symbol characters")
                #these characters can yield symbols of length 1 or 2, covered next
                
                if token.value == '=' or type(token) == TokenClasses.Colon:
                    if len(current_symbol) == 2:
                        token_list.append(token)
                        current_symbol = ''

                else:
                    if type(token) == TokenClasses.HardOpen and type(token_list[-1]) != TokenClasses.Label :
                        prevTok = token_list[-1]
                        token_list[-1] = token
                        token_list.append(prevTok)
                        current_symbol = ""
                        
                    else:
                       token_list.append(token)
                       current_symbol = ''
                
                    
            """
            Checking to see if we're at the end of a word and a token needs to be added
            compares
            """
            if index == len(word) -1:
                #print(current_symbol)
                if len(token_list) == 0 or (isLabel == True and type(token_list[-1]) is not TokenClasses.Label) and currentLabel not in keywords:
                    if (currentLabel + "_") not in word and ("_" + currentLabel) not in word:
                        token = TokenClasses.Label(currentLabel)
                        token_list.append(token)
                        isLabel = False
                        currentLabel = ''
                if len(token_list) == 0 or(isInt == True and token_list[-1].value != currentInt):
                    token = TokenClasses.Integer(currentInt)
                    token_list.append(token)
                    isInt = False
                    currentInt = ''
                if len(token_list) == 0 or(current_symbol != "" and token_list[-1].value != isSymbol(current_symbol)):
                    #print(current_symbol)
                    token = isSymbol(current_symbol)
                    current_symbol = ''
                    token_list.append(token)
                
                currentLabel = ''
                isLabel = False
                
            
                
    return token_list
    
        
       
       
    
"""
Functions to help tokenize lines
"""

"""
Checks to see if the current word list is a Keyword. Keywords are all capitalized
so this checks for that. Returns the keyword if it is one or None if not
"""
def isKeyword(text):
    keyword_dict = {"START_PROGRAM": TokenClasses.START_PROGRAM(),
                    "END_PROGRAM.": TokenClasses.END_PROGRAM(),
                    "START_SUB": TokenClasses.START_SUB(),
                    "END_SUB.": TokenClasses.END_SUB(),
                    "GOSUB": TokenClasses.GOSUB(),
                    "CODE": TokenClasses.CODE(),
                    "IF": TokenClasses.IF(),
                    "THEN": TokenClasses.THEN(),
                    "ELSE": TokenClasses.ELSE(),
                    "END_IF": TokenClasses.END_IF(),
                    "WHILE": TokenClasses.WHILE(),
                    "DO": TokenClasses.DO(),
                    "END_WHILE": TokenClasses.END_WHILE(),
                    "INT": TokenClasses.INT(),
                    "STRING": TokenClasses.STRING(),
                    "PRINT": TokenClasses.PRINT(),
                    "INPUT": TokenClasses.INPUT()}
    if text.isupper():
        #if it is a keyword
        if text in keyword_dict.keys():
            return keyword_dict[text]

    return None;

"""
Checks to see if the current word is a symbol using a dictionary
"""
def isSymbol(text):
    symbol_dict = {"(": TokenClasses.SoftOpen(),
                   ")": TokenClasses.SoftClose(),
                   '"': TokenClasses.Quote(),
                   ";": TokenClasses.Semicolon(),
                   ":=": TokenClasses.Assignment(),
                   ":": TokenClasses.Colon(),
                   "*": TokenClasses.MultOp("*"),
                   "/": TokenClasses.MultOp("/"),
                   "+": TokenClasses.AddOp("+"),
                   "-": TokenClasses.AddOp("-"),
                   "<": TokenClasses.CompOp("<"),
                   ">": TokenClasses.CompOp(">"),
                   "=<": TokenClasses.CompOp("=<"),
                   "=>": TokenClasses.CompOp("=>"),
                   "=": TokenClasses.CompOp("="),
                   "!=": TokenClasses.CompOp("!="),
                   "[": TokenClasses.HardOpen(),
                   "]": TokenClasses.HardClose()
                   }
    if text in symbol_dict.keys():
        return symbol_dict[text]
    else:
        return None
    

"""
This function calls the above functions to create a list of tokens, and then returns in
"""

def tokenize_file(filename):
    list_of_tokens = list()
    lines_of_code = read_amb_file(filename)
    
    for line in lines_of_code:
        line_tokens = tokenize_line(line)
        for token in line_tokens:
            list_of_tokens.append(token)

    return list_of_tokens
    

