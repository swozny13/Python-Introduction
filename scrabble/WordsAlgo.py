import operator

file = open("slowa.txt", "r", encoding='utf-8')
wordsList = []
allResult = []
# TODO: dodać np try except -> aby nie można wpisać liczb, oraz przerabiało...
# TODO: ...jak wpisze się z dużych liter albo wycinało puste znaki
findChars = input("Wpisz litery, z których chcesz ułożyć hasło: ")
if len(findChars) < 2:
    print("Podaj przynajmniej 2 litery")
else:
    # WYRAZY Z PLIKU ŁADUJE DO LISTY
    for word in file:
        wordsList.append(word.rstrip())

    # SPRAWDZAM ZGODNOŚĆ LITEREK Z LITERKAMI Z SŁOWA SZUKANEGO
    for word2 in wordsList:
        word2Count = len(word2) - 1
        findCharCount = len(findChars) - 1
        x = 0
        y = 0
        # DO "SINGLERESULTS" TRAFIAJĄ TYLKO TE WYRAZY, KTÓRE MAJĄ
        # TAKIE SAME LITERKI, DZIĘKI CZEMU ZAWĘŻAM MOJE WYNIKI
        singleResults = ""
        while word2:
            if word2Count >= x and findCharCount >= y:
                # PORÓWNANIE LITER
                if word2[x] == findChars[y]:
                    singleResults += word2[x]
                    x += 1
                    y = 0
                    if singleResults != word2:
                        continue
                    else:
                        # ZA POMOCĄ ALFABETU TWORZĘ SWÓJ SPECJALNY ALFABET,
                        # KTÓRY PÓŹNIEJ BĘDĘ WYKORZYSTYWAĆ.
                        alfabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"

                        specjalnyAlfabet = ""
                        singleResultsCount = len(singleResults) - 1
                        b = 0
                        c = 0
                        while singleResultsCount >= c:
                            if singleResults[c] == alfabet[b]:
                                specjalnyAlfabet += singleResults[c]
                                c += 1
                                b = 0
                            else:
                                b += 1

                        # SPECJALNY ALFABET POMOŻE MI W SPRAWDZENIU
                        # WYSTĄPIENIA ILE RAZY WYSTĘPUJĘ DANA LITERKA
                        # CO PÓŹNIEJ DODAJE DO LICZNIKÓW. FUNKCJONALNOŚĆ
                        # TA POMOŻE W PRZYPADKU GDY MAMY DO CZYNIENIA
                        # Z WIELOKROTNOŚCIĄ WYSTĄPIENIA WIĘKSZEJ ILOŚCI
                        # KONKRETNEJ LITERY
                        alfabetCount = 0
                        a = 0
                        licznik1 = 0
                        licznik2 = 0
                        alfabetLength = len(specjalnyAlfabet)
                        while alfabetLength > a:
                            # LICZENIE LITER
                            literka = specjalnyAlfabet[alfabetCount]
                            temp1 = singleResults.count(literka)
                            temp2 = findChars.count(literka)
                            # TODO: GDZIEŚ PRZY TYM IFIE NALEŻY PORÓWNYWAĆ CZY DANA LITERKA JUŻ BYŁA
                            if temp1 != temp2:
                                licznik1 += temp1
                                licznik2 += temp2
                                alfabetCount += 1
                                a += 1
                            else:
                                licznik1 += temp1
                                licznik2 += temp2
                                alfabetCount += 1
                                a += 1
                        # JEŚLI LICZNIKI SĄ RÓWNE TO WTEDY JEST PEWNOŚĆ
                        # ŻE WYRAZ ZE SŁOWNIKA WYSTĘPUJĘ W NASZYCH PODANYCH
                        # ZNAKACH NA POCZĄTKU
                        if licznik1 == licznik2:
                            allResult.append(singleResults)
                        else:
                            continue
                else:
                    y += 1
            else:
                break
# WYNIKI DODAJE DO FINALNEJ LISTY
print(" ")
print("Wyszukane hasła z ciągu znaków: " + findChars)

# PUNKTACJA ZA SŁOWA

points = {"a": 1, "ą": 5, "b": 3, "c": 2, "ć": 6, "d": 2, "e": 1, "ę": 5, "f": 5, "g": 3,
          "h": 3, "i": 1, "j": 3, "k": 2, "l": 2, "ł": 3, "m": 2, "n": 1, "ń": 7, "o": 1,
          "ó": 5, "p": 2, "r": 1, "s": 1, "ś": 5, "t": 2, "u": 3, "w": 1, "y": 2, "z": 1,
          "ź": 9, "ż": 5}

for found in allResult:

    licznikPunktow = 0
    s = 0
    t = 0
    foundCount = len(found) - 1

    while foundCount >= s:
        licznikPunktow += points.get(found[t])
        t += 1
        s += 1

    # PRINTUJE HASŁA Z PUNKTACJĄ (NIEPOSORTOWANE)
    # print("{}: {} pkt".format(found, licznikPunktow))

    # WYNIKI DO SŁOWNIKA
    resultsDictionary = {found: licznikPunktow}

    # SORTUJE WYNIKI
    a = sorted(resultsDictionary.items(), key=operator.itemgetter(0))
    print(a)
# PRINTUJE WYNIKI
