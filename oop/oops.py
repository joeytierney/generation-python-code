

## Class - Blueprint
## Attributes / Properties / Similar to variables in Procedural
## methods / behaviours / functions / procedures
## objects - 







###########################################################################

#procedural 

# foodList = []
# foodListMaxItems = 10
# drinkList = []
# count = len(foodList)
# maxItem = 10
# if count < maxItem:
#     foodList.append('Pizza')
# print(foodList)

# # # ##oop

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


    
# list1Food = ListOfItems(2, True)
# list1Drinks = ListOfItems(2, True)
# list1Places = ListOfItems(10, True)

# list1Food.addItem('Pizza')
# list1Food.myIsEmpty = True
# list1Food.removeItem()
# # list1Drinks.addItem('Oj')
# # print(list1Drinks.myItems)



class Door():
    def __init__(self, isOpen, colour, material, hasWindow):
        self.isOpen = isOpen
        self.colour = colour
        self.material = material
        self.hasWindow = hasWindow
        self.doorHandle = 'Brass'


class Door2():
    def __init__(self):
        self.isOpen = True
        self.colour = 'Red'
        self.material = 'PVC'
        self.hasWindow = True

myDoor = Door(True, 'Brown', 'Wood', False)
myOtherDoor = Door2()
myotherotherdoor = Door2()

print(myDoor.colour)
print(myOtherDoor.colour)
print(myotherotherdoor.colour)
myotherotherdoor.colour = 'Yellow'
print(myotherotherdoor.colour)
# print(myDoor.doorHandle)
# myDoor.doorHandle = 'Silver'
# print(myDoor.doorHandle)



#########################################################

# #door 

class Door():
    def __init__(self, size, closed, colour, material):
        self.mySize = size
        self.isClosed = closed
        self.myColour = colour
        self.myMaterial = material

    def openDoor(self):
        if self.isClosed:
            self.isClosed = False
            print('Door is now open')
        else:
            print('Door is already open')


    def closeDoor(self):
        if self.isClosed:
            self.isClosed = True
            print('Door is now closed')
        else:
            print('Door already closed')
            

    def describeSelf(self):
        print(f'I am a door made of {self.myMaterial}, I am the colour {self.myColour}. My height is: {self.mySize}cm.')


class Character():
    def __init__(self, name, type, health, level):
        self.name = name
        self.type = type
        self.health = health
        self.level = level 


    def nextLevel(self):
        acceptedTrue = ['true', 't','True','yes','y','Yes','YES','TRUE']
        acceptedFalse = ['no', 'n', 'No', 'f', 'false', 'False', 'NO', 'FALSE']
        isLevelUp = input('Would you like to level up, true or false? ')
        if isLevelUp in acceptedFalse:
            isLevelUp = False
            print('Okay, you stay here for now')
        elif isLevelUp in acceptedTrue:
            isLevelUp = True
            if door1.isClosed == False:
                self.level += 1
                print(f'You are able to go through the door and level up to level {self.level}.')
            else:
                print('The door is still closed, you need to finish this level')
        else:
            print('Please answer True or False. ')



door1 = Door(189, True, 'Red', 'Wood')
firstCharacter = Character('Link','Elf', 100, 1)


while(1):
    print(f'The door is closed: {door1.isClosed}. \n')
    print(f'The current character level is: {firstCharacter.level} \n')

    trivia = input('What is the princesses name? \n')
    if trivia.lower() == 'zelda':
        door1.openDoor()
        firstCharacter.nextLevel()
    else:
        print('Sorry no. \n')

    print(firstCharacter.level)


#########################################################


##takes a username from excel. 

##class rep a current user <- populate

##create a new user in linux
