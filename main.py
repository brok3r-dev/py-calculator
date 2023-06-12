from tkinter import *

def int_validator(char):
    return char.isdigit()

window = Tk()
label1 = Label(window, text="Number A")
label2 = Label(window, text="Number B")
validation = window.register(int_validator)
entry1 = Entry(window, bd=3, validate="key", validatecommand=(validation, '%S'))
entry2 = Entry(window, bd=3, validate="key", validatecommand=(validation, '%S'))
entry3 = Entry(window, bd=3)

def addition():
    entry3.delete(0, END)
    entry3.insert(INSERT, int(entry1.get()) + int(entry2.get()))

def subtraction():
    entry3.delete(0, END)
    entry3.insert(INSERT, int(entry1.get()) - int(entry2.get()))

def multiplication():
    entry3.delete(0, END)
    entry3.insert(INSERT, int(entry1.get()) * int(entry2.get()))

def division():
    entry3.delete(0, END)
    entry3.insert(INSERT, int(entry1.get()) / int(entry2.get()))

button1 = Button(window, text="+", command=addition)
button2 = Button(window, text="-", command=subtraction)
button3 = Button(window, text="X", command=multiplication)
button4 = Button(window, text="/", command=division)

def main():
    window.title("Calculator")

    label1.grid(row=0, column=0)
    label2.grid(row=0, column=2)

    entry1.grid(row=1, column=0)
    entry2.grid(row=1, column=2)

    button1.grid(row=2, column=0)
    button2.grid(row=2, column=2)
    button3.grid(row=3, column=0)
    button4.grid(row=3, column=2)

    entry3.grid(row=4, column=1)

    window.mainloop()



if __name__ == "__main__":
    main()