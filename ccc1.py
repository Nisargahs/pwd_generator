import tkinter as tk 
from collections import Counter 

def handle():
    msg="palindromable"
    userStr= entryBox.get()
    counts=Counter(userStr)
    print(counts)
    odd_count=len([v for v in counts.values() if v%2])
    if odd_count and((len(userStr)%2==0) or odd_count>1):
        msg="not palindromable"
    resultLabel.config(text=msg)
root = tk.Tk()
btn=tk.Button(root,text="click me!",fg="white",bg="red",command=handle)
entryBox=tk.Entry(root)
resultLabel=tk.Label(root,text="")
entryBox.grid(row=0,column=0)
btn.grid(row=0,column=1)
resultLabel.grid(row=1,column=0)
root.mainloop()