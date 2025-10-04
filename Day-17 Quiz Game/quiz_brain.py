class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {question.text} (True/False)?:")
        self.question_number += 1
        self.check_answer(question.answer, user_answer)
        return self.score

    def check_answer(self, q_answer, u_answer):
        if q_answer.lower() == u_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {q_answer}. ")
        print(f"Your current score is: {self.score}/{self.question_number}\n\n")
