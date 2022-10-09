from abc import ABC
from typing import List


class PyObject(ABC):
    '''Python Object Block'''
    pass


class MyDict(dict):
    def __init__(self) -> None:
        self.scope = PyObjects.Block(None, [])
        self.line_count = 0

        # global indentation level *************
        self.indentation = 0

    def append(self, new_line) -> None:
        '''Append code block to end of code'''
        self.line_count += 1
        self[self.line_count] = new_line

    def replace_line(self, new_line: object, line_number: int) -> object:
        '''Replace line with new_block, return old line'''
        old_line = self[line_number]
        self[line_number] = new_line

        return old_line

    def pop(self, line_number: int) -> object:
        '''Pop line number line. Return block if line exists, -1 otherwise'''
        if line_number not in self:
            return -1
        self.line_count -= 1

        line = self.pop(line_number)

        for key in self.keys[line_number:]:
            self[key-1] = self.pop(key)

        return line

    def insert(self, line_number: int, new_line: object) -> object:
        '''Insert block at line'''

        if line_number > self.line_count:
            return

        self.line_count += 1

        for key in reversed(self[line_number:].keys()):
            self[line_number+1] = self.pop(line_number)

        self[line_number] = new_line


class PyObjects:
    class Condition(PyObject):
        '''Condition statement containing string condition'''

        def __init__(self, condition: str) -> None:
            super().__init__()

            self._condition = condition

        def condition(self) -> str:
            return self._condition

    class Variable(PyObject):
        '''Variable containing name and value'''

        def __init__(self, parent: PyObject, var_name: str, var_value: str) -> None:
            super().__init__()

            self.indentation = parent.indentation + 1
            self.parent = parent
            self._name = var_name
            self._value = var_value

        @property
        def name(self) -> str:
            return self._name

        @property
        def value(self) -> str:
            return self._value

    class Statement(PyObject):
        '''Statement -> string containing code'''

        def __init__(self, parent: PyObject, statement: str) -> None:
            super().__init__()

            self.indentation = parent.indentation + 1
            self.parent = parent
            self._statement = statement

        @property
        def statement(self) -> str:
            return self._statement

    class Block(PyObject):
        '''Block containing list of child PyObjects'''

        def __init__(self, parent: PyObject, children: List[PyObject]) -> None:
            super().__init__()

            if parent:
                self.indentation = parent.indentation + 1
            else:
                self.indentation = -1
            self.parent = parent
            self._children = children

        @property
        def children(self) -> List[PyObject]:
            return self._children

        def insert_child(self, new_child: PyObject) -> None:
            self._children.append(new_child)

        def remove_child(self, child: PyObject) -> PyObject:
            return self._children.remove(child)

    class If(PyObject):
        '''If containing condition PyObject and block PyObject'''

        def __init__(self, parent: PyObject, condition: PyObject, block: PyObject) -> None:
            super().__init__()

            self.indentation = parent.indentation + 1
            self.parent = parent
            self._condition = condition
            self._block = block

        @property
        def condition(self) -> PyObject:
            return f'if {self._condition.condition()}:'

        @property
        def block(self) -> PyObject:
            return self._block

        def set_block(self, new_block: PyObject) -> None:
            self._block = new_block

        def insert_child(self, child: PyObject) -> None:
            self._block.insert_child(child)

    class IfElse(PyObject):
        '''If Else block containing condition, if Block, else Block'''

        def __init__(self, parent: PyObject, condition: PyObject, if_block: PyObject, else_block: PyObject) -> None:
            super().__init__()

            self.indentation = parent.indentation + 1
            self.parent = parent
            self._condition = condition
            self._if_block = if_block
            self._else_block = else_block

        @property
        def condition(self) -> PyObject:
            return self._condition

        @property
        def else_str(self) -> str:
            return 'else:'

        @property
        def if_block(self) -> PyObject:
            return self._if_block

        @property
        def else_block(self) -> PyObject:
            return self._else_block

        def set_if_block(self, new_block: PyObject) -> None:
            self._if_block = new_block

        def set_else_block(self, new_block: PyObject) -> None:
            self._else_block = new_block

        def insert_if_child(self, child: PyObject) -> None:
            self._if_block.insert_child(child)

        def insert_else_child(self, child: PyObject) -> None:
            self._else_block.insert_child(child)

    class While(PyObject):
        '''While PyObject containing condition and Block'''

        def __init__(self, parent: PyObject, condition: PyObject, block: PyObject) -> None:
            super().__init__()

            self.indentation = parent.indentation + 1
            self.parent = parent
            self._condition = condition
            self._block = block

        @property
        def condition(self) -> str:
            return f'while {self._condition.condition()}:'

        @property
        def block(self) -> PyObject:
            return self._block

        def set_block(self, new_block: PyObject) -> None:
            self._block = new_block

        def insert_child(self, child: PyObject) -> None:
            self._block.insert_child(child)

    class For(PyObject):
        '''For containing start, end, and For block'''

        def __init__(self, parent: PyObject, start: int, end: int, block: PyObject) -> None:
            super().__init__()

            self.indentation = parent.indentation + 1
            self.parent = parent
            self._start = start
            self._end = end
            self._block = block

        @property
        def start(self) -> int:
            return self._start

        @property
        def end(self) -> int:
            return self._end

        @property
        def condition(self) -> int:
            if self._start:
                return f'for i in range({self._start, self._end})'
            else:
                return f'for i in range({self._end})'

        @property
        def block(self) -> PyObject:
            return self._block

        def set_block(self, new_block: PyObject) -> None:
            self._block = new_block

        def insert_child(self, child: PyObject) -> None:
            self._block.insert_child(child)

    class Function(PyObject):
        def __init__(self, parent: PyObject, func_name: str, func_args: str, block: PyObject) -> None:
            super().__init__()

            self.indentation = parent.indentation + 1
            self.parent = parent
            self._block = block
            self._name = func_name
            self._args = func_args

        @property
        def name(self) -> str:
            return self._name

        @property
        def args(self) -> str:
            return self._args

        @property
        def signature(self) -> str:
            return f'def {self._name}({self._args}):'

        @property
        def block(self) -> PyObject:
            return self._block

        def set_block(self, new_block: PyObject) -> None:
            self._block = new_block

        def insert_child(self, child: PyObject) -> None:
            self._block.insert_child(child)

    class Call(PyObject):
        def __init__(self, parent: PyObject, func_name: str, func_args: str) -> None:
            super().__init__()

            self.indentation = parent.indentation + 1
            self.parent = parent
            self._name = func_name
            self._args = func_args

        @property
        def name(self) -> str:
            return self._name

        @property
        def args(self) -> str:
            return self._args

        @property
        def call(self) -> str:
            return f'{self._name}({self._args}):'
