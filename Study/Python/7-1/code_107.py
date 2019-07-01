from tkinter import *
from tkinter import messagebox

def clickImage(event):
    messagebox.showinfo("마우스", "개에서 마우스 클릭됨")


window = Tk()
window.geometry("400x400")

photo = PhotoImage(file = "image/dog.gif")
label1 = Label(window, image = photo)

label1.bind("<Button>", clickImage)

label1.pack(expand =1,anchor = CENTER)
window.mainloop()
