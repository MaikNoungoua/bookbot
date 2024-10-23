


def count_words(file):

    #ponctuation = [".",";",":","?","!","(",")","'",'"',"{","}",]
    count = 0 

    book_as_list = file.split(" ")
   
    for item in book_as_list: 
        #print(item)
        count +=1 
        #print(count)
    print(count)

def main():
    with open("./books/Frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
    count_words(file_contents)


main()
