
#characters = {}

def count_words(file):
    #global book_as_list
    #ponctuation = [".",";",":","?","!","(",")","'",'"',"{","}",]
    count = 0 
    book_as_list = file.split() #this split methods operates on spaces, tabs , new lines.

    for item in book_as_list: 
        count +=1 
    #print(count)
    return count

def count_characters(book):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
               "n","o","p","q","r","s","t","u","v","w","x","y","z" ]
    global characters
    characters = {}
    for item in book: 
        if item not in characters and item in alphabet: #starts by checking if the character is already in the dictionary. If it is not it creates it.
            #print(item)
            characters[item] = 1
        elif item in characters and item in alphabet: 
            characters[item] += 1
    #print(characters)

    


def main():
    with open("./books/Frankenstein.txt") as f:
        file_contents = f.read()
        file_contents_lowered = file_contents.lower()

    count_words(file_contents)
    count_characters(file_contents_lowered)

    book_title = input("Please enter the book title: ")

    print("\n")

    print(f"--- Begin report of books/{book_title} --- \n{count_words(file_contents)} words found in the document")
    print("\n")
    for item in characters: 
        print(f"The '{item}' character was found {characters[item]} times")
    print("--- End report ---")

main()
