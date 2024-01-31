from tkinter import ttk
import tkinter as tk
import multiprocessing as mp
import time

def proccess():
    time.sleep(10)

def sleep():
    p = mp.Process(target=proccess)
    p.start()
    p.join()
    time.sleep(10)
    lab['text'] = "After run"
    
if __name__=='__main__':
    root = tk.Tk()
    root.configure(bg='blue')
    root.geometry('500x500')
        
    btn = ttk.Button(root, text='run', command=sleep)
    btn.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    lab = ttk.Label(root, text="Before run")
    lab.place(relx=0.5, rely=0.6, anchor=tk.CENTER)


root.mainloop()