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
books['Antoine de Saint-Exupéry'] = {'Mały Książę': {'kategoria': 'powiastka', 'ilosc': 10, 'cena': 23}}
print(books)


# 2
def add_book_to_library(author, title, category, quantity, price):
    if author in books.keys():
        books[author][title] = {'kategoria': category, 'ilosc': quantity, 'cena': price}
    else:
        books[author] = {title: {'kategoria': category, 'ilosc': quantity, 'cena': price}}


# 3
# dodaje książkę której autor jest już w księgarni
add_book_to_library('J.R.R. Tolkien', 'Silmarillion', 'zbiór opowieści', 5, 67)
# dodaje książkę której autor nie jest w księgarni
add_book_to_library('Henryk Sienkiewicz', 'Potop', 'powieść', 12, 43)
print(books)
