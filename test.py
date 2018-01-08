slowo1 = "karczma"
slowo2 = "k"

alfabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
a = 0
b = 0
licznik1 = 0
dlugoscSlowo1 = len(slowo1) - 1
while dlugoscSlowo1 >= a:
    test1 = slowo1[a]
    test2 = alfabet[b]
    if slowo1[a] == alfabet[b]:
        licznik1 += 1
        a += 1
        b = 0
    else:
        # slowo1[a] != alfabet[b]:
        b += 1
print(licznik1)

c = 0
licznik2 = 0
dlugoscSlowo2 = len(slowo2) - 1
while dlugoscSlowo2 >= c:
    test3 = slowo2[c]
    test4 = alfabet[b]
    if slowo2[c] == alfabet[b]:
        licznik2 += 1
        c += 1
        b = 0
    else:
        b += 1
print(licznik2)

if licznik1 == licznik2:
    print("Uda sie")
else:
    print("Nie uda sie")
