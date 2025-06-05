from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions_bank = []

for element in question_data:
    # new_question = Question(element["text"], element["answer"])
    new_question = Question(element["question"], element["correct_answer"])
    questions_bank.append(new_question)

quiz = QuizBrain(questions_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("\nYou've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")