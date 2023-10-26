import tkinter as tk
from tkinter import ttk


class Window(tk.Tk):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        


def main():
    window = Window()
    window.title('youbike_ver2.0')
    window.geometry('600x300')
    window.resizable(width=False,height=False)
    window.mainloop()


if __name__ == '__main__':
    main()