from tkinter import *
from tkinter import ttk
root = Tk()
root.title("app-template")
root.geometry("400x300")
frm = ttk.Frame(root, padding=10)
frm.pack()
ttk.Label(frm, text="app-template!").pack(side="top", pady="0",)
ttk.Button(frm, text="Quit", command=root.destroy).pack(side="left", pady="0",)
root.mainloop()
