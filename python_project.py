import tkinter as tk

def close_window(event):
    root.destroy()

root = tk.Tk()
root.geometry("400x300")  
root.configure(bg="black")  


canvas = tk.Canvas(root, bg="black", width=400, height=300)
canvas.pack()

circle_button = canvas.create_oval(5, 5, 30, 30, fill="red")

canvas.tag_bind(circle_button, "<Button-1>", close_window)

root.mainloop()
