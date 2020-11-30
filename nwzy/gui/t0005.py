"""
@author
"""
from tkinter import*
tk=Tk()
canvas=Canvas(tk,width=500,height=500)
canvas.pack()
def draw():
    import sys
    print('width')
    a=int(sys.stdin.readline())
    print('height')
    b=int(sys.stdin.readline())
    import random
    a1=random.randint(0,100)
    b1=random.randint(0,100)
    canvas.create_rectangle(a1,b1,a1+a,b1+b)
btn=Button(tk,text='draw one rectangle',command=draw)
btn.pack()
tk.mainloop()
