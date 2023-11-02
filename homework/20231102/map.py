import tkinter as tk
import tkintermapview as tkmap
from PIL import Image, ImageTk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.thumbnails = {}

        map_widget = tkmap.TkinterMapView(self, width=800, height=600, corner_radius=0)
        map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        marker_1 = map_widget.set_position(25.257887730617984, 121.49401660340506, marker=True)
        map_widget.set_zoom(13)
        marker_1.set_text("三芝區")

        marker_2 = map_widget.set_marker(25.2604340447434, 121.50276763806208, text="老地方")
        marker_2.data = {'a': 15, 'b': '紀念館', 'image_path': 'A.jpg'}

        # 使用bind方法绑定点击事件
        marker_2.bind("<Button-1>", self.show_thumbnail)

    def show_thumbnail(self, event):
        marker = event.widget
        data = marker.data

        if 'image_path' in data:
            image_path = data['image_path']
            if image_path in self.thumbnails:
                thumbnail = self.thumbnails[image_path]
            else:
                image = Image.open(image_path)
                image.thumbnail((100, 100))
                thumbnail = ImageTk.PhotoImage(image)

                self.thumbnails[image_path] = thumbnail

            popup = tk.Toplevel()
            label = tk.Label(popup, image=thumbnail)
            label.pack()
            popup.mainloop()

if __name__ == "__main__":
    app = Window()
    app.mainloop()
