import ru_local


def main():
    """Main program with data entry"""
    print('{}'.format(ru_local.purchase))
    print('{}\n{}\n{}\n{}'.format(ru_local.first_option, ru_local.second_option, ru_local.third_option,
                                  ru_local.fourth_question))
    choice = int(input())
    if choice == 1:
        library_by_genre()
    elif choice == 2:
        library_by_year()
    elif choice == 3:
        library_by_author()
    elif choice == 4:
        print(ru_local.no_choice)
        return
    else:
        print('{}'.format(ru_local.input_error))
        main()


def library_by_genre():
    """Compiling a list of books by genre """
    print('{}'.format(ru_local.question_genre))
    for num_genre in range(len(ru_local.list_of_genre)):
        print(num_genre + 1, '. ', ru_local.list_of_genre[num_genre], sep='')
    num_choice = int(input())
    if not(num_choice == 1 or num_choice == 2 or num_choice == 3 or num_choice == 4 or num_choice == 5 or
           num_choice == 6):
        print(ru_local.input_error)
        library_by_genre()
    with open('Book_data.txt', 'r', encoding='utf-8') as f_in:
        text = f_in.readlines()
        books_by_genry = {}
        for i in range(len(text)):
            genre, writer, title, year = text[i].split(' - ')
            year = int(year)
            data = []
            data.append([year, writer, title])
            if genre not in books_by_genry:
                books_by_genry[genre] = data
            else:
                books_by_genry[genre] += data
    print(books_by_genry)
    output_books = books_by_genry[ru_local.list_of_genre[num_choice - 1]]
    print(output_books)
    print (ru_local.books_by_genre)
    for num_book in range(len(output_books)):
        print(num_book + 1, '. ', output_books[num_book][1], ' "', output_books[num_book][2], '"', sep='')
    right_choice_book = input(ru_local.right_choice)
    if right_choice_book.upper() == ru_local.no:
        main()
    num_choice_book = int(input(ru_local.num_book))
    print(ru_local.book, output_books[num_choice_book - 1][1], ' "', output_books[num_choice_book - 1][2], '"',
          sep='')
    print()
    print(ru_local.thanks)

def library_by_author():
    """Compiling a list of books by author"""
    print('{}'.format(ru_local.question_author))
    surname = input()
    with open('Book_data.txt', 'r', encoding='utf-8') as f_in:
        text = f_in.readlines()
        books_by_author = {}
        for i in range(len(text)):
            genre, writer, title, year = text[i].split(' - ')
            year = int(year)
            data = []
            data.append([year, writer, title])
            if writer not in books_by_author:
                books_by_author[writer] = data
            else:
                books_by_author[writer] += data
    if not(surname in books_by_author):
        print(ru_local.input_error)
        library_by_author()
    print(books_by_author)
    output_books = books_by_author[surname]
    print(output_books)
    print (ru_local.books_by_author)
    for num_book in range(len(output_books)):
        print(num_book + 1, '. ', output_books[num_book][1], ' "', output_books[num_book][2], '"', sep='')
    right_choice_book = input(ru_local.right_choice)
    if right_choice_book.upper() == ru_local.no:
        main()
    num_choice_book = int(input(ru_local.num_book))
    print(ru_local.book, output_books[num_choice_book - 1][1], ' "', output_books[num_choice_book - 1][2], '"',
          sep='')
    print()
    print(ru_local.thanks)

def library_by_year():
    """Compiling a list of books by year"""
    print('{}'.format(ru_local.question_year))
    gap_choice = input()
    if not (gap_choice.upper() == ru_local.before or gap_choice.upper() == ru_local.after):
        print(ru_local.input_error)
        library_by_year()
    with open('Book_data.txt', 'r', encoding='utf-8') as f_in:
        text = f_in.readlines()
        books_by_year = {}
        for i in range(len(text)):
            genre, writer, title, year = text[i].split(' - ')
            year = int(year)
            data = []
            data.append([writer, title])
            if genre not in books_by_year:
                books_by_year[year] = data
            else:
                books_by_year[year] += data
    print(books_by_year)
    output_books = []
    if gap_choice == ru_local.before:
        for year in books_by_year:
            if year < 2000:
                output_books += [books_by_year[year]]
    else:
        for year in books_by_year:
            if year >= 2000:
                output_books += [books_by_year[year]]
    print(output_books)
    print(ru_local.books_by_year)
    for num_book in range(len(output_books)):
        print(num_book + 1, '. ', output_books[num_book][0], ' "', output_books[num_book][1], '"', sep='')
    right_choice_book = input(ru_local.right_choice)
    if right_choice_book.upper() == ru_local.no:
        main()
    num_choice_book = int(input(ru_local.num_book))
    print(ru_local.book, output_books[num_choice_book - 1][0], ' "', output_books[num_choice_book - 1][1], '"',
          sep='')
    print()
    print(ru_local.thanks)

if __name__ == '__main__':
    main()