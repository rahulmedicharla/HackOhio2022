from ide.controller import Controller
from ide.model import Model
from ide.view import View

def main():
    view = View()
    model = Model()
    controller = Controller(model, view)
    pass
    
if __name__ == "__main__":
    main()