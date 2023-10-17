import dataSource
import tkinter as tk
from tkinter import ttk


class Window(tk.Tk):
    def __init__(self,**kwargs) -> None:
        super().__init__(**kwargs)        
        self.title("鄉鎮人口")        
        self.configure(background='#86473F')        
        
        topFrame = tk.Frame(self,background='#CB1B45')        
        label = ttk.Label(topFrame,text="鄉鎮人口",
        font=("arial",30,"bold"))
        label.pack(padx=10,pady=10)
        topFrame.pack()
        
        bottomFrame = tk.Frame(self,
        background='#FC9F4D')  
        choices = dataSource.cityNames()
        choicesvar = tk.StringVar(value=choices)
        self.listbox = tk.Listbox(bottomFrame,listvariable=choicesvar,width=0,justify="center",font=('30'),relief="solid")
        self.listbox.pack(pady=5)
        bottomFrame.pack(expand=True,fill='x')
        self.listbox.bind("<<ListboxSelect>>",self.user_selected)
        

        resultFrame = tk.Frame(self)
        tk.Label(resultFrame,text="年度:",relief='solid').grid(column=0,row=0,sticky="W",pady=5)
        tk.Label(resultFrame,text="地區:",relief='solid').grid(column=0,row=1,sticky="W",pady=5)
        tk.Label(resultFrame,text="人口:").grid(column=0,row=2,sticky="W",pady=5)
        tk.Label(resultFrame,text="土地面積:").grid(column=0,row=3,sticky="W",pady=5)
        tk.Label(resultFrame,text="人口密度:").grid(column=0,row=4,sticky="W",pady=5)
        
        self.yearVar = tk.StringVar()
        tk.Label(resultFrame,textvariable=self.yearVar).grid(column=1,row=0,sticky="W",pady=5)
        self.cityVar = tk.StringVar()
        tk.Label(resultFrame,textvariable=self.cityVar).grid(column=1,row=1,sticky="W",pady=5)
        self.population = tk.StringVar()
        tk.Label(resultFrame,textvariable=self.population).grid(column=1,row=2,sticky="W",pady=5)
        self.areaVar = tk.StringVar()
        tk.Label(resultFrame,textvariable=self.areaVar).grid(column=1,row=3,sticky="W",pady=5)
        self.densityVar = tk.StringVar()
        tk.Label(resultFrame,textvariable=self.densityVar).grid(column=1,row=4,sticky="W",pady=5)
        
        
        
        resultFrame.pack()

    def user_selected(self,event):
        selectedIndex = self.listbox.curselection()[0]
        cityName = self.listbox.get(selectedIndex)
        #print(dataSource.info(cityName))
        datalist = dataSource.info(cityName)
        self.yearVar.set(datalist[0]) 
        self.cityVar.set(datalist[1]) 
        self.population.set(datalist[2]) 
        self.areaVar.set(datalist[3]) 
        self.densityVar.set(datalist[4]) 


def main():
    window = Window()    
    window.mainloop()


if __name__ == "__main__": 
    main()


