from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.config(bg=THEME_COLOR)
        self.window.title("Quizzler")

        self.label_score = Label(text="Score:0", bg=THEME_COLOR, fg="white")
        self.label_score.grid(column=1, row=0, padx=20, pady=20)

        self.white_space = Canvas(width=300, height=250, background="white")
        self.white_space.grid(column=0, row=1, columnspan=2, padx=20, pady=30)

        self.q_text = self.white_space.create_text(150, 125, text="Question text", font=("Arial", 15, "italic"),
                                                   fill=THEME_COLOR, width=280)

        right = PhotoImage(file="images/true.png")
        wrong = PhotoImage(file="images/false.png")

        self.right_but = Button(image=right, highlightthickness=0, command=self.correct_answer)
        self.right_but.grid(column=0, row=2, padx=20, pady=20)

        self.wrong_but = Button(image=wrong, highlightthickness=0, command=self.wrong_answer)
        self.wrong_but.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.white_space.config(bg="white")
            self.label_score.config(text=f"{self.quiz.score}")
            question_text = self.quiz.next_question()
            self.white_space.itemconfig(self.q_text, text=question_text)

        else:
            self.white_space.config(bg="white")
            self.label_score.config(text=f"{self.quiz.score}")
            question_text = "You've completed the quiz"
            self.white_space.itemconfig(self.q_text, text=question_text)
            self.right_but.config(state="disabled")
            self.wrong_but.config(state="disabled")

    def correct_answer(self):
        user_answer = "True"
        is_right = self.quiz.check_answer(user_answer)
        self.give_feedback(is_right)

    def wrong_answer(self):
        user_answer = "False"
        is_right = self.quiz.check_answer(user_answer)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.white_space.config(bg="green")
            self.window.after(1000, self.get_next_question)

        else:
            self.white_space.config(bg="red")
            self.window.after(1000, self.get_next_question)




