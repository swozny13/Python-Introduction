slowo1 = "rumak"
slowo2 = "makjrisu"
alfabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"

specjalnyAlfabet = ""
slowo1Count = len(slowo1) - 1
b = 0
c = 0
while slowo1Count >= c:
    if slowo1[c] == alfabet[b]:
        test1 = slowo1[c]
        test2 = alfabet[b]
        specjalnyAlfabet += slowo1[c]
        c += 1
        b = 0
    else:
        test3 = slowo1[c]
        test4 = alfabet[b]
        b += 1

alfabetCount = 0
a = 0
licznik1 = 0
licznik2 = 0
alfabetLength = len(specjalnyAlfabet)
while alfabetLength > a:
    literka = specjalnyAlfabet[alfabetCount]
    temp1 = slowo1.count(literka)
    temp2 = slowo2.count(literka)
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
    print("uda się")
else:
    print("Nie uda sie")
