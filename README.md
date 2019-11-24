# Advanced-MindBlock-Compiler

This compiler was made as part of a 400 level Programming Languages course. it consists of a tokenizer, parser, and python code to create runnable C code from the parse tree.

# Tokenizer

The tokenizer takes in a '.amb' file. It will tokenize symbols, keywords, integers, labels, and strings. Tokens are all subclasses of a 'Token' class. For example START_PROGRAM would tokenize into a START_PROGRAM object that's a subclass of the Token class.

A list of tokens is returned, in order, to the parse tree generator.

# Parsing and Translation
The parse tree generator takes the given list of tokens and uses the AMB grammar to create a tree. Each node has it's C languge equivalent which is dumped into a list. The list is then printed into a C file, compiled, and executed.

# Notes
1. The program currently uses GCC to compile. This can be changed in the starter file.
2. The grammar doesn't indicate a space being necessary between PRINT and the parentheses containing what is going to be printed, however without a space the program runs into a parse tree error, so a space should be used. 
ie. PRINT (*your text here*)
3. There's a test.amb file that can be used as an example of the grammar, as well as testing that the program is working properly.
