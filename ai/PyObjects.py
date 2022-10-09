from abc import ABC
from typing import List


class PyObject(ABC):
    '''Python Object Block'''
    pass


class PyObjects:
    class Statement(PyObject):
        '''Statement -> string containing code'''

        def __init__(self, statement: str) -> None:
            super().__init__()

            self._statement = statement

        @property
        def statement(self) -> str:
            return self._statement

    class Block(PyObject):
        '''Block containing list of child PyObjects'''

        def __init__(self, children: List[PyObject]) -> None:
            super().__init__()
            self._children = children

        @property
        def children(self) -> List[PyObject]:
            return self._children

    class If(PyObject):
        '''If containing condition PyObject and block PyObject'''

        def __init__(self, condition: str, block: PyObject) -> None:
            super().__init__()

            self._condition = condition
            self._block = block

        @property
        def conditional(self) -> str:
            return f'if {self._condition}:'

        @property
        def block(self) -> PyObject:
            return self._block

    class IfElse(PyObject):
        '''If Else block containing condition, if Block, else Block'''

        def __init__(self, condition: str, if_block: PyObject, else_block: PyObject) -> None:
            super().__init__()

            self._condition = condition
            self._if_block = if_block
            self._else_block = else_block

        @property
        def conditional(self) -> str:
            return f'if {self._condition}:'

        @property
        def else_str(self) -> str:
            return 'else:'

        @property
        def if_block(self) -> PyObject:
            return self._if_block

        @property
        def else_block(self) -> PyObject:
            return self._else_block

    class While(PyObject):
        '''While PyObject containing condition and Block'''

        def __init__(self, condition: str, block: PyObject) -> None:
            super().__init__()

            self._condition = condition
            self._block = block

        @property
        def conditional(self) -> str:
            return f'while {self._condition}:'

        @property
        def block(self) -> PyObject:
            return self._block

    class For(PyObject):
        '''For containing start, end, and For block'''

        def __init__(self, start: int, end: int, block: PyObject) -> None:
            super().__init__()

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
        def conditional(self) -> int:
            if self._start:
                return f'for i in range({self._start, self._end})'
            else:
                return f'for i in range({self._end})'

        @property
        def block(self) -> PyObject:
            return self._block
