from abc import ABC
from typing import List
import PyObjects_interface

class PyObject(ABC):
    '''Python Object Block'''
    pass

class PyObjects:
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
            
            self._condition: str
            self._block: PyObject
        
        @property
        def condition(self) -> str:
            return self._condition
        
        @property
        def block(self) -> PyObject:
            return self._block
        
    class IfElse(PyObject):
        '''If Else block containing condition, if Block, else Block'''
        def __init__(self, condition: str, if_block: PyObject, else_block: PyObject) -> None:
            super().__init__()
            
            self._condition = condition
            self._if_block: if_block
            self._else_block: else_block
            
        @property
        def condition(self) -> str:
            return self._condition
        
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
        def condition(self) -> str:
            return self._condition
        
        @property
        def block(self) -> PyObject:
            return self._block
        
    class Method(PyObject):
        '''Method containing args, Method block, and return'''
        def __init__(self, block: PyObject, return_obj: str, *args: List[str]) -> None:
            super().__init__()
            
            self._block = block
            self._return_obj = return_obj
            self._args = args
            
        @property
        def block(self) -> PyObject:
            return self._block
        
        @property
        def return_obj(self) -> str:
            return self._return_obj

        @property
        def args(self) -> List[str]:
            return self.args
