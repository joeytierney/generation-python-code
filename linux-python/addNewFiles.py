import os

isAsk = True
filePrompt = input("Enter Python file name: ")

filename = filePrompt + '.py'
os.system(f'touch {filename}')

while isAsk == True:
    askUser = input('Would you like to create another file? (Y/N): ')
    askUser = askUser.upper()

    if askUser == 'Y':
        filePrompt = input("Enter Python file name: ")
        filename = filePrompt + '.py'
        os.system(f'touch {filename}')
    elif askUser == 'N':
        isAsk = False
    else:
        print('Invalid input! Enter Y/N ')

print('\nShowing all files with extension .py')
os.system(f'find *.py')
print('\n')