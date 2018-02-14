# do tworzenia GUI importuje tkinter i wszystkie jego metody (*)
from tkinter import *

# inicjalizacja obiektu Tk, gdzie pózniej mam dostep do metod
window = Tk()
# metoda, która zwraca mi nazwe okienka
window.title("Simple Window")
# metoda ustawie wielkość głównego okna
window.geometry("1000x500")
# tworze obiekt Frame czyli element w moim oknie tak jakby ramka, albo pojemnik
#  w konstruktorze przekazuje obiekt na którym ma się pojawić moja ramka
frame = Frame(window)
# metoda grid zapewni mi widoczność ramki
frame.grid()
# tworze łańcuch znaków jako przyklad
text = "Przykładowy napis, który tutaj sie wyświetla"
# tworze obiekt Label czyli etykietę, jaki bedzie znajdować sie w danej ramce
# w paramerach podaje w jakiej ramce dana etykieta ma sie znajdowac
# jako 2 parametr przekazuje stringa czyli to sie wyswietli w etykiecie
# mozna oczywiscie odwolywac sie do roznych metod na łancuchach znaków
label = Label(frame, text=text.upper())
# metoda grid zapewni mi widoczność etykiety
label.grid()
# mainloop to cykl uruchomieniowy pętli zdarzeń mojego GUI

# Kilka sposobów na wywołanie buttonów, które jeszcze nic nie robią ale są klikalne

# definiuje obiekt Button, w którym przekazuje w parametrach daną ramkę/ pudełko
# w którym ma się znajdować dany btn
# meoda grid zapewnia mi widoczność etykiety
btn1 = Button(frame, text="Sposób 1")
btn1.grid()

# inne sposoby
# metoda configure pozwala mi dostanie sie do buttono gdy juz go zdefiniuje
btn2 = Button(frame)
btn2.configure(text="Sposób 2")
btn2.grid()

textForBtn3and4 = ["Sposób 3", "Sposób 4"]
btn3 = Button(frame, text=textForBtn3and4[0])
btn3.grid()

btn4 = Button(frame, text=textForBtn3and4[1])
btn4.grid()

window.mainloop()
