import psutil
import time
from tkinter import *

root = Tk()
root.title("CPU Usage")
root.geometry("550x40")
root.resizable(width=False, height=False)
text_label = Label(root, font=("calibri", 20), background="black", foreground="white")
bar_label = Label(root, font=("", 21), background="black", foreground="green")
pCent_label = Label(root, font=("calibri", 20), background="black", foreground="white")

cpu_use = psutil.cpu_percent()
text_label.config(text="CPU")


def update(scale=50):
    global cpu_use
    cpu_use = cpu_use / 100.0
    cpu_bar = "|" * int(cpu_use * scale) + " " * (scale - int(cpu_use * scale))
    string_cpu = f"|{cpu_bar}| "
    bar_label.config(text="")
    pCent_label.config(text=f"{(cpu_use * 100):.2f}")
    bar_label.config(text=string_cpu)
    bar_label.after(500, update)
    cpu_use = psutil.cpu_percent()


text_label.grid(column=0, row=0)
bar_label.grid(column=1, row=0)
pCent_label.grid(column=2, row=0)
update()
mainloop()