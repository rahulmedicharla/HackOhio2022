from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

class View():
    def __init__(self):
        self.compiler = Tk()
        self.filePath = ''
        self.editor = Text()
        self.codeOutput = Text(height=10)

        self.editor.pack()
        self.codeOutput.pack()

        self.initGUI()

    def setFilePath(self, path):
        self.filePath = path
    
    def initGUI(self):
        self.compiler.title("Audio Studio")

        menuBar = Menu(self.compiler)

        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label='Open', command=self.openFile) 
        fileMenu.add_command(label='Save As', command=self.saveAs)
        fileMenu.add_command(label='Save', command=self.saveAs) 
        menuBar.add_cascade(label='File', menu=fileMenu)


        runBar = Menu(menuBar, tearoff=0)
        runBar.add_command(label='Run', command=self.run)
        menuBar.add_cascade(label='Run', menu=runBar)

        self.compiler.config(menu = menuBar)

        self.compiler.mainloop()

    def openFile(self):
        path = askopenfilename(filetypes=[('Python Files', '*py')])
        with open(path, 'r') as file:
            code = file.read()
            self.editor.delete('1.0', END)
            self.editor.insert('1.0', code)
            self.setFilePath(path)

    def saveAs(self):
        if(self.filePath == ''):
            path = asksaveasfilename(filetypes=[('Python Files', '*py')])
        else:
            path = self.filePath
        with open(path, 'w') as file:
            code = self.editor.get('1.0', END)
            file.write(code)
            self.setFilePath(path)

    def run(self):
        if(self.filePath == ''):
            savePromt = Toplevel()
            text = Label(savePromt, text="Please save code to run")
            text.pack()
            return
        command = f'python {self.filePath}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        self.codeOutput.insert('1.0', output)
        self.codeOutput.insert('1.0', error)
    