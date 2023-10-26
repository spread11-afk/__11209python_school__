import tkinter as tk
from tkinter import ttk
import datasource
from tkinter import messagebox


class Window(tk.Tk):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        try:
            datasource.download_youbike_data()
        except Exception:
            messagebox.showerror('Error','關閉視窗\n稍後再試')
            self.destroy()


        


def main():
    window = Window()
    window.title('youbike_ver2.0')
    window.geometry('600x300')
    window.resizable(width=False,height=False)
    window.mainloop()


if __name__ == '__main__':
    main()