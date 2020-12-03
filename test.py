from tkinter import *
import baby

window = Tk()

window.geometry('500x500')


window.title("Baby name generator")

lbl = Label(window, text="Congratulations on the birth of your baby!", font=("Arial Bold", 25))

lbl.grid(column=5, row=0)

def clicked():

    baby.start()

btn = Button(window, text="Begin", command=clicked)

btn.grid(column=3, row=4)


window.mainloop()