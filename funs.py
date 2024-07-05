from tkinter import*
import tkinter.filedialog as fd

def __init__(self):

    def choose(self):
        directory = fd.askdirectory(title="Открыть папку", initialdir="/")
        if directory:
            print(directory)
