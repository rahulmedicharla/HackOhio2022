# pyobjects
from PyObjects import PyObjects, MyDict
from Parser import TextToCode, CodeToText

# firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

code = MyDict()
text = MyDict()


def input(event):
    print(1)
    if not event.data:
        return
    print(event.data)
    # text = MyDict()

    tokens = event.data.split(" ")
    print(tokens)
    TextToCode.parse(tokens, code, code.append)

    CodeToText.parse(code.scope, text, text.append)

    print(text)
    # db.reference('/output').delete()
    db.reference('/output').set(text)


def fire():
    cred = credentials.Certificate("firebaseConfig.json")
    firebase_admin.initialize_app(
        cred, {'databaseURL': 'https://hackohio2022-1ccea-default-rtdb.firebaseio.com/'})

    db.reference('/input').listen(input)
    while db.reference('/isLive').get():
        pass


fire()
