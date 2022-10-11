import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class Model():
    def __init__(self):
        self.x = 0
    
    def setData(self, path, data):
        ref = db.reference(path)
        ref.set(data)

    def updateData(self, path, data):
        ref = db.reference(path)
        ref.update(data)
    
    def getData(self, path):
        ref = db.reference(path)
        return ref.get()
