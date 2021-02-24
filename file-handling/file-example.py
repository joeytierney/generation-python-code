
counter = 0 # counter to keep track of user attempts in while loop

with open('demoFile4.txt', 'w') as file4:
    while counter != 3: # while the counter is not equal to 3
        try:
            name=input("Enter a name: ")
            age=int(input("Enter your age: "))
            file4.write(f'{name},{str(age)}\n')
            counter+=1 # add 1 to the counter
        except:
            print('That was an invalid age ')