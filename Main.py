import tkinter as tk
import threading

wind = tk.Tk()
wind.geometry('800x400')
wind.title('SocketTools')

# 标题栏为切换UDP和TCP和其他设置的主区域
f_title = tk.Frame(wind)
f_title.pack()

b_udp=tk.Button(f_title,text='UDP')
b_udp.grid()

# UDP的主框架
f_UDP = tk.Frame(wind)
f_UDP.pack()













# 程序主入口
wind.mainloop()
