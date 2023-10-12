import tkinter as tk,tkinter.ttk
class Window(tk.Tk):
    def __init__(self,**kwargs) -> None:
        super().__init__(**kwargs)
        self.title("第一個視窗")
        label = tk.Label(self,text="Hi Tkinter",width=400,height=400,font=("arial",100,"bold"))
        label.pack(padx=10,pady=50)

def main():
    window = Window()    
    window.mainloop()

if __name__ == "__main__": 
    main()


