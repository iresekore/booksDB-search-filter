#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def read_file(filename):
    books = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split('\t')
                # data = (title, author, publisher, date, category)
                if len(data) == 5:
                    books.append(data)
                else:
                    print('Error: Incorrect format in line:', line)
        return books
    except FileNotFoundError:
        print('Error: File not found.')
        return None
    
def format_book(book):
    return book[0] + ', by ' + book[1] + ' (' + book[3] + ')'

def print_results(results):
    for x in results:
        print('\t' + x)
        
def no_books_found():
    print ('\tno books found for your query :(')
    

def search_between_years(start, stop, books):
    result = []
    for book in books:
        year = int(book[3].split('/')[-1])
        if (year >= int(start)) and (year <= int(stop)):
            result.append(format_book(book))
    if len(result) == 0:
        no_books_found()
    else:
        print('All Titles between ' + start + ' and ' + stop + ':')
        print_results(result)
    return

def search_by_month_year(month, year, books):
    result = []
    for book in books:
        if (int(year) == int(book[3].split('/')[-1])) and (int(month) == int(book[3].split('/')[0])):
            result.append(format_book(book))
    if len(result) == 0:
        no_books_found()
    else:
        print('All Titles in month ' + month + ' of ' + year + ':')
        print_results(result)
    return

def search_by_author(author, books):
    result = []
    for book in books:
        if author.lower() in book[1].lower():
            result.append(format_book(book))
    if len(result) == 0:
        no_books_found()
    else:
        print('All Titles by ' + author + ':')
        print_results(result)
    return
    
def search_by_title(thing, books):
    result = []
    for book in books:
        if thing.lower() in book[0].lower():
            result.append(format_book(book))
    if len(result) == 0:
        no_books_found()
    else:
        print('All titles containing ' + thing + ':')
        print_results(result)
    return


    
def menu(books):
    while True:
        print ('''\nWhat would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit''')
        option = input()
        if option == '1':
            year1 = input('enter a beginning year:')
            year2 = input('enter an ending year:')
            search_between_years(year1, year2, books)
            continue
        elif option == '2':
            month = input('enter month(as a number 1-12):')
            year = input('enter year:')
            search_by_month_year(month, year, books)
            continue
        elif option == '3':
            author = input('enter an authors name (or part of a name):')
            search_by_author(author, books)
            continue
        elif option == '4':
            title = input('enter a title (or part of a title):')
            search_by_title(title, books)
            continue
        elif option == 'Q' or option == 'q':
            print('\n\tthanks for using my program :)')
            break
        else:
            print('\tplease choose an option from the menu >:(')
            continue
  
def main():
    books = read_file('bestsellers.txt')
    menu(books)
    # print (search_between_years('1960', '1962', books))
    
    
    
if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




