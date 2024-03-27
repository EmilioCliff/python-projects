from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = []

try:
    data_read = pandas.read_csv("data/to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/spanish_words.csv")
    data_list = [[row['Spanish'], row['English']] for (index, row) in original_data.iterrows()]
else:
    data_list = [[row['Spanish'], row['English']] for (index, row) in data_read.iterrows()]


def known():
    data_list.remove(current_card)
    to_learn = pandas.DataFrame(data_list, columns=["Spanish", "English"])
    to_learn.to_csv("data/to_learn.csv", index=False)
    unknown()


def unknown():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(data_list)
    my_canvas.itemconfig(flip, image=card_front_image)
    my_canvas.itemconfig(title, text="Spanish", fill="black")
    my_canvas.itemconfig(text, text=current_card[0], fill="black")
    timer = window.after(5000, create_new_flashcard)


def create_new_flashcard():
    my_canvas.itemconfig(flip, image=card_back_image)
    my_canvas.itemconfig(title, text="English", fill="white")
    my_canvas.itemconfig(text, text=current_card[1], fill="white")


window = Tk()
window.title("Translator game")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

my_canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
my_canvas.grid(row=0, column=0, columnspan=2)

# Images
card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")
flip = my_canvas.create_image(400, 265, image=card_front_image)

right_button_image = PhotoImage(file="images/right.png")
wrong_button_image = PhotoImage(file="images/wrong.png")

# Texts
title = my_canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
text = my_canvas.create_text(400, 253, text="", font=("Ariel", 40, "bold"))

# Buttons
right_button = Button(image=right_button_image, highlightthickness=0, width=100, height=100, command=known)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong_button_image, highlightthickness=0, width=100, height=100, command=unknown)
wrong_button.grid(row=1, column=0)
timer = my_canvas.after(5000, create_new_flashcard)
unknown()

window.mainloop()
