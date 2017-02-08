import time
from tkinter import Label, StringVar, Tk, font

ncycles = 1000
ndigits = len(str(ncycles)) - 1
timeout = 10 # milliseconds
root = Tk()
font.nametofont('TkDefaultFont').configure(size=10) # big
text = StringVar()
text.set('0'*ndigits)
Label(root, textvariable=text).pack()

# center the window
root.update_idletasks() # necessary to update w, h
w, h = root.winfo_width(), root.winfo_height()
x = root.winfo_screenwidth() // 2  - w // 2
y = root.winfo_screenheight() // 2 - h // 2
root.geometry('{}x{}+{}+{}'.format(w, h, x, y))

def timer():
    return round(time.perf_counter() * 1000)

def update_timer(i=0):
    if i >= ncycles:
        root.destroy() # exit
    else:
        root.after(timeout - timer() % timeout, update_timer, i+1)
        text.set('{:0{width}d}'.format(i, width=ndigits))

root.after(timeout - timer() % timeout, update_timer) # start timer
root.mainloop()