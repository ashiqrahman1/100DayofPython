from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.sc = 0
        self.window = Tk()
        self.window.title("Quiz UI")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.label = Label(
            text=f"Score : 0", bg=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(
            150, 125, width=260, text="Some Question", fill=THEME_COLOR, font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true_img = PhotoImage(file='images/true.png')
        self.true_btn = Button(
            image=true_img, highlightthickness=0, command=self.true_press)
        self.true_btn.grid(row=2, column=0)
        false_img = PhotoImage(file='images/false.png')
        self.false_btn = Button(
            image=false_img, highlightthickness=0, command=self.false_press)
        self.false_btn.grid(row=2, column=1)
        self.current_q = self.getNextQuestion()
        self.window.mainloop()

    def getNextQuestion(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.label.config(text=f"Score : {self.sc}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(
                self.question, text=f"Quiz is Completed Your Score is {self.sc}")
            self.true_btn.config(state=DISABLED)
            self.false_btn.config(state=DISABLED)

    def true_press(self):
        print(self.quiz.check_answer("True"))
        self.feedback(self.quiz.check_answer("True"))

    def false_press(self):
        print(self.quiz.check_answer("False"))
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, status):
        if status:
            self.canvas.configure(bg="green")
            self.sc += 1
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.getNextQuestion)
