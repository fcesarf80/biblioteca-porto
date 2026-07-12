import tkinter as tk
from tkinter import ttk

root = tk.Tk()

print(ttk.Style().theme_names())
print(ttk.Style().theme_use())

root.mainloop()