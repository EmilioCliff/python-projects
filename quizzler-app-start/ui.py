from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizUserInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        # Images
        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")
        # Canvas
        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        # Score Label
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        # Question Text
        self.question = self.canvas.create_text(150, 125, text="", width=280, fill=THEME_COLOR, font=("Arial", 20, "italic"))
        # Buttons
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.right_answer)
        self.true_button.grid(row=3, column=0)
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.wrong_answer)
        self.false_button.grid(row=3, column=1)
        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question)
        else:
            self.canvas.itemconfig(self.question, text="You have come to the end of the questions")
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)

    def right_answer(self):
        self.check_answer(self.quiz.check_answer("True"))

    def wrong_answer(self):
        self.check_answer(self.quiz.check_answer("False"))

    def check_answer(self, answer_provided):
        if answer_provided:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)
