from PyObjects import PyObjects

def add_to_dict(string):
    Parser.lines += 1
    Parser.code[Parser.lines] = string
    
class Parser:
    lines = 0
    code = {}
    
    def parse_block(block):
        for child in block.children:
            Parser.parse(child)

    def parse_statement(statement):
        add_to_dict(statement.statement)

    def parse_if(if_block):
        add_to_dict(if_block.conditional)
        Parser.parse_block(if_block.block)

    def parse_if_else(if_else_block):
        add_to_dict(if_else_block.conditional)
        Parser.parse_block(if_else_block.if_block)
        add_to_dict(if_else_block.else_str)
        Parser.parse_block(if_else_block.else_block)

    def parse_while(while_block):
        add_to_dict(while_block.conditional)
        Parser.parse_block(while_block.block)

    def parse_for(for_block):
        add_to_dict(for_block.conditional)
        Parser.parse_block(for_block.block)

    def parse(block):
        jump_table[type(block)](block)

jump_table = {
            PyObjects.Block: Parser.parse_block,
            PyObjects.Statement: Parser.parse_statement,
            PyObjects.If: Parser.parse_if,
            PyObjects.IfElse: Parser.parse_if_else,
            PyObjects.While: Parser.parse_while,
            PyObjects.For: Parser.parse_for
    }