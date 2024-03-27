from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
check_label_text = ""
timer = ""

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #


def counter(new_count):
    count_minutes = new_count // 60
    count_seconds = new_count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(my_count, text=f"{count_minutes}:{count_seconds}")
    if new_count > 0:
        global timer
        timer = canvas.after(1000, counter, new_count - 1)
    else:
        start_clicked()
        global check_label_text, reps
        if reps % 2 == 0:
            check_label_text += "✔"
            check_label.config(text=check_label_text)


def start_clicked():
    global reps
    reps += 1

    if reps % 8 == 0:
        timer_label.config(fg=RED, text="Long Break")
        counter(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer_label.config(fg=PINK, text="Short Break")
        counter(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text="Work")
        counter(WORK_MIN * 60)


def end_clicked():
    global reps
    canvas.after_cancel(timer)
    reps = 0
    timer_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, 'normal'))
    canvas.itemconfig(my_count, text="00:00")
    check_label.config(text="")




window = Tk()
window.title("Pomodoro")
window.minsize(width=400, height=400)
window.config(bg=YELLOW, padx=50, pady=50)
count = 5

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
my_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=my_image)
my_count = canvas.create_text(100, 112, text=WORK_MIN, font=(FONT_NAME, 24, 'bold'), fill='white')
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, 'normal'))
timer_label.grid(row=0, column=1)
check_label = Label(text=check_label_text, bg=YELLOW, fg=GREEN)
check_label.grid(row=3, column=1)
start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start_clicked, highlightthickness=0)
start_button.grid(row=2, column=0)
end_button = Button(text="End", font=(FONT_NAME, 10, "bold"), command=end_clicked, highlightthickness=0)
end_button.grid(row=2, column=2)

window.mainloop()
