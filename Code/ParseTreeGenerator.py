import TokenClasses as tc

"""
Defining grammar variables to be used in the parse tree
"""


class GrammarVariable:
    def __init__(self):
        self.value = None
        
class Program(GrammarVariable):
    def __init__(self):
        super().__init__()
        
class VariableList(GrammarVariable):
    def __init__(self):
        super().__init__()
        
class Variable(GrammarVariable):
    def __init__(self):
        super().__init__()
        
class ArrayVariable(GrammarVariable):
    def __init__(self):
        super().__init__()
        
class SubList(GrammarVariable):
    def __init__(self):
        super().__init__()

class CodeList(GrammarVariable):
    def __init__(self):
        super().__init__()
        
class CodeLine(GrammarVariable):
    def __init__(self):
        super().__init__()
    
class LineLabel(GrammarVariable):
    def __init__(self):
        super().__init__()      
        
class Assignment(GrammarVariable):
    def __init__(self):
        super().__init__()
        
class Condition(GrammarVariable):
    def __init__(self):
        super().__init__()
        
class ThenCodeList(GrammarVariable):
    def __init__(self):
        super().__init__()
        
class ElseCodeList(GrammarVariable):
    def __init__(self):
        super().__init__()

class Loop(GrammarVariable):
    def __init__(self):
        super().__init__()

class WhileCodeList(GrammarVariable):
    def __init__(self):
        super().__init__()

class ExpressionOrInput(GrammarVariable):
    def __init__(self):
        super().__init__()

class Expression(GrammarVariable):
    def __init__(self):
        super().__init__()

class TermTail(GrammarVariable):
    def __init__(self):
        super().__init__()

class Term(GrammarVariable):
    def __init__(self):
        super().__init__()


class FactorTail(GrammarVariable):
    def __init__(self):
        super().__init__()


class Factor(GrammarVariable):
    def __init__(self):
        super().__init__()
        
class PossibleArray(GrammarVariable):
    def __init__(self):
        super().__init__()




class ParseTreeNode:
    def __init__(self, tokenOrVariable, parent = None):
        self.parent = parent
        self.tokenOrVariable = tokenOrVariable
        self.children = []
        self.currentChild = 0

    def addChild(self,tokenOrVariable):
        if tokenOrVariable != None:
            child = ParseTreeNode(tokenOrVariable, self)
            self.children.append(child)

    def nextNode(self):
        if self.currentChild < len(self.children):
            rtnNode = self.children[self.currentChild]
            self.currentChild += 1
            return rtnNode
        else:
            self.currentChild = 0
            rtnNode = self.parent
            return rtnNode

    def printNode(self,level):
        print("At level "+str(level)+" my children are")
        for child in self.children:
            print("\t" + str(type(child.tokenOrVariable)))
            if isinstance(child.tokenOrVariable,tc.Token):
                print("\t" + str(child.tokenOrVariable.dump_node()))
        for child in self.children:
            child.printNode(level+1)
            
    def dumpNode(self, c_list):
        if isinstance(self.tokenOrVariable,tc.Token):
            c_list.append(self.tokenOrVariable.dump_node())
        for child in self.children:
            child.dumpNode(c_list)

class ParseTree:
    def __init__(self):
        self.head = ParseTreeNode(Program())

    def printTree(self):
        self.head.printNode(0)
        
    def dumpTree(self, c_list):
        return self.head.dumpNode(c_list)




