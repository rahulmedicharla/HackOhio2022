from PyObjects import PyObjects
from Parser import Parser


def test():
    statement = PyObjects.Statement("x = 1")
    statement2 = PyObjects.Statement("x += 2")
    statement3 = PyObjects.Statement("print(x)")
    block = PyObjects.Block([statement, statement2, statement3])

    statement4 = PyObjects.Statement("print(\"else executed\")")
    block2 = PyObjects.Block([statement4])
    if_else_block = PyObjects.IfElse("x > 1", block, block2)
    main_block = PyObjects.Block([if_else_block])

    Parser.parse(main_block)

    for line, code in Parser.code.items():
        print(f'{line}    {code}')


test()
