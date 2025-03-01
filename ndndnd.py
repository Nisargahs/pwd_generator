import tkinter as tk
count=0
def handle():
    global count
    count += 1
    msg=f"clicked {count} times"
    label.config(text=msg)
root=tk.Tk()
btn=tk.Button(root,text="click me",fg="white",bg="red",command=handle)
btn.pack()
label=tk.Label(root,text="count=0")

label.pack()
root.mainloop()