import sys

from antlr4 import *

from antlr_gen.CLexer import CLexer
from antlr_gen.CListener import CListener
from antlr_gen.CParser import CParser


class FunctionListener(CListener):
    def enterFunctionDefinition(self, ctx: CParser.FunctionDefinitionContext):
        # Get the function name
        function_name = ctx.declarator().directDeclarator().directDeclarator().getText()

        # Get the return type
        return_type = ctx.declarationSpecifiers().getText()

        print(f"Function Name: {function_name}, Return Type: {return_type}")


def main():
    # Check if command line arguments were provided
    if len(sys.argv) > 1:
        # Get the filename from the first command line argument
        filename = sys.argv[1]
    else:
        print("Please provide a filename as a command line argument.")
        sys.exit()

    # Use the filename to create a FileStream
    input_stream = FileStream(filename)

    # create a lexer and parser
    lexer = CLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CParser(stream)

    # create the parse tree
    tree = parser.compilationUnit()

    # create the listener and walker
    listener = FunctionListener()
    walker = ParseTreeWalker()

    # walk the tree
    walker.walk(listener, tree)

    # Open the file
    with open('conf/def_macros.txt', 'r') as file:
        # Read the file line by line
        for line in file:
            # Print each line
            print(line)


if __name__ == '__main__':
    main()
