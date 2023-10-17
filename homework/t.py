'''
學習Canvas
'''
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.simpledialog import Dialog

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)        
        self.title("Image")
        #self.geometry("300x250")
        #self.configure(background='#E79460')



    
    

class MyFrame(tk.LabelFrame):
    def __init__(self,master,title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        self.pack(expand=1,fill='both',padx=10,pady=10)

        self.tree = ttk.Treeview(self,columns=['#1', '#2', '#3'],show="headings")
        self.tree.heading('#1', text="第一欄")
        self.tree.heading('#2', text="第二欄")
        self.tree.heading('#3', text="第三欄")

        contacts = []
        for n in range(1,100):
            contacts.append([f'first {n}',f'last {n}',f'email{n}:example.com'])

        for contact in contacts:
            self.tree.insert('',tk.END,value=contact)
        
        self.tree.pack()

        self.tree.bind('<<TreeviewSelect>>',self.item_selected)


    def item_selected(self,event):
        item_id = self.tree.selection()[0]
        item_dict = self.tree.item(item_id)
        values=item_dict['values']
        class GetPassword(Dialog):
            def body(self, master):
                self.title("Enter New Password")

                tk.Label(master, text='Old Password:').grid(row=0, sticky=tk.W)
                tk.Label(master, text='New Password:').grid(row=1, sticky=tk.W)
                tk.Label(master, text='Enter New Password Again:').grid(row=2, sticky=tk.W)

                tk.Label(master, text=values[0]).grid(row=0,column=1, sticky=tk.W)
        answer = GetPassword(self)
       
        

        
    


def main():    
    window = Window()
    myFrame = MyFrame(window,"對齊方式")    
    window.mainloop()

if __name__ == "__main__":
    main()