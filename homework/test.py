import tkinter as tk
import csv
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
        self.tree.heading('#1',text='交易日期')
        self.tree.heading('#2',text='開盤價')
        self.tree.heading('#3',text='最高價')
        self.tree.heading('#4',text='最低價')
        self.tree.heading('#5',text='收盤價')
        self.tree.heading('#6',text='經過調整的收盤價')
        self.tree.heading('#7',text='成交量')
        self.tree.pack()

        self.tree.grid(row=0, column=0, sticky='nsew')

        
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        f = open('tgd.csv','r')
        csvreader = csv.reader(f)
        next(csvreader)
        final_list = list(csvreader)
        

        for contact in final_list:
            self.tree.insert('',tk.END,value=contact)
        
        

        self.tree.bind('<<TreeviewSelect>>',self.item_selected)


    def item_selected(self,event):
        item_id = self.tree.selection()[0]
        item_dict = self.tree.item(item_id)
        values=item_dict['values']
        class GetPassword(Dialog):
            def body(self, master):
                self.title("Enter New Password")

                tk.Label(master, text='交　 　易　　　日：').grid(row=0, sticky=tk.W)
                tk.Label(master, text='開　 　盤　　　價：').grid(row=1, sticky=tk.W)
                tk.Label(master, text='最　 　高　　　價：').grid(row=2, sticky=tk.W)
                tk.Label(master, text='最　 　低　　　價：').grid(row=3, sticky=tk.W)
                tk.Label(master, text='收　 　盤　　　價：').grid(row=4, sticky=tk.W)
                tk.Label(master, text='經過調整的收盤價：').grid(row=5, sticky=tk.W)
                tk.Label(master, text='成　 　交　　　量：').grid(row=6, sticky=tk.W)

                tk.Label(master, text=values[0]).grid(row=0,column=1, sticky=tk.W)
                tk.Label(master, text=values[1]).grid(row=1,column=1, sticky=tk.W)
                tk.Label(master, text=values[2]).grid(row=2,column=1, sticky=tk.W)
                tk.Label(master, text=values[3]).grid(row=3,column=1, sticky=tk.W)
                tk.Label(master, text=values[4]).grid(row=4,column=1, sticky=tk.W)
                tk.Label(master, text=values[5]).grid(row=5,column=1, sticky=tk.W)
                tk.Label(master, text=values[6]).grid(row=6,column=1, sticky=tk.W)
        answer = GetPassword(self)

 



    def choised(self):
        print(self.aligement.get())


def main():
    window = Window()
    myFrame = MyFrame(window,'對齊方式')
    window.mainloop()


if __name__ == '__main__':
    main()


