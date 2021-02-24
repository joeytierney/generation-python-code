import datetime

def displayBlogPost():
    print("\n***** " + name + "'s recent blog post *****")
    for key, value in blogPost1.items(): # print the post
        print(f'{key} {value}')

def updateBlogPost():
    updatePost = True # set updatePost to true

    while updatePost is True: # while updatePost is true, prompt user to update blog post
        updateMessage = input("\nWould you like to update your blog post? (Y/N) ")
        updateMessage = updateMessage.upper() # forces the input to be uppercase

        if updateMessage == 'Y':
            print("\nThis is your original post:",blogPost1.get(key3)) # show the user their original post
            newPost = input("\nEnter your new blog post: ")
            print("\nThis is your new post: " + newPost) # show them their new post
            saveChanges = input("\nWould you like to save your changes? (Y/N) ")
            saveChanges = saveChanges.upper() # force input to be uppercase
            if saveChanges == 'Y':
                blogPost1[f'{key3}'] = newPost # replace the item at 'key3' with the new post
                print("\n***** " + name + "'s recent blog post *****")
                for key, value in blogPost1.items():
                    print(f'{key} {value}')
            elif saveChanges == 'N':
                print('\nChanges not saved!')
            else:
                print('\nInvalid input! Please enter Y/N')
        elif updateMessage =='N':
            updatePost = False # set updatePost to False so we can exit the loop 
        else:
            print('\nInvalid input! Please enter Y/N')

def createDictionaryItem(incomingList):
    for row in incomingList:
        key = row[0] 
        value = row[1]
        blogPost2[f'{key}'] = value
 
    return blogPost2
 
# empty dictionaries 
blogPost1 = {}
blogPost2 = {}

validDate = False # set date to false

# declare keys for dictionary
key1 = 'Author: '
key2 = 'Date: '
key3 = 'Post: '

# take inputs from user
name = input("Enter author name: ")
while not validDate: # while validDate is false
    datePost = input("Enter date (DD/MM/YY): ")
    try: # strptime throws an exception if the input doesn't match the pattern
        d = datetime.datetime.strptime(datePost, "%d/%m/%y")
        validDate = True # set it to true to exit the loop
    except:
        print("Please enter Date in the format of: DD/MM/YY")
post = input("Enter post: ")

# store the inputs from the user in the dictionary
blogPost1[f'{key1}'] = name
blogPost1[f'{key2}'] = datePost
blogPost1[f'{key3}'] = post

print("\n")

displayBlogPost()
updateBlogPost() # call the updateBlogPost function

# hard coded list
myList = [['Author: ', 'Patton Tierney'], ['Date: ', '07/01/21'],['Post: ', 'I like annoying my owner at 7am to bring me out on walks in the cold :)']]

newBlogPost = createDictionaryItem(myList)
print("\n***** Here's a recent blog post from another user *****")
for key, value in blogPost2.items(): # print the post
    print(f'{key} {value}')