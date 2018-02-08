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
authorList = []
for author in books.keys():
    authorList.append(author)

print("Lista autorów w księgarni:")
print(authorList)
print()

# 2
booksList = []
for book in books:
    for title in books[book]:
        booksList.append(title)

print("Lista książek w księgarni:")
print(booksList)
print()

# 3
counter = 0
for book in books:
    for title in books[book]:
        quantity = books[book][title]['ilosc']
        counter += quantity
print("Aktualna ilość książek w składzie: {}".format(counter))
print()

# 4
currentlyMax = 0
currentlyMin = 0
maxBook = ""
minBook = ""
flag = True
for book in books:
    for title in books[book]:
        quantity = books[book][title]['ilosc']

        if quantity > currentlyMax:
            currentlyMax = quantity
            maxBook = "{}: {} szt".format(title, quantity)
        elif quantity == currentlyMax:
            currentlyMax = quantity
            maxBook += ", {}: {} szt".format(title, quantity)

        if flag:
            currentlyMin = quantity
            flag = False
        else:
            if quantity < currentlyMin:
                currentlyMin = quantity
                minBook = "{}: {} szt".format(title, quantity)
            elif quantity == currentlyMin:
                currentlyMin = quantity
                minBook += ", {}: {} szt".format(title, quantity)

print("Najwięcej tytułów w księgarni: {}".format(maxBook))
print("Najmniej tytułów w księgarni: {}".format(minBook))
print()

# 5
currentlyMax = 0
currentlyMin = 0
maxBookAuthor = ""
minBookAuthor = ""
flag = True
for book in books:
    current = 0
    for title in books[book]:
        quantity = books[book][title]['ilosc']
        current += quantity

    if current > currentlyMax:
        currentlyMax = current
        maxBookAuthor = "{} - {} szt".format(book, current)
    elif current == currentlyMax:
        currentlyMax = current
        maxBookAuthor += ", {} - {} szt".format(book, current)

    if flag:
        currentlyMin = current
        flag = False
    else:
        if current < currentlyMin:
            currentlyMin = current
            minBookAuthor = "{} - {} szt".format(book, current)
        elif current == currentlyMin:
            currentlyMin = current
            minBookAuthor += ", {} - {} szt".format(book, current)

print("Najwięcej książek jest autora: {}".format(maxBookAuthor))
print("Najmniej książek jest autora: {}".format(minBookAuthor))
