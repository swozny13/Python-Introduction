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
                        a = 0
                        b = 0
                        licznik1 = 0
                        singleResultsCount = len(singleResults) - 1
                        while singleResultsCount >= a:
                            if singleResults[a] == alfabet[b]:
                                test1 = singleResults
                                test2 = singleResults[a]
                                test3 = alfabet[b]
                                licznik1 += 1
                                a += 1
                                b = 0
                            else:
                                test4 = singleResults[a]
                                test5 = alfabet[b]
                                b += 1
                        print(licznik1)

                        c = 0
                        licznik2 = 0
                        while findCharCount >= c:
                            if findChars[c] == alfabet[b]:
                                licznik2 += 1
                                c += 1
                                b = 0
                            else:
                                b += 1
                        print(licznik2)
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
