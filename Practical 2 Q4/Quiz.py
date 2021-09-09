import random


class Quiz:
    questions = []

    def __init__(self):
        while True:
            choice = input("Create Questions(C), Start Quiz(S), Exit(E)\nEnter Choice: ").upper()
            if choice == "C":
                self.create_question()
            elif choice == "S":
                self.quiz()
            elif choice == "E":
                print("Goodbye.")
                exit()
            else:
                print("Invalid Choice")


    # this method creates question bank using question class and store in []

    def create_question(self):
        self.questions.append(Question(input("Please enter a question: "), input("Please enter an answer: ")))

    def quiz(self):
        score = 0
        count = 0
        occuredNumbers = []
        while count!=3:
            if len(self.questions) < 3:
                print("Please Create at least 3 questions before starting the Quiz.")
                break

            elif len(self.questions) > 2:
                random_num = random.randint(0, (len(self.questions)-1))
                if random_num not in occuredNumbers:
                    print((self.questions[random_num]).get_question())
                elif random_num in occuredNumbers:
                    continue
                choice = input("Enter answer: ")
                if choice == (self.questions[random_num]).get_answer() and random_num not in occuredNumbers:
                    occuredNumbers.append(random_num)
                    score+=1
                    count+=1
                    print(f"The answer is {(self.questions[random_num]).get_answer()}")
                    print("You got it right yay!")
                    print(f"You got {score} out of 3 so far!")
                else:
                    count += 1
                    print(f"The answer is {(self.questions[random_num]).get_answer()}")
                    print("Better Luck Next Time!")
                    print(f"You got {score} out of 3 so far!")
        if len(self.questions)>=3:
            print("The Quiz has Ended.")
            print(f"You got {score} out of 3 right!")




class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def get_answer(self):
        return self.answer
    def get_question(self):
        return self.question


Quiz()
