import tkinter as tk
from tkinter import ttk
import qrcode

def getQR(url):
    img = qrcode.make(url)
    img.show()

def window_init(w):
    w.title("QR")
    w.geometry("200x100")
    t1 = tk.StringVar()
    t1.set('')
    URL_text = tk.Entry(w, textvariable=t1)
    URL_text.pack(side='left')
    b=ttk.Button(w, text="生成", width=7, command=lambda :getQR(URL_text.get()))
    b.pack(side='right')
if __name__=="__main__":
    window=tk.Tk()
    window_init(window)
    window.mainloop()
