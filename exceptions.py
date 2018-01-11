# obsługa wyjatkow
# blok try troche inaczej niz w Javie

# przechwycenie wyjatku file not found error

try:
    path = open("test.txt", "r")
    path.write("Hello world")
    path.close()
except FileNotFoundError as ex:
    print("Wystapil blad podczas otwierania pliku. Prawdopodobnie brak takiego pliku")
    print(ex)

except Exception as ex:
    print("Nieznany blad")
    print(ex)

print("--------------------------")
print("Kod jedzie dalej... nie konczy go tak krytycznie")
print()