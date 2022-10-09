import os
from tkinter import *
from tkinter.filedialog import Open, asksaveasfilename, askopenfilename
import subprocess

compiler = Tk()
compiler.title('Audio Studio')
file_path = ''
    

def set_file_path(path):
    global file_path
    file_path = path


def open_file():
    path = "./ide/audioCode.py"
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)

def outputLoading():
     code_output.insert('1.0', "Loading code from database")

def save_as():
    file_path = "./ide/audioCode.py"
    with open(file_path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)


def openEditor():
    compiler.mainloop()

def updateGraphics():
    compiler.update()

def compileAndRun():
    save_as()
    run()

def run():
    code_output.insert('1.0', '')
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0',  error)


menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
menu_bar.add_cascade(label='File', menu=file_menu)


run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=compileAndRun)
menu_bar.add_cascade(label='Run', menu=run_bar)

compiler.config(menu=menu_bar)

editor = Text()
editor.pack()

code_output = Text(height=10)
code_output.pack()
