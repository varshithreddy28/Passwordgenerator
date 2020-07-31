import tkinter as tk
from tkinter import ttk
import math
import random
import string

try:
    from ctypes import windll
    windll.shcore.SetProcessDpAwareness(1)
except:
    pass
def passwo(*args):
    a = random.randint(0,11)
    l='abcdefghijklmnopqrstuvwxyz'
    lu=l.upper()
    ch='!@#$%^&*-+'
    num=str(a)
    total=num+l+lu+ch
    al=''.join(random.choice(total) for i in range(8) )
    lower=random.choice(l)
    upper=random.choice(lu)
    charecter=random.choice(ch)
    final=num+lower+upper+charecter+al
    passw.set(final)

root=tk.Tk()

root.title('Password Generator')
label=ttk.Label(root,text='Password Generator')
label.config(font=('Algerian',15))
label.pack()
passw=tk.StringVar()
entry=tk.Entry(root,textvariable=passw)
entry.pack()
button=tk.Button(root,text='Genetate Password',command=passwo,fg='black',bg='lightblue')
button.pack(side='left')
bquit=tk.Button(root,text='Exit',command=root.destroy,fg='black',bg='lightblue',height=1, width=16)
bquit.pack(side='right')

root.mainloop()