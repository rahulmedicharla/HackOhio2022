import code
from PyObjects import PyObjects, PyObject
from typing import Callable


class TextToCode():
    def parse_variable(tokens: list[str], code_dict: dict, action: Callable):
        if not tokens:
            return

        tokens.pop(0)
        var_name = tokens.pop(0)
        tokens.pop(0)
        var_value = tokens.pop(0)

        var = PyObjects.Variable(code_dict.scope, var_name, var_value)
        code_dict.scope.block.insert_child(var)
        action(var)

    def parse_statement(tokens: list[str], code_dict: dict, action: Callable):
        if not tokens:
            return

        tokens.pop(0)

        statement = PyObjects.Statement(code_dict.scope, " ".join(tokens[0:]))
        statement.parent.insert_child(statement)
        action(statement)

    def parse_if(tokens: list[str], code_dict: dict, action: Callable):
        if not tokens:
            return

        tokens.pop(0)

        if_block = PyObjects.If(code_dict.scope, PyObjects.Condition(
            " ".join(tokens[0:])), PyObjects.Block(None, []))
        if_block.set_block(PyObjects.Block(if_block, []))
        if_block.parent.insert_child(if_block)
        action(if_block)

        code_dict.scope = code_dict[code_dict.line_count]

    def parse_if_else(tokens: list[str], code_dict: dict, action: Callable):
        if not tokens:
            return

        tokens.pop(0)
        if_else_block = PyObjects.IfElse(code_dict.scope, PyObjects.Condition(
            " ".join(tokens[0:])), PyObjects.Block(
            None, []), PyObjects.Block(None, []))
        if_else_block.set_if_block(PyObjects.Block(if_else_block, []))
        if_else_block.set_else_block(PyObjects.Block(if_else_block, []))
        if_else_block.parent.block.insert_child(if_else_block)

        action(if_else_block)

    def parse_while(tokens: list[str], code_dict: dict, action: Callable):
        if not tokens:
            return

        tokens.pop(0)
        while_block = PyObjects.While(
            code_dict.scope, PyObjects.Condition(" ".join(tokens[0:])), PyObjects.Block(None, []))
        while_block.set_block(PyObjects.Block(while_block, []))
        while_block.parent.insert_child(while_block)
        action(while_block)

        code_dict.scope = code_dict[code_dict.line_count]

    def parse_for(tokens: list[str], code_dict: dict, action: Callable):
        if not tokens:
            return

        tokens.pop(0)
        start = tokens.pop(0)
        tokens.pop(0)
        end = tokens.pop(0)

        for_block = PyObjects.For(
            code_dict.scope,  start, end, PyObjects.Block(None, []))
        for_block.set_block(PyObjects.Block(for_block, []))
        for_block.parent.insert_child(for_block)

        action(for_block)
        code_dict.scope = code_dict[code_dict.line_count]

    def parse_call(tokens: list[str], code_dict: dict, action: Callable):
        if not tokens:
            return

        tokens.pop(0)
        name = tokens.pop(0)
        args = ",".join(tokens[0:])

        call_block = PyObjects.Call(
            code_dict.scope, name, args)
        call_block.parent.insert_child(call_block)

        action(call_block)

    def back_out(tokens, code_dict, action):
        code_dict.scope = code_dict.scope.parent

    def parse(tokens: list[str], code_dict: dict, action: Callable):
        if tokens[0] in T2C_jump:
            T2C_jump[tokens[0]](tokens, code_dict, action)


T2C_jump = {
    "variable": TextToCode.parse_variable,
    "statement": TextToCode.parse_statement,
    "while": TextToCode.parse_while,
    "for": TextToCode.parse_for,
    "if": TextToCode.parse_if,
    "if else": TextToCode.parse_if_else,
    "call": TextToCode.parse_call,
    "close": TextToCode.back_out
}


class CodeToText():
    def parse_block(block, text_dict: dict, action: Callable):
        for child in block.children:
            CodeToText.parse(child, text_dict, action)

    def parse_statement(statement: PyObject, text_dict: dict, action: Callable):
        action(f'{statement.indentation}{statement.statement}')

    def parse_variable(var: PyObject, text_dict: dict, action: Callable):
        action(f'{var.indentation}{var.name} = {var.value}')

    def parse_call(call_block: PyObject, text_dict: dict, action: Callable):
        action(f'{call_block.indentation}{call_block.call}')

    def parse_if(if_block: PyObject, text_dict: dict, action: Callable):
        action(f'{if_block.indentation}{if_block.condition}')
        CodeToText.parse_block(if_block.block, text_dict, action)

    def parse_if_else(if_else_block: PyObject, text_dict: dict, action: Callable):
        action(f'{if_else_block.indentation}{if_else_block.condition}')
        CodeToText.parse_block(if_else_block.if_block, text_dict, action)
        action(if_else_block.else_str)
        CodeToText.parse_block(if_else_block.else_block, text_dict, action)

    def parse_while(while_block: PyObject, text_dict: dict, action: Callable):
        action(f'{while_block.indentation}{while_block.condition}')
        CodeToText.parse_block(while_block.block, text_dict, action)

    def parse_for(for_block: PyObject, text_dict: dict, action: Callable):
        action(f'{for_block.indentation}{for_block.condition}')
        CodeToText.parse_block(for_block.block, text_dict, action)

    def parse(block: PyObject, text_dict: dict, action: Callable):
        return C2T_jump[type(block)](block, text_dict, action)


C2T_jump = {
    PyObjects.Variable: CodeToText.parse_variable,
    PyObjects.Statement: CodeToText.parse_statement,
    PyObjects.Block: CodeToText.parse_block,
    PyObjects.While: CodeToText.parse_while,
    PyObjects.For: CodeToText.parse_for,
    PyObjects.If: CodeToText.parse_if,
    PyObjects.IfElse: CodeToText.parse_if_else,
    PyObjects.Call: CodeToText.parse_call
}
