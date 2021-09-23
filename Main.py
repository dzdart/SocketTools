import tkinter as tk
import threading

wind = tk.Tk()
wind.geometry('800x400')
wind.title('SocketTools')
paibu = tk.E
# 标题栏为切换UDP和TCP和其他设置的主区域
f_title = tk.Frame(wind)
f_title.pack(side='top', fill='both')
top_button_width = 180
top_button_height = 1
top_button = []
b_udp = tk.Button(f_title, text='UDP')
b_udp.configure(command=lambda: switchSocketButton(b_udp))
top_button.append(b_udp)
b_udp.grid(row=1, column=1, padx=1, pady=1)

b_tcp = tk.Button(f_title, text='tcp')
b_tcp.configure(command=lambda: switchSocketButton(b_tcp))
top_button.append(b_tcp)
b_tcp.grid(row=1, column=2, padx=1, pady=1)


def switchSocketButton(b):
    for item in top_button:
        if b == item:
            item.configure(state='disable', fg='Green')
        else:
            item.configure(state='active', fg='Black')


# UDP的主框架
f_UDP = tk.Frame(wind)
f_UDP.pack(side='top', fill='both')

# ip输入框，端口号
l_udp_ip = tk.Label(f_UDP, text='IP地址', width=10)
e_udp_ip = tk.Entry(f_UDP, show=None, width=10)
e_udp_ip.insert('end', '127.0.0.1')

e_udp_port = tk.Entry(f_UDP, show=None, width=10)
l_udp_port = tk.Label(f_UDP, text='端口', width=10)
e_udp_port.insert('end', '2333')

udp_mod = tk.StringVar()


def Rb_var():
    print(udp_mod.get())


l_udp_mode = tk.Label(f_UDP, text='发送模式', width=10)
Rb_udp_mod1 = tk.Radiobutton(f_UDP, text='单次', variable=udp_mod, value='A', command=Rb_var, width=10)
Rb_udp_mod2 = tk.Radiobutton(f_UDP, text='循环', variable=udp_mod, value='B', command=Rb_var, width=10)
udp_mod.set("A")

l_udp_mode_number = tk.Label(f_UDP, text='循环次数', width=10)
e_udp_mode_number = tk.Entry(f_UDP, width=10)
e_udp_mode_number.insert('end', '5')
l_udp_mode_delay = tk.Label(f_UDP, text='循环间隔', width=10)
e_udp_mode_delay = tk.Entry(f_UDP, width=10)
e_udp_mode_delay.insert('end', '1')

l_udp_ip.grid(row=1, column=1, sticky=paibu)
e_udp_ip.grid(row=1, column=2, sticky=paibu)
l_udp_port.grid(row=1, column=3, sticky=paibu)
e_udp_port.grid(row=1, column=4, sticky=tk.W)

l_udp_mode.grid(row=2, column=1, sticky=paibu)
Rb_udp_mod1.grid(row=2, column=2, sticky=paibu)
Rb_udp_mod2.grid(row=2, column=3, sticky=paibu)

l_udp_mode_number.grid(row=2, column=4, sticky=paibu)
e_udp_mode_number.grid(row=2, column=5, sticky=paibu)
l_udp_mode_delay.grid(row=2, column=6, sticky=paibu)
e_udp_mode_delay.grid(row=2, column=7, sticky=paibu)

# 程序主入口
wind.mainloop()
