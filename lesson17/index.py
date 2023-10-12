import dataSource,tkinter as tk,tkinter.ttk




def main():
    window = tk.Tk()
    window.title("第一個視窗")
    label = tk.Label(window,text="Hi Tkinter",width=400,height=400,font=("arial",100,"bold"))
    label.pack(padx=10,pady=50)
    
    
    
    
    window.mainloop()

if __name__ == "__main__": 
    main()
