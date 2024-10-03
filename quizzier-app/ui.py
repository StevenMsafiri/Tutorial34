from tkinter import *
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.config(bg=THEME_COLOR)
        self.window.title("Quizzler")

        self.label_score = Label(text="Score:0", bg=THEME_COLOR, fg="white")
        self.label_score.grid(column=1, row=0, padx=20, pady=20)

        self.white_space = Canvas(width=300, height=250, background="white")
        self.white_space.grid(column=0, row=1, columnspan=2, padx=20, pady=30)

        self.q_text = self.white_space.create_text(150, 125, text="Question text", font=("Arial", 20, "italic"), fill=THEME_COLOR)

        right = PhotoImage(file="images/true.png")
        wrong = PhotoImage(file="images/false.png")

        self.right_but = Button(image=right, highlightthickness=0)
        self.right_but.grid(column=0, row=2, padx=20, pady=20)

        self.wrong_but = Button(image=wrong, highlightthickness=0)
        self.wrong_but.grid(column=1, row=2, padx=20, pady=20)

        self.window.mainloop()
