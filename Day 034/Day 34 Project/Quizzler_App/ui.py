from tkinter import * # type: ignore
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(
            text="Score: 0", 
            fg="white",
            font=("Arial", 14, "bold"),
            bg=THEME_COLOR
        )
        self.score_label.grid(row=0,column=1, sticky="e")
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(
            150,
            125,
            width=280,
            text = "Here goes the question", 
            font=("Arial", 16, "italic"), 
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        
        true_button_img = PhotoImage(file=r"images\true.png")
        self.true_button = Button(image=true_button_img, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(row=2,column=0)
        
        false_button_img = PhotoImage(file=r"images\false.png")
        self.false_button = Button(image=false_button_img, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(row=2,column=1)
        
        self.get_next_question()
        
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")          
    
    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))
        
    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))        
        
    def give_feedback(self, is_right:bool):
        if is_right:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000, self.get_next_question)
        
