'''
這是說明,學習Canvas
'''
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk


class Window(tk.Tk):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.geometry("1902x1070")
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
        self.img = Image.open('221009gallery.jpg')
        self.bot = ImageTk.PhotoImage(self.img)
        canvas = tk.Canvas(self,width=1902,height=1070)
        canvas.create_image(24,24,image=self.bot,anchor=tk.CENTER)
        canvas.pack()
        self.pack(expand=1,fill='both')


def main():
    window = Window()
    myFrame=MyFrame(window)
    window.mainloop()

if __name__ == '__main__':
    main()