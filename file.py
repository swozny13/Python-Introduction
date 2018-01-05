# plik mogę otworzyć za pomocą open()
# w parametrach wpisuje np nazwę pliku, który chce otworzyć
# jak jej nie ma to python ją stworzy
# "r" to tryb jaki na jakim bedziemy pracowac z plikiem - mozna inne wybrac,
# ale r tylko odczytuje z pliku
# utf-8 to zeby byly polskie znaki oczywiscie
# rstrip - funkcja pomija znaki odstepu (\n)


# przykladowyPlik = open("plik.txt", "r", encoding='utf-8')
#
# szukanaFraza = input("Podaj slowo: ")
#
# if szukanaFraza in przykladowyPlik:
#     print("Znalazłem takie słowo")
# else:
#     print("Nie znalazłem takiego słowa")
#
# przykladowyPlik.close()


# slownik = open("slowa.txt", "r", encoding='utf-8')
# for slowo in slownik.readlines():
#     x = 0
#     while int(len(slowo)) > x:
#         pojedyncze = slowo[x]
#         x += 1
#         print(pojedyncze, end=' ')
# slownik.close()


# szukajHasla = input("Podaj słowo: ")
# # rozbicie hasla na pojedyncze litery
# x = 0
# while int(len(szukajHasla)) > x:
#     pojedyncze = szukajHasla[x]
#     x += 1
#     print(pojedyncze, end=' ')
#
# print()
# print("----------------")

# porównianie hasła "szukajHasla" z hasłami w słowniku
slownik = open("slowa.txt", "r", encoding='utf-8')

"""
Z racji tego, że było problem podczas gdy sprawdzam sobie moje haslo 
z haslami w slowniku, poniewaz wyszukiwalo mi ciag znakow wewnatrz danego
slowa czego nie chcialem, dlatego dodalem sobie moje hasla ze slownika (slowa.txt)
do listy, a dopiero pozniej ja przeszukiwalem
"""
lista = []
for slowo in slownik:
    lista.append(slowo.rstrip())

flaga = True
while flaga:
    szukajHasla = input("Podaj słowo: ")
    if szukajHasla in lista:
        print("Znaleziono")
    else:
        print("Nie znaleziono")
        dodaj = int(input("Jak chcesz dodac do listy kliknij 1, a jak nie to 0: "))
        if dodaj == 1:
            lista.append(szukajHasla)
        elif dodaj == 0:
            continue
        else:
            flaga = False
    print(lista)
slownik.close()
