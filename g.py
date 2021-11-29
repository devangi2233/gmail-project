from tkinter import *
import calendar
def submit():
    win=Tk()
    win.geometry("600x690")
    win.title("Calendar of the year")
    win.config(bg="Salmon")
    year_cal = int(entry_value.get())
    cal = calendar.calendar(year_cal)
    calYear = Label(win,text = cal, font="lucida 10 bold").place(x=60,y=40)
    win.mainloop()
    
if __name__ == '__main__' :
    window=Tk()
    window.geometry("600x300")
    window.title("Calendar")
    window.config(bg="yellowgreen")
    label = Label(window,text="Calendar Of The Year",font="licida 15 bold",fg="red",bg="yellowgreen").place(x=150,y=15)
    label1 = Label(window,text="Enter Year",font="licida 12 bold",fg="red",bg="yellowgreen").place(x=190,y=55)
    entry_value = StringVar()
    entry = Entry(window,textvariable=entry_value,bd=6,relief=SUNKEN)
    entry.place(x=185,y=90)
    button = Button(window,text="Display Calendar",font="licida 10 bold",padx=10,pady=10,bg="red",command=submit)
    button.place(x=185,y=130)
    window.mainloop()