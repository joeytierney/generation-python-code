


class Human():
    def __init__(self, fName, lName, age, birthPlace):
        self.firstName = fName
        self.lastName = lName
        self.age = age
        self.birthPlace = birthPlace

    def displayDeets(self):
        print(f'My name is {self.firstName} {self.lastName}. I was born in {self.birthPlace} and I am {self.age} years old.')
    
    def speak(self):
        self.displayDeets()
        again = input('Did you want me to say that again? y/n ').lower()
        if again == 'y': 
            self.displayDeets()
        else:
            print('Okay, bye!')





# firstHuman = Human('Eve', 'Noname', 35, 'Unknown')
# firstHuman.speak()
    





# ###############################################################################################

# class Adult(Human):
#     def __init__(self, fName, lName, age, birthPlace, job, canDrive, married):
#         super().__init__(fName, lName, age, birthPlace)
#         self.job = job
#         self.canDrive = canDrive
#         self.married = married


# # adult1 = Adult('Grace', 'Shaffi', '30', 'Hackney', 'Instructor', True, True)

# # adult1.displayDeets()

# ###############################################################################################
 

class Adult(Human):
    def __init__(self, fName, lName, age, birthPlace, job, canDrive, married):
        super().__init__(fName, lName, age, birthPlace)
        self.job = job
        self.canDrive = canDrive
        self.married = married


    def changeJob(self):
        newJob = input('What is your new job? ')
        if newJob:
            self.job = newJob
            print(f'Congrats, on the new job as a {self.job}.')
        else:
            print('Sorry, please enter a job title')  


adult1 = Adult('Grace', 'Shaffi', '30', 'Hackney', 'Instructor', True, True)

adult1.displayDeets()
adult1.changeJob()


# ###############################################################################################


# class Child(Human):
#     def __init__(self, fName, lName, age, birthPlace, hungry, mother, canWalk):
#         super().__init__(fName, lName, age, birthPlace)
#         self.hungry  = hungry
#         self.mother = mother
#         self.canWalk = canWalk

#     def feedMe(self):
#         if self.hungry:
#             print('Okay, have a potato')
#             self.hungry = False
#         else:
#             print('Nope, here is a dummy istead')
    
#     def callMother(self):
#         print(f'Can you get my mother, her name is {self.mother.firstName}')


# child1 = Child('Grace Jnr', 'Briody', 5, 'Harlow', True, adult1, True)

# child1.callMother()