'''
這是說明,學習Canvas
'''
import tkinter as tk
from tkinter import ttk
frome PIL import image


class Window(tk.Tk):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.geometry("400x200+300+300")
        self.title('Lines')
        self.configure(background='red')

class MyFrame(tk.Frame):
    def __init__(self, master,**kwargs) -> None:
        super().__init__(master,**kwargs)
        self.configure(background='blue')
        canvas = tk.Canvas(self)
        canvas.create_line(15,30,200,30)
        canvas.create_line(300,35,300,200,dash = (4,2))
        canvas.create_line(55,85,155,85,105,180,55,85)
        canvas.pack(expand=1,fill='both')
        self.img = image.open
        self.pack(expand=1,fill='both')


def main():
    window = Window()
    myFrame=MyFrame(window)
    window.mainloop()

if __name__ == '__main__':
    main()