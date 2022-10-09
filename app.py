from asyncio import events
from time import time
from ide.controller import Controller
from ide.model import Model
import ide.view
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def outputCode(event):
    with open("./ide/audioCode.py", "w") as file:
        for line in event.data:
            if line:
                file.write(( int(line[0]) * "\t") + line[1:] + '\n')
    ide.view.open_file()
    ide.view.outputLoading()
    
def runCode(event):
    if(event.data == 1):
        ide.view.compileAndRun()
        db.reference('/shouldRun').set(0)

def main():
    cred = credentials.Certificate("firebaseConfig.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://hackohio2022-1ccea-default-rtdb.firebaseio.com/'
    })

    db.reference('/isLive').set(1)
    db.reference('/shouldRun').listen(runCode)
    db.reference('/output').listen(outputCode)

    ide.view.openEditor()

    db.reference('/isLive').set(0)

    model = Model()
    #controller = Controller(model, view)
    pass
    
if __name__ == "__main__":
    main()