import tkinter as tk
from tkinter import ttk

windowSize = [800,360]

class PasswordADM(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        
    def create_widgets(self):
        background = tk.Frame(self.master, width=windowSize[0], height=windowSize[1], bg="Deep sky blue")
        background.place(x=0, y=0)
        
        frameTools = tk.Frame(background, width=200, height=windowSize[1], bg="gray")
        frameTools.place(x=600, y=0)
        
        btnNew = tk.Button(frameTools, text="Criar senha",width=16,font=("Verdana",13))
        btnNew.place(x=10,y=10)
        btnSearch = tk.Button(frameTools, text="Procurar senha",width=16,font=("Verdana",13))
        btnSearch.place(x=10,y=50)
        btnUpdate = tk.Button(frameTools, text="Atualizar senha",width=16,font=("Verdana",13))
        btnUpdate.place(x=10,y=90)
        btnDelete = tk.Button(frameTools, text="Deletar senha",width=16,font=("Verdana",13))
        btnDelete.place(x=10,y=130)
        
        listPass= ttk.Treeview(background, column=("column1", "column2", "column3","column4"), show='headings',height=16)
        listPass.heading("#1", text="ID")
        listPass.heading("#2", text="Senha")
        listPass.heading("#3", text="Onde será usada")
        listPass.heading("#4", text="Data de criação")
        listPass.column('#1', width=80)
        listPass.column('#2', width=240)
        listPass.column('#3', width=120)
        listPass.column('#4', width=120)

        scrollPass = tk.Scrollbar(background)
        listPass.configure(yscrollcommand=scrollPass.set)   
        scrollPass.configure(command=listPass.yview)       
        
        listPass.place(x=10,y=5)
        scrollPass.place(x=570,y=6,height=345)
                
    def Run():
        root = tk.Tk()
        root.title("Password Administrator V0.0.0")
        app = PasswordADM(master=root)
        root.geometry(str(windowSize[0])+"x"+str(windowSize[1]))
        root.resizable(width=False,height=False)
        app.mainloop()