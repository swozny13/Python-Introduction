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
beforeBuy = books['Charles Dickens']['Oliver Twist']['ilosc']
print("Ilość książki Charlesa Dickensa \"Olivier Twist\" przed zakupem: {} szt".format(beforeBuy))
afterBuy = beforeBuy - 1
print("Ilość książki Charlesa Dickensa \"Olivier Twist\" po zakupie: {} szt".format(afterBuy))


# aktualizuje stan ksiazek dostepnych w ksiegarni


# 2
def buy_book(author, title, quantity):
    quantityBeforeBuy = books[author][title]['ilosc']
    if quantityBeforeBuy < quantity:
        print("Nie możesz tyle kupić. Aktualny stan wynosi: {}".format(quantityBeforeBuy))
    else:
        quantityAfterBuy = quantityBeforeBuy - quantity
        # aktualizuje stan ksiazek dostepnych w ksiegarni
        books[author][title]['ilosc'] = quantityAfterBuy
        print("Właśnie kupiłeś {} szt książki".format(quantity))
        print("Aktualny stan wynosi: {}".format(quantityAfterBuy))


# 3
# w przypadku gdy chce kupić więcej książek niż mam dostępnych
buy_book('Alexander Dumas', 'Robin Hood banita', 2)
# w przypadku gdy stan książki jest adekwatny do stanu dostępności
buy_book('J.R.R. Tolkien', 'Władca Pierścieni: Powrót Króla', 4)
