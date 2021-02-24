##procedural 
# foodList = []
# count = len(foodList)
# maxItem = 10
# if count < maxItem:
#     foodList.append('Pizza')
# print(foodList)
##oop
# class ListOfItems():
#     def __init__(self, maxLength, isEmpty):
#         self.myMaxLength = maxLength
#         self.myIsEmpty = isEmpty
#         self.myItems = []
#         self.myLength = len(self.myItems)
#     def addItem(self, item):
#         if self.myLength < self.myMaxLength:
#             self.myItems.append(item)
#             print('Item added')
#             print(self.myItems)
#             self.myIsEmpty = False
#         else:
#             print('Sorry the list is full')
#     def removeItem(self):
#         if self.myIsEmpty == True:
#             print('Sorry the list is already empty')
#         else:
#             print(f'{self.myItems.pop()} item out') 
#        
# list1Food = ListOfItems(2, True)
# list1Drinks = ListOfItems(2, True)
# list1Places = ListOfItems(10, True)
# list1Food.addItem('Pizza')
# list1Food.myIsEmpty = True
# list1Food.removeItem()
# # list1Drinks.addItem('Oj')
# # print(list1Drinks.myItems)


class Student():
    def __init__(self, firstName, surname):
        self.firstName = firstName
        self.surname = surname

    def displayDeets(self):
        print(f'My first name is {self.firstName} and my surname is {self.surname}')

    def amendDetails(self, fName, sName):
        self.firstName = fName
        self.surname = sName

studentObject1 = Student('Joey','Tierney')
studentObject1.displayDeets()
studentObject1.amendDetails('Rommel','Patton')
studentObject1.displayDeets()
