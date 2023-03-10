class QuizBrain:
    def __init__(self, qlist):
        self.qno = 0
        self.questionList = qlist
        self.score = 0

    def still_has_question(self):
        if self.qno < len(self.questionList):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.questionList[self.qno]
        self.qno += 1
        userInput = input(
            f"{self.qno}.Q {current_question.question} (True / False) : ").capitalize()
        # input(f"{self.qno}.Q {current_question.text} True / False : ")
        self.checkAnswer(userInput, current_question.answer)

    def checkAnswer(self, user_answer, current_answer):
        if current_answer == user_answer:
            self.score += 1
            print("You got it Right!")
        else:
            print("You got it Wrong!")
        print(f"The Correct Answer Was : {current_answer}")
        print(f"Your Current Score is {self.score}/{self.qno}")
        print("")
    # def checkAns(self):
    #     if self.current_question.answer == self.userInput:

        # def check(self):
        #     if self.qlist[self.qno - 1].answer == self.userInput:
        #         self.score += 1
        #         print("You Got Right")
        #         print(
        #             f"The Correct answer was : {self.qlist[self.qno - 1].answer}")
        #         print(f"Your Current Score is {self.score}/{self.qno}")
        #         self.qno += 1
        #     else:
        #         print("You Got Wrong")
        #         print(f"The Correct answer was : {self.qlist['answer']}")
        #         print(f"Your Current Score is {self.score}/{self.qno}")
        #         self.qno += 1
