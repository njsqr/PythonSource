"""
@author
"""

# import tkinter as tk    # 导入tkinter 模块并创建一个别名tk
#
# win = tk.Tk()              # 实例化tk.TK
# win.title("Python GUI")    # 添加标题
# win.resizable(0, 0)        # 禁止调整窗口大小
# win.mainloop()             # 当调用mainloop()时,窗口才会显示出来

# This program displays an empty window.
# import tkinter
# def main():
#     main_window = tkinter.Tk()
#     main_window.mainloop()
# main()

from tkinter import *
def huabu():
    hua=Canvas(win,width=500,height=500)

win=Tk()
win.title=('huabu')
win.geometry('300x200')
win.resizable(1,1)
hu=Button(win,text='start',command=huabu,activeforeground='white',activebackground='red')
hu.pack(side='bottom')
win.mainloop()