import random

books = {
    'Alexander Dumas': {
        'Trzej Muszkieterowie': {
            'kategoria': 'dramat',
            'ilosc': 6,
            'cena': 45
        },
        'Hrabia Monte Christo': {
            'kategoria': 'proza fabularna',
            'ilosc': 4,
            'cena': 74
        },
        'Robin Hood banita': {
            'kategoria': 'proza fabularna',
            'ilosc': 1,
            'cena': 37
        }
    },
    'Charles Dickens': {
        'Oliver Twist': {
            'kategoria': 'powiesc',
            'ilosc': 10,
            'cena': 55
        },
        'David Copperfield': {
            'kategoria': 'powiesc',
            'ilosc': 7,
            'cena': 42
        },
        'Wielkie nadzieje': {
            'kategoria': 'powiesc',
            'ilosc': 3,
            'cena': 65
        },
        'Opowieść o dwóch miastach': {
            'kategoria': 'powiesc',
            'ilosc': 5,
            'cena': 45
        }
    },
    'Ernest Hemingway': {
        'Pożegnanie z bronią': {
            'kategoria': 'powiesc',
            'ilosc': 4,
            'cena': 64
        },
        'Komu bije dzwon': {
            'kategoria': 'powiesc',
            'ilosc': 6,
            'cena': 47
        }
    },
    'Fiodor Dostojewski': {
        'Zbrodnia i Kara': {
            'kategoria': 'powiesc',
            'ilosc': 5,
            'cena': 47
        },
        'Bracia Karamazow': {
            'kategoria': 'powiesc',
            'ilosc': 3,
            'cena': 52
        }
    },
    'George Orwell': {
        'Folwark zwierzęcy': {
            'kategoria': 'powiesc',
            'ilosc': 8,
            'cena': 34
        }
    },
    'J.R.R. Tolkien': {
        'Hobbit': {
            'kategoria': 'powiesc',
            'ilosc': 4,
            'cena': 45
        },
        'Władca Pierścieni: Drużyna Pierścienia': {
            'kategoria': 'powiesc',
            'ilosc': 3,
            'cena': 52
        },
        'Władca Pierścieni: Dwie Wieże': {
            'kategoria': 'powiesc',
            'ilosc': 7,
            'cena': 57
        },
        'Władca Pierścieni: Powrót Króla': {
            'kategoria': 'powiesc',
            'ilosc': 6,
            'cena': 54
        },
        'Przygody Toma Bombadila': {
            'kategoria': 'poezja',
            'ilosc': 1,
            'cena': 75
        }
    }
}


# 1
def update_category():
    print("Zaktualizowane kategorie:")
    new_category = ['powiesc', 'proza fabularna', 'dramat', 'poezja', 'komedia', 'thriller']
    quantity_new_category = [1, 2, 3, 4]
    for author in books:
        for title in books[author]:
            books[author][title]['kategoria'] = random.sample(new_category, random.choice(quantity_new_category))
    print(books)
    print()


update_category()


# 2
def find_book_for_two_random_categories(first, second):
    book_finder = []
    for author in books:
        for title in books[author]:
            categories = books[author][title]['kategoria']
            if first in categories and second in categories:
                book_finder.append(title)
    print("Książki, w których znajduje się kategoria {} i {}".format(first, second))
    if len(book_finder) == 0:
        print("Nie ma takich książek")
    else:
        print(book_finder)
    print()


find_book_for_two_random_categories('powiesc', 'dramat')


# 3
def find_book_for_two_categories(first, second):
    book_finder = []
    for author in books:
        for title in books[author]:
            categoriesLength = len(books[author][title]['kategoria'])
            categories = books[author][title]['kategoria']
            if categoriesLength == 2:
                if first in categories and second in categories:
                    book_finder.append(title)
    print("Książki, wyłącznie z kategoriami {} i {}".format(first, second))
    if len(book_finder) == 0:
        print("Nie ma takich książek")
    else:
        print(book_finder)
    print()


find_book_for_two_categories('komedia', 'dramat')


def find_book_for_two_categories_where_one_is_fine(first, second):
    book_finder = []
    for author in books:
        for title in books[author]:
            categories = books[author][title]['kategoria']
            if first in categories or second in categories:
                book_finder.append(title)
    print("Książki, których kategoria to {} albo {}".format(first, second))
    if len(book_finder) == 0:
        print("Nie ma takich książek")
    else:
        print(book_finder)
    print()


find_book_for_two_categories_where_one_is_fine('thriller', 'poezja')
