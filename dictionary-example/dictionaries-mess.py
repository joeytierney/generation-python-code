# messing around with dictionaries

dictionaryExample = {
    'key1' : 'Joey',
    'key2' : 'Patton',
    'key3' : 'Rommel',
    'key4' : 'Chester',
    'key5' : 'Max'
}

# print single value
print(dictionaryExample.get('key1'))

# add an item to the dictionary
dictionaryExample['key6'] = 'Pepsi'

# update value
dictionaryExample['key1'] = 'Dante'

# print items as list of tuples
print(dictionaryExample.items())

# print items in key:value pair
print(dictionaryExample)

# delete an item
del dictionaryExample['key1']
print(dictionaryExample.items())

# return true or false
isPatton = 'key2' in dictionaryExample
print(f'Is Patton in the list: {isPatton}')

# search for a key
searchFor = input("Enter search item: ")
isFound = searchFor in dictionaryExample
print(f'Is {searchFor} in the list: {isFound}')

# iterating through
for key, value in dictionaryExample.items():
    print(f'The key is {key}, the value is {value}')

# zip method example
questionsD = {
    'q1' : 'What is your name? ',
    'q2' : 'What is your age? ',
    'q3' : 'What is your height? ',
    'q4' : 'What is your favourite pet? '
}

answersD = {
    'a1' : 'Joey',
    'a2' : 26,
    'a3' : '5 ft 9',
    'a4' : 'Patton'
}

for q, a in zip(questionsD.items(), answersD.items()):
    print(f'{q[1]} {a[1]}')

# iterate through each list printing out q and a
questions = ['name', 'quest', 'favourite colour']
answers = ['joey', 'none', 'blue']

for q, a in zip(questions, answers):
    print(f'What is your {q}? It is {a}')