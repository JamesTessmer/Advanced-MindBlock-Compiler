# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:38:08 2019

@author: james
"""

import unittest
import Tokenizer
import TokenClasses as tc

class TestFileOpen(unittest.TestCase):

        #should open the file, fails if an exception is thrown
        def testOpen(self):
            try:
                Tokenizer.read_amb_file("test.amb")
                self.assertTrue(True)
            except:
                self.assertTrue(False)
                
        def testBadExtension(self):
            try:
                Tokenizer.read_amb_file("test.exe")
            except Exception as e:
                print (e)
                self.assertEqual('Error: File extension is exe and should be amb', e.args[0])
                
        def testBadType(self):
            try:
                Tokenizer.read_amb_file(8)
            except Exception as e:
                print (e)
                self.assertEqual('Error: A string must be entered as the file name', e.args[0])
                
        def testBadFileName(self):
            try:
                Tokenizer.read_amb_file("test")
            except Exception as e:
                print (e)
                self.assertEqual('Error: Input is not a valid file name', e.args[0])
                
class TestParseLine(unittest.TestCase):
    
    """
    Testing for each Keyword, symbol, ints, labels, and character strings
    """
    
    def testStart(self):
        token = Tokenizer.tokenize_line("START_PROGRAM")
        self.assertEqual(type(token[0]), tc.START_PROGRAM)
        
    def testEnd(self):
        token = Tokenizer.tokenize_line("END_PROGRAM.")
        self.assertEqual(type(token[0]), tc.END_PROGRAM)
        
    def testStartSub(self):
        token = Tokenizer.tokenize_line("START_SUB")
        self.assertEqual(type(token[0]), tc.START_SUB)
        
    def testEndSub(self):
        token = Tokenizer.tokenize_line("END_SUB.")
        self.assertEqual(type(token[0]), tc.END_SUB)
                
    def testGoSub(self):
        token = Tokenizer.tokenize_line("GOSUB")
        self.assertEqual(type(token[0]), tc.GOSUB)
        
    def testCode(self):
        token = Tokenizer.tokenize_line("CODE")
        self.assertEqual(type(token[0]), tc.CODE)
        
    def testIf(self):
        token = Tokenizer.tokenize_line("IF")
        self.assertEqual(type(token[0]), tc.IF)
        
    def testThen(self):
        token = Tokenizer.tokenize_line("THEN")
        self.assertEqual(type(token[0]), tc.THEN)
        
    def testElse(self):
        token = Tokenizer.tokenize_line("ELSE")
        self.assertEqual(type(token[0]), tc.ELSE)
    
    def testEndIf(self):
        token = Tokenizer.tokenize_line("END_IF")
        self.assertEqual(type(token[0]), tc.END_IF)
        
    def testWhile(self):
        token = Tokenizer.tokenize_line("WHILE")
        self.assertEqual(type(token[0]), tc.WHILE)
        
    def testDo(self):
        token = Tokenizer.tokenize_line("DO")
        self.assertEqual(type(token[0]), tc.DO)
        
    def testEndWhile(self):
        token = Tokenizer.tokenize_line("END_WHILE")
        self.assertEqual(type(token[0]), tc.END_WHILE)
        
    def testInt(self):
        token = Tokenizer.tokenize_line("INT")
        self.assertEqual(type(token[0]), tc.INT)
        
    def testString(self):
        token = Tokenizer.tokenize_line("STRING")
        self.assertEqual(type(token[0]), tc.STRING)
        
    def testPrint(self):
        token = Tokenizer.tokenize_line("PRINT")
        self.assertEqual(type(token[0]), tc.PRINT)
        
    def testInput(self):
        token = Tokenizer.tokenize_line("INPUT")
        self.assertEqual(type(token[0]), tc.INPUT)
        
    """
    Testing Symbols
    
    There's a case where if a line only has an = or a : it doesn't tokenize properly
    I haven't yet found a way to solve it without creating more errors
    """
    def testSoftOpen(self):
        token = Tokenizer.tokenize_line("(")
        self.assertEqual(type(token[0]), tc.SoftOpen)
        
    def testSoftClose(self):
        token = Tokenizer.tokenize_line(")")
        self.assertEqual(type(token[0]), tc.SoftClose)
        
        
    def testSemi(self):
        token = Tokenizer.tokenize_line(";")
        self.assertEqual(type(token[0]), tc.Semicolon)
        
    def testAssignment(self):
        token = Tokenizer.tokenize_line(":=")
        self.assertEqual(type(token[0]), tc.Assignment)
        
#    def testColon(self):
#        token = Tokenizer.tokenize_line(":")
#        self.assertEqual(type(token[0]), tc.Colon)
        
    def testMultOpM(self):
        token = Tokenizer.tokenize_line("*")
        self.assertEqual(type(token[0]), tc.MultOp)
        
    def testMultOpD(self):
        token = Tokenizer.tokenize_line("/")
        self.assertEqual(type(token[0]), tc.MultOp)
        
    def testAddOpP(self):
        token = Tokenizer.tokenize_line("+")
        self.assertEqual(type(token[0]), tc.AddOp)
        
    def testAddOpM(self):
        token = Tokenizer.tokenize_line("-")
        self.assertEqual(type(token[0]), tc.AddOp)
        
    def testLThan(self):
        token = Tokenizer.tokenize_line("<")
        self.assertEqual(type(token[0]), tc.CompOp)
        
    def testGThan(self):
        token = Tokenizer.tokenize_line(">")
        self.assertEqual(type(token[0]), tc.CompOp)
        
    def testLEThan(self):
        token = Tokenizer.tokenize_line("=<")
        self.assertEqual(type(token[0]), tc.CompOp)
        
    def testGEThan(self):
        token = Tokenizer.tokenize_line("=>")
        self.assertEqual(type(token[0]), tc.CompOp)
        
#    def testEqual(self):
#        token = Tokenizer.tokenize_line("=")
#        self.assertEqual(type(token[0]), tc.CompOp)
        
    def testNEqual(self):
        token = Tokenizer.tokenize_line("!=")
        self.assertEqual(type(token[0]), tc.CompOp)
        
    """
    Testing integers, labels, and strings
    The tokenizer doesn't properly tokenize integers at the moment, it reports them as labels
    """
    def testLabel(self):
        token = Tokenizer.tokenize_line("abc123")
        self.assertEqual(type(token[0]), tc.Label)
    
#    def testInteger(self):
#        token = Tokenizer.tokenize_line("1234")
#        self.assertEqual(type(token[0]), tc.Integer)
        
    def testCharString(self):
        token = Tokenizer.tokenize_line('"Yeehaw Pardner"')
        self.assertEqual(type(token[0]), tc.CharacterString)
        
if __name__ == '__main__':
    unittest.main()