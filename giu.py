import tkinter as tk
from tkinter import *
from tkinter import ttk
from training import *
import tkinter.filedialog as fd

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Defect detection service")
        self.geometry("1440x1024")
        self.resizable(True, True)

        notebook = ttk.Notebook()
        notebook.pack(expand=True, fill=BOTH)

        frame1 = ttk.Frame(notebook)
        frame2 = ttk.Frame(notebook)
        frame3 = ttk.Frame(notebook)

        frame1.pack(fill=BOTH, expand=True)
        frame2.pack(fill=BOTH, expand=True)
        frame3.pack(fill=BOTH, expand=True)

        notebook.add(frame1, text="Training")
        notebook.add(frame2, text="Runtime")
        notebook.add(frame3, text="Statistics")


        btn_choose = ttk.Button(frame1, text="Выбрать файлы для обучения", command=self.choose_directory)
        btn_choose.place(x=143.36, y=216.0, width=363.29, height=105.0)



        runtime_btn = ttk.Button(text="Runtime")
        runtime_btn.place(x=143.36, y=216.0+105+50, width=363.29, height=105.0)

    def choose_directory(self):
        directory = fd.askdirectory(title="Открыть папку", initialdir="/")
        if directory:
            print(directory)







if __name__ == "__main__":
    app = App()
    app.mainloop()
