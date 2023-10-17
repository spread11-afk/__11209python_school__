'''
這是說明,學習Canvas
'''
import tkinter as tk
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter.simpledialog import Dialog
from tkinter.messagebox import showinfo


class Window(tk.Tk):
    def __init__(self, **kwargs,) -> None:
        super().__init__(**kwargs)
        self.title('Image')
        #self.geometry("300x250")
        

class MyFrame(ttk.LabelFrame):
    def __init__(self, master,title,**kwargs) -> None:
        super().__init__(master,text=title,**kwargs)
        self.pack(expand=1,fill='both',pady=10)

        self.tree = ttk.Treeview(self,columns=['#1','#2','#3','#4','#5','#6','#7'],show='headings')
        self.tree.heading('#1',text='第一欄')
        self.tree.heading('#2',text='第二欄')
        self.tree.heading('#3',text='第三欄')
        self.tree.heading('#4',text='第四欄')
        self.tree.heading('#5',text='第五欄')
        self.tree.heading('#6',text='第六欄')
        self.tree.heading('#7',text='第七欄')
        self.tree.pack()
        
        
        contacts = []
        for n in range(1,100):
            contacts.append([f'first{n}',f'last{n}',f'email{n}:exmple.com'])

        for contact in contacts:
            self.tree.insert('',tk.END,value=contact)
        
        
        
        self.tree.bind('<<TreeviewSelect>>',self.item_selected)
        self.tree.grid(row=0, column=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

    
    def item_selected(self,event):
        item_id = self.tree.selection()[0]
        item_dict = self.tree.item(item_id)
        print(item_dict['values'])

        



    def choised(self):
        print(self.aligement.get())


def main():
    window = Window()
    myFrame = MyFrame(window,'對齊方式')
    window.mainloop()




if __name__ == '__main__':
    main()

