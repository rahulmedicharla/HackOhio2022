# pyobjects
from PyObjects import PyObjects
from Parser import ParserC2T

# firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


def fire():
    cred = credentials.Certificate("firebaseConfig.json")
    firebase_admin.initialize_app(
        cred, {'databaseURL': 'https://hackohio2022-1ccea-default-rtdb.firebaseio.com/'})

    ref = db.reference('/output')
    ref.set(test())


def test():

    statement = PyObjects.Statement("x = 1")
    statement2 = PyObjects.Statement("x += 2")
    statement3 = PyObjects.Statement(
        "print(\"like so gay it hurts\")")
    block = PyObjects.Block([statement, statement2, statement3])

    statement4 = PyObjects.Statement("print(\"else executed\")")
    block2 = PyObjects.Block([statement4])
    if_else_block = PyObjects.IfElse("x > 1", block, block2)
    main_block = PyObjects.Block([if_else_block])

    ParserC2T.parse(main_block)

    return ParserC2T.code


fire()
