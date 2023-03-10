from question_model import Question
from quiz_brain import QuizBrain
from data import question_data, new_question

question_bank = []
for i in new_question:
    new_q = Question(i['question'], i['correct_answer'])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
    # quiz.checkAnswer()
print("You have Completed th Quiz")
print(f"Your Score is {quiz.score}/{quiz.qno}")
# print(new_question[0]['correct_answer'])
