'''
這是說明,學習Canvas
'''
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk


class Window(tk.Tk):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.geometry("2000x2000")
        self.title('Lines')
        self.configure(background='red')

class MyFrame(tk.Frame):
    def __init__(self, master,**kwargs) -> None:
        super().__init__(master,**kwargs)
        self.configure(background='blue')
        canvas = tk.Canvas(self)
        canvas.create_line(15,30,200,30)
        canvas.create_line(300,35,300,200,dash = (4,2))
        self.img = Image.open('221009gallery.jpg')
        self.bot = ImageTk.PhotoImage(self.img)
        botLable = tk.Label(self,image=self.bot)
        botLable.pack()
        self.pack(expand=1,fill='both')




def main():
    window = Window()
    myFrame=MyFrame(window)
    window.mainloop()

if __name__ == '__main__':
    main()