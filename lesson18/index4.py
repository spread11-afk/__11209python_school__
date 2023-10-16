'''
這是說明,學習Canvas
'''
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk


class Window(tk.Tk):
    def __init__(self, **kwargs,) -> None:
        super().__init__(**kwargs)
        self.title('Image')
        #self.geometry("300x250")
        

class MyFrame(ttk.LabelFrame):
    def __init__(self, master,title,**kwargs) -> None:
        super().__init__(master,text=title,**kwargs)
        self.pack(expand=1,fill='both',pady=10)
    
        #標題
        headind=ttk.Label(self,text='會員登入',font=('Arial',15,'bold'),foreground='red')
        headind.grid(column=0,row=0,columnspan=2,padx=(20,0))
    
        username_label = ttk.Label(self,text='使用者名稱')
        username_label.grid(column=0,row=1,pady=20,padx=(10,1))

        username_entry = ttk.Entry(self)
        username_entry.grid(column=1,row=1,padx=(0,10))

        password_label = ttk.Label(self,text='密　　　碼')
        password_label.grid(column=0,row=2,pady=20,padx=(10,1))

        password_entry = ttk.Entry(self,show='*')
        password_entry.grid(column=1,row=2,padx=(0,10))

        login_button = ttk.Button(self,text='登入')
        login_button.grid(column=1,row=3,padx=(0,10),sticky='E')


    def choised(self):
        print(self.aligement.get())


def main():
    window = Window()
    myFrame = MyFrame(window,'對齊方式')
    window.mainloop()

if __name__ == '__main__':
    main()