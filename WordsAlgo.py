file = open("slowa.txt", "r", encoding='utf-8')
wordsList = []
allResult = []
findChars = input("Wpisz litery, z których chcesz ułożyć hasło: ")
if len(findChars) < 2:
    print("Podaj przynajmniej 2 litery")
else:
    for word in file:
        wordsList.append(word.rstrip())

    for word2 in wordsList:
        word2Count = len(word2) - 1
        findCharCount = len(findChars) - 1
        x = 0
        y = 0
        singleResults = ""
        while word2:
            if word2Count >= x and findCharCount >= y:
                if word2[x] == findChars[y]:
                    singleResults += word2[x]
                    x += 1
                    y = 0
                    if singleResults != word2:
                        continue
                    else:
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

                        alfabetCount = 0
                        a = 0
                        licznik1 = 0
                        licznik2 = 0
                        alfabetLength = len(specjalnyAlfabet)
                        while alfabetLength > a:
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

                        if licznik1 == licznik2:
                            allResult.append(singleResults)
                        else:
                            continue
                else:
                    y += 1
            else:
                break

print(" ")
print("Wyszukane hasła z ciągu znaków: " + findChars)
for found in allResult:
    print(found)
