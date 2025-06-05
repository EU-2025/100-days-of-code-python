class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0    
        self.question_bank = question_bank
        self.score = 0

    def still_has_questions(self):
        return len(self.question_bank) > self.question_number 

    def next_question(self):
        current_question = self.question_bank[self.question_number]
        user_answer = input(f"Q.{self.question_number+1}: {current_question.text} (True/False): ")     
        self.check_answer(user_answer)
        self.question_number +=1
    
    def check_answer(self, user_answer):
        if self.question_bank[self.question_number].answer == user_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {self.question_bank[self.question_number].answer}.")
        print(f"Your current score is: {self.score}/{self.question_number+1}")