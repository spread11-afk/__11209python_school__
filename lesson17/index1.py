import dataSource
import tkinter as tk
from tkinter import ttk


class Window(tk.Tk):
    def __init__(self,**kwargs) -> None:
        super().__init__(**kwargs)
        self.title("鄉鎮人口")
        self.configure(background='#86473F')
        topFrame = tk.Frame(self,background='#CB1B45')
        label = ttk.Label(topFrame,text="鄉鎮人口",font=("arial",30,"bold"))
        label.pack(padx=10,pady=10)
        topFrame.pack()

        bottomFrame = tk.Frame(self,background='#FC9F4D')
        choices = dataSource.cityNames()
        choicesvar = tk.StringVar(value=choices)
        listbox = tk.Listbox(bottomFrame,listvariable=choicesvar,width=30)
        listbox.pack(pady=10)
        bottomFrame.pack(expand=True,fill='x')

        listbox.bind("<<ListboxSelect>>",self.user_selected)

    def user_selected(self,event):
        print("user selected")

def main():
    window = Window()    
    window.mainloop()

if __name__ == "__main__": 
    main()


