from tkinter import *
root=Tk()
def hello():
  print("hello World")
button1=Button(root,text="Click Me",commnad=hello)
button1.pack()
root.mainloop()
