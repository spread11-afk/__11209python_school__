import tkinter as tk
from tkinter import ttk
import sqlite3

def search_sitename(word: str) -> list[tuple]:
    conn = sqlite3.connect("youbike.db")
    cursor = conn.cursor()
    sql = '''
    SELECT 站點名稱,MAX(更新時間) AS 更新時間,行政區,地址,總車輛數,可借,可還
    FROM 台北市youbike
    WHERE 站點名稱 LIKE ?
    GROUP BY 站點名稱
    '''
    cursor.execute(sql, [f'%{word}%'])
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def search_button_clicked():
    keyword = entry.get()
    results = search_sitename(keyword)
    listbox.delete(0, tk.END)
    for result in results:
        listbox.insert(tk.END, result)

app = tk.Tk()
app.title("YouBike站点搜索")

# 创建ttk.Entry小部件
entry = ttk.Entry(app)
entry.pack(padx=10, pady=10)

# 创建一个按钮来执行搜索
search_button = ttk.Button(app, text="搜索", command=search_button_clicked)
search_button.pack(padx=10, pady=10)

# 创建一个列表框来显示搜索结果
listbox = tk.Listbox(app)
listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

app.mainloop()