def parse(tokens):
    #Constructing initial tree and testing cases that would cause failure before loop
    parseTree = ParseTree()
    currentNode = parseTree.head
    index = 0
    if len(tokens)<=0:
        return None
    
    
    
    """
    A very long while loop with one huge if else statement
    Every case uses the predict table and grammar rules to append children to the current node
    The current node is then updated to the next node
    """
    while index < len(tokens) and currentNode != None:
        
        #print("Printing current node tokenOrVar, then token type")
        #print(type(currentNode.tokenOrVariable))
        #print(type(tokens[index]))
        #if type(tokens[index]) is tc.Label:
            #print("value of label")
            #print(tokens[index].value)
        #print(currentNode.tokenOrVariable)
        
        if len(currentNode.children)==0:
            if type(currentNode.tokenOrVariable) is Program:
                if type(tokens[index]) is tc.START_PROGRAM:     
                    currentNode.addChild(tc.START_PROGRAM())
                    currentNode.addChild(VariableList())
                else: 
                    raise Exception("Error on Program")
            
            elif type(currentNode.tokenOrVariable) is VariableList:
                if type(tokens[index]) is tc.INT:
                    currentNode.addChild(Variable())
                    currentNode.addChild(VariableList())
                elif type(tokens[index]) is tc.STRING:
                    currentNode.addChild(Variable())
                    currentNode.addChild(VariableList())
                elif type(tokens[index]) is tc.HardOpen:
                    currentNode.addChild(Variable())
                    currentNode.addChild(VariableList())
                elif type(tokens[index]) is tc.CODE:
                    currentNode.addChild(tc.CODE())
                    currentNode.addChild(SubList())
                else:
                    raise Exception("Error on VariableList")
                    
            elif type(currentNode.tokenOrVariable) is Variable:
                if type(tokens[index]) is tc.INT:
                    currentNode.addChild(tc.INT())
                    currentNode.addChild(tc.Label())
                    currentNode.addChild(tc.Semicolon())
                elif type(tokens[index]) is tc.STRING:
                    currentNode.addChild(tc.STRING())
                    currentNode.addChild(tc.Label())
                    currentNode.addChild(tc.Semicolon())
                elif type(tokens[index]) is tc.HardOpen:
                    currentNode.addChild(tc.HardOpen())
                    currentNode.addChild(ArrayVariable())
                else:
                    raise Exception("Error on Variable")
            
            elif type(currentNode.tokenOrVariable) is ArrayVariable:
                if type(tokens[index]) is tc.INT:
                    currentNode.addChild(tc.INT())
                    currentNode.addChild(tc.HardClose())
                    currentNode.addChild(tc.Label())
                    currentNode.addChild(tc.HardOpen())
                    currentNode.addChild(tc.Integer())
                    currentNode.addChild(tc.HardClose())
                    currentNode.addChild(tc.Semicolon())
                elif type(tokens[index]) is tc.STRING:
                    currentNode.addChild(tc.STRING())
                    currentNode.addChild(tc.HardClose())
                    currentNode.addChild(tc.Label())
                    currentNode.addChild(tc.HardOpen())
                    currentNode.addChild(tc.Integer())
                    currentNode.addChild(tc.HardClose())
                    currentNode.addChild(tc.Semicolon())
                else:
                    raise Exception("Error on ArrayVariable")
                    
            elif type(currentNode.tokenOrVariable) is SubList:
                if type(tokens[index]) is tc.START_SUB:
                    currentNode.addChild(tc.START_SUB())
                    currentNode.addChild(tc.Label())
                    currentNode.addChild(tc.Colon())
                    currentNode.addChild(CodeList())
                    currentNode.addChild(SubList())
                elif type(tokens[index]) is tc.END_PROGRAM:
                    currentNode.addChild(tc.END_PROGRAM())
                    
                else:
                    raise Exception("Error on SubList")
                    
                    
            elif type(currentNode.tokenOrVariable) is CodeList:
                if type(tokens[index]) is tc.PRINT or type(tokens[index]) is tc.GOSUB or type(tokens[index]) is tc.Label or type(tokens[index]) is tc.IF or type(tokens[index]) is tc.WHILE:
                    currentNode.addChild(CodeLine())
                    currentNode.addChild(CodeList())
                elif type(tokens[index]) is tc.END_SUB:
                    currentNode.addChild(tc.END_SUB())

                else:
                    raise Exception("Error on CodeList")
            
            elif type(currentNode.tokenOrVariable) is CodeLine:
                if type(tokens[index]) is tc.Label:
                    currentNode.addChild(LineLabel())
                elif type(tokens[index]) is tc.IF:
                    currentNode.addChild(Condition())
                elif type(tokens[index]) is tc.WHILE:
                    currentNode.addChild(Loop())
                elif type(tokens[index]) is tc.PRINT:
                    currentNode.addChild(tc.PRINT())
                    currentNode.addChild(tc.SoftOpen())
                    currentNode.addChild(Expression())
                    currentNode.addChild(tc.SoftClose())
                    currentNode.addChild(tc.Semicolon())
                elif type(tokens[index]) is tc.GOSUB:
                    currentNode.addChild(tc.GOSUB())
                    currentNode.addChild(tc.Label())
                    currentNode.addChild(tc.Semicolon())
                else:
                    raise Exception("Error on CodeLine")
                    
            elif type(currentNode.tokenOrVariable) is LineLabel:
                if type(tokens[index]) is tc.Label:
                    currentNode.addChild(tc.Label())
                    currentNode.addChild(Assignment())
                else:
                    raise Exception("LineLabel")
                    
            elif type(currentNode.tokenOrVariable) is Assignment:
                if type(tokens[index]) is tc.Assignment:
                    currentNode.addChild(tc.Assignment())
                    currentNode.addChild(ExpressionOrInput())
                    currentNode.addChild(tc.Semicolon())
                    
                elif type(currentNode.tokenOrVariable) is tc.HardOpen:
                    currentNode.addChild(tc.HardOpen())
                    currentNode.addChild(tc.Integer())
                    currentNode.addChild(tc.HardClose())
                    currentNode.addChild(tc.assignment())
                    currentNode.addChild(ExpressionOrInput())
                    currentNode.addChild(tc.Semicolon())
                else:
                    raise Exception("Error on Assignment")
                    
            
            elif type(currentNode.tokenOrVariable) is Condition:
                if type(tokens[index]) is tc.IF:
                    currentNode.addChild(tc.IF())
                    currentNode.addChild(Expression())
                    currentNode.addChild(tc.CompOp())
                    currentNode.addChild(Expression())
                    currentNode.addChild(tc.THEN())
                    currentNode.addChild(ThenCodeList())
                else:
                    raise Exception("Error on Condition")
                    
            elif type(currentNode.tokenOrVariable) is ThenCodeList:
                if type(tokens[index]) is tc.PRINT or type(tokens[index]) is tc.GOSUB or type(tokens[index]) is tc.Label or type(tokens[index]) is tc.IF or type(tokens[index]) is tc.WHILE:
                    currentNode.addChild(CodeLine())
                    currentNode.addChild(ThenCodeList())
                elif type(tokens[index]) is tc.ELSE:
                    currentNode.addChild(tc.ELSE())
                    currentNode.addChild(ElseCodeList())

                else:
                    raise Exception("Error on ThenCodeList")
                    
            elif type(currentNode.tokenOrVariable) is ElseCodeList:
                if type(tokens[index]) is tc.PRINT or type(tokens[index]) is tc.GOSUB or type(tokens[index]) is tc.Label or type(tokens[index]) is tc.IF or type(tokens[index]) is tc.WHILE:
                    currentNode.addChild(CodeLine())
                    currentNode.addChild(CodeList())
                elif type(tokens[index]) is tc.END_IF:
                    currentNode.addChild(tc.END_IF())

                else:
                    raise Exception("Error on ElseCodeList")
                    
            elif type(currentNode.tokenOrVariable) is Loop:
                if type(tokens[index]) is tc.WHILE:
                    currentNode.addChild(tc.WHILE())
                    currentNode.addChild(Expression())
                    currentNode.addChild(tc.CompOp())
                    currentNode.addChild(Expression())
                    currentNode.addChild(tc.DO())
                    currentNode.addChild(WhileCodeList())
                else:
                    raise Exception("Error on Loop")        
            
            elif type(currentNode.tokenOrVariable) is WhileCodeList:
                if type(tokens[index]) is tc.PRINT or type(tokens[index]) is tc.GOSUB or type(tokens[index]) is tc.Label or type(tokens[index]) is tc.IF or type(tokens[index]) is tc.WHILE:
                    currentNode.addChild(CodeLine())
                    currentNode.addChild(WhileCodeList())
                elif type(tokens[index]) is tc.END_WHILE:
                    currentNode.addChild(tc.END_WHILE())

                else:
                    raise Exception("Error on WhileCodeList")
            
            elif type(currentNode.tokenOrVariable) is ExpressionOrInput:
                if type(tokens[index]) is tc.SoftOpen or type(tokens[index]) is tc.Integer or type(tokens[index]) is tc.CharacterString or type(tokens[index]) is tc.Label:
                    currentNode.addChild(Expression())
                elif type(tokens[index]) is tc.INPUT:
                    currentNode.addChild(tc.INPUT())
                   # currentNode.addChild(tc.Semicolon())

                else:
                    raise Exception("Error on ElseCodeList")
            
            elif type(currentNode.tokenOrVariable) is Expression:
                if type(tokens[index]) is tc.SoftOpen or type(tokens[index]) is tc.Integer or type(tokens[index]) is tc.CharacterString or type(tokens[index]) is tc.Label:
                    currentNode.addChild(Term())
                    currentNode.addChild(TermTail())
                else:
                    raise Exception("Error on Expression")
                    
                    
            elif type(currentNode.tokenOrVariable) is TermTail:
                if type(tokens[index]) is tc.AddOp:
                    currentNode.addChild(tc.AddOp())
                    currentNode.addChild(Term())
                    currentNode.addChild(TermTail())
                elif type(tokens[index]) is tc.CompOp or type(tokens[index]) is tc.DO or type(tokens[index]) is tc.SoftClose or type(tokens[index]) is tc.Semicolon or type(tokens[index]) is tc.THEN:

                    currentNode.addChild(None)
                else:
                    raise Exception("Error on TermTail")
                    
                    
            elif type(currentNode.tokenOrVariable) is Term:
                if type(tokens[index]) is tc.SoftOpen or type(tokens[index]) is tc.Integer or type(tokens[index]) is tc.CharacterString or type(tokens[index]) is tc.Label:
                    currentNode.addChild(Factor())
                    currentNode.addChild(FactorTail())
                else:
                    raise Exception("Error on Term")
                    
                    
            elif type(currentNode.tokenOrVariable) is FactorTail:
                if type(tokens[index]) is tc.MultOp:
                    currentNode.addChild(tc.MultOp())
                    currentNode.addChild(Factor())
                    currentNode.addChild(FactorTail())
                elif type(tokens[index]) is tc.AddOp or type(tokens[index]) is tc.CompOp or type(tokens[index]) is tc.DO or type(tokens[index]) is tc.SoftClose or type(tokens[index]) is tc.Semicolon or type(tokens[index]) is tc.THEN:
                    currentNode.addChild(None)
                else:
                    raise Exception("Error on FactorTail")
                    
                    
            elif type(currentNode.tokenOrVariable) is Factor:
                if type(tokens[index]) is tc.Integer:
                    currentNode.addChild(tc.Integer())
                elif type(tokens[index]) is tc.SoftOpen:
                    currentNode.addChild(tc.SoftOpen())
                    currentNode.addChild(Expression())
                    currentNode.addChild(tc.SoftClose())
                elif type(tokens[index]) is tc.CharacterString:
                    currentNode.addChild(tc.CharacterString())
                elif type(tokens[index]) is tc.Label:
                    currentNode.addChild(tc.Label())
                    currentNode.addChild(PossibleArray())
                else:
                    raise Exception("Error on Factor")
                    
                    
            elif type(currentNode.tokenOrVariable) is PossibleArray:
                if type(tokens[index]) is tc.HardOpen:
                    currentNode.addChild(tc.HardOpen())
                    currentNode.addChild(tc.Integer())
                    currentNode.addChild(tc.HardClose())
                elif type(tokens[index]) is tc.AddOp or type(tokens[index]) is tc.CompOp or type(tokens[index]) is tc.DO or type(tokens[index]) is tc.SoftClose or type(tokens[index]) is tc.Semicolon or type(tokens[index]) is tc.THEN:
                    currentNode.addChild(None)
                else:
                    raise Exception("Error on FactorTail")
                    
                    
            elif isinstance(currentNode.tokenOrVariable,tc.Token):
                if type(tokens[index]) is type(currentNode.tokenOrVariable):
                    currentNode.tokenOrVariable = tokens[index]
                    index += 1
                else:
                    raise Exception("Expected token "+str(type(currentNode.tokenOrVariable))+" Instead got "+str(type(tokens[index])))
        currentNode = currentNode.nextNode()

    return parseTree

