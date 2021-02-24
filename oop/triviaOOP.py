class ListOfItems():
    def __init__(self, maxLength):
        self.myMaxLength = maxLength
        self.myIsEmpty = True
        self.myItems = []
        self.myLength = len(self.myItems)

    def addItem(self, item):
        if self.myLength < self.myMaxLength:
            self.myItems.append(item)
            # print('Item added')
            # print(self.myItems)
            self.myIsEmpty = False
        else:
            print('Sorry the list is full')

    def displayItems(self):
             for item in self.myItems:
                 print(item) 


class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.quiestionsAnswers = 0


    def printScore(self):
        print(f'My score is {self.score}') 

    def answerQuestion(self, question, answer):
        print(question)
        answerAttempt = input('What is your answer: ')
        if answerAttempt == answer:
            self.score += 1
            myList.addItem(answerAttempt)
        else:
            print('Sorry that was the wrong answer')


myList = ListOfItems(5)

name = input("What is your name: ")
currentPlayer = Player(name)

q = 'What is the capital of Ireland? '
a = 'Dublin'
currentPlayer.answerQuestion(q, a)

q = 'What is the capital of England? '
a = 'London'
currentPlayer.answerQuestion(q, a)

q = 'What is the capital of Wales? '
a = 'Cardiff'
currentPlayer.answerQuestion(q, a)

q = 'What is the capital of Scotland? '
a = 'Edinburgh'
currentPlayer.answerQuestion(q, a)

q = 'What is the capital of France? '
a = 'Paris'
currentPlayer.answerQuestion(q, a)

print(myList.myItems)

