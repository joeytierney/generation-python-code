class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name
        # self.age = age
        # self.bornPlace = bornPlace

    def printName(self):
      print(f'My name is {self.name}')  

# someAnimal = Animal('Unknown', 'Grogu')
# someAnimal.printName()
# print(someAnimal.name)
#######################################

class Cat(Animal):
    def __init__(self, species, name):
        super().__init__(species, name)
        
    def hiss(self):
      print('HISS!')

    def meow(self):
      print('Meow')

    def purr(self):
      print('Puurr Puuurrrr')

class Bird(Animal):
    def __init__(self, species, name):
        super().__init__(species, name)

    def squark(self):
      print('SKWARK!!!!!!')
        
class Dog(Animal):
    def __init__(self, species, name):
        super().__init__(species, name)
        
    def runAndBark(self):
        print("Bark Bark, run run")

class Game():
  def __init__(self):
    self.finished = False

  def compareObj(self, object1, object2):
    if object1.species == 'Cat' and object2.species == 'Dog':
      object1.hiss()
      object2.runAndBark()
    elif object1.species == 'Cat' and object2.species == 'Bird':
      object2.squark()
    elif object1.species == 'Cat' and object2.species == 'Cat':
      object1.meow()
      object1.meow()

kittie1 = Cat('Cat', 'Loki')
kittie2 = Cat('Cat', 'Albus')
doggo = Dog('Dog', 'Patton')
birdy = Bird('Bird', 'Tweety Pie')
currentGame = Game()

while(currentGame.finished == False):
  currentGame.compareObj(kittie1, kittie2)
  print('Next \n')
  currentGame.compareObj(kittie1, birdy)
  print('Next \n')
  currentGame.compareObj(kittie1, doggo)
  print('Next \n')
  currentGame.finished = True