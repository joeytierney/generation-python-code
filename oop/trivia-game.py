import winsound
import random
frequency = 1500  # Set Frequency To 1500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second

class ListOfItems():
    def __init__(self, maxLength):
        self.myMaxLength = maxLength
        self.myIsEmpty = True
        self.myItems = []
        self.myLength = len(self.myItems)

    def addItem(self, item):
        if self.myLength < self.myMaxLength:
            self.myItems.append(item)
            self.myIsEmpty = False
            # print('Item added')
            # print(self.myItems)
        else:
            print("Sorry! List is full!\n")
    
    def displayAnswers(self):
        for item in self.myItems:
            print(item)

class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.questionsAnswers = 0

    def printScore(self):
        print(f'My score is {self.score}')

    def answerQuestion(self, question, answer):
        print("***** QUESTION *****")
        print(question)
        answerAttempt = input("\nWhat is your answer: ")
        print("\n")

        if answerAttempt == answer:
            self.score += 1
            myList.addItem(answerAttempt)
        else:
            print("Oh no! That was incorrect :(\n")
            winsound.Beep(frequency, duration)

    def printFinalScore(self):
        print(self.score)

myList = ListOfItems(5)

print("***** PLAYER *****")
name = input("Enter your name: ")
currentPlayer = Player(name)
print("\n")

# ***** QUESTIONS *****

questions = [
    ("Alongside Damon Albarn, who co-founded the virtual band 'Gorillaz'?", "Jamie Hewlett"),
    ("What band were 'Queen' members Brian May and Rodger Taylor members of before they founded 'Queen'?", "Smile"),
    ("The word 'Désolé' in French, means what in English?", "Sorry"),
    ("What is the current (2021) highest grossing movie of all time?", "Avengers Endgame"),
    ("What is the capital of Ireland?", "Dublin")
    ]

random.shuffle(questions)

for question, answer in questions:
    currentPlayer.answerQuestion(question, answer)

# q = "Alongside Damon Albarn, who co-founded the virtual band 'Gorillaz'?"
# a = "Jamie Hewlett"
# currentPlayer.answerQuestion(q, a)

# q = "What band were 'Queen' members Brian May and Rodger Taylor members of before they founded 'Queen'?"
# a = "Smile"
# currentPlayer.answerQuestion(q, a)

# q = "The word 'Désolé' in French, means what in English?"
# a = "Sorry"
# currentPlayer.answerQuestion(q, a)

# q = "What is the current (2021) highest grossing movie of all time?"
# a = "Avengers Endgame"
# currentPlayer.answerQuestion(q, a)

# q = "What is the capital of Ireland?"
# a = "Dublin"
# currentPlayer.answerQuestion(q, a)

print("\n***** YOUR CORRECT ANSWERS *****")
print(myList.myItems)

print("\n***** FINAL SCORE *****")
print(currentPlayer.printFinalScore())