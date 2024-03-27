from tkinter import *
window = Tk()
window.title("Mile to Kilometer")
window.minsize(width=20, height=20)
window.config(pady=20, padx=20)

my_label = Label(text="miles")
my_label.grid(row=0, column=3)

new_label = Label(text="is equal to ")
new_label.grid(row=1, column=0)

result = Label(text=0)
result.grid(row=1, column=2)
result.config(padx=30, pady=30)

another_label = Label(text="Km")
another_label.grid(row=1, column=3)


def button_clicked():
    new_text = int(user_input.get())
    new_text *= 1.609
    result.config(text=round(new_text))


button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=2)

user_input = Entry(width=5)
user_input.grid(row=0, column=2)

window.mainloop()
