"""
There are 3 geometry managers in Tkinter:
-pack()
-grid()
-place()
"""

import tkinter as tk

root = tk.Tk()
root.geometry('350x200')
root.title('Pack Geo Mgr Demo')
root.configure(bg='#d9d9d9')

box1 = tk.Label(root, text='Box 1', bg='red', fg='white')
box1.pack(ipadx=20, ipady=20, padx=20, pady=20, expand=True, fill='both')

box2 = tk.Label(root, text='Box 2', bg='green', fg='white')
box2.pack(ipadx=20, ipady=20, padx=20, pady=20, expand=True, fill='both')

root.mainloop()