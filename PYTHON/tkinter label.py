import tkinter as tk 
r = tk.Tk()
r.title("abhishek")
button = tk.Button(r,text="stop",width=25,command=r.destroy)
button.pack()
r.mainloop()