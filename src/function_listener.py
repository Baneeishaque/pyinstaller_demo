from antlr_gen.CListener import CListener
from antlr_gen.CParser import CParser


class FunctionListener(CListener):
    def enterFunctionDefinition(self, ctx: CParser.FunctionDefinitionContext):
        # Get the function name
        function_name = ctx.declarator().directDeclarator().directDeclarator().getText()

        # Get the return type
        return_type = ctx.declarationSpecifiers().getText()

        print(f"Function Name: {function_name}, Return Type: {return_type}")
