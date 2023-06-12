from tkinter import *

def int_validator(char):
    return char.isdigit()

def main():
    window = Tk()

    window.title("Calculator")

    label1 = Label(window, text="Number A")
    label2 = Label(window, text="Number B")

    label1.grid(row=0, column=0)
    label2.grid(row=0, column=1)

    validation = window.register(int_validator)

    entry1 = Entry(window, bd=3, validate="key", validatecommand=(validation, '%S'))
    entry2 = Entry(window, bd=3, validate="key", validatecommand=(validation, '%S'))

    entry1.grid(row=1, column=0)
    entry2.grid(row=1, column=1)

    window.mainloop()

if __name__ == "__main__":
    main()