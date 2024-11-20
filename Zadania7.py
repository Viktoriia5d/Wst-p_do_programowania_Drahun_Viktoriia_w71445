#Zadania 7

# Importujemy bibliotekę random, aby móc losowo generować wartość drogi
import random

# Stała cena paliwa za litr
cena_paliwa = 6.5  # zł/l

# Pobieranie średniego spalania od użytkownika
# Funkcja input() pobiera wartość jako tekst, więc konwertujemy ją na liczbę zmiennoprzecinkową float()
spalanie_na_100_km = float(input("Podaj średnie spalanie samochodu (w litrach na 100 km): "))

# Generowanie losowej drogi w zakresie od 50 do 500 km
# randint() zwraca liczbę całkowitą z podanego zakresu
dystans = random.randint(50, 500)

# Obliczanie zużycia paliwa i kosztów podróży
zuzycie_paliwa = (dystans / 100) * spalanie_na_100_km  # Zużycie paliwa w litrach na zadany dystans
koszt_podrozy = zuzycie_paliwa * cena_paliwa           # Koszt paliwa na całą podróż

# Wyświetlanie wyników
print(f"Długość trasy wynosi: {dystans} km")                  # Informacja o losowo wygenerowanej długości trasy
print(f"Przewidywane zużycie paliwa: {zuzycie_paliwa:.2f} litrów")  # Wynik zużycia paliwa, zaokrąglony do 2 miejsc po przecinku
print(f"Szacowany koszt podróży: {koszt_podrozy:.2f} zł")            # Koszt podróży, zaokrąglony do 2 miejsc po przecinku

'''
Dlaczego wartości zwracane przez funkcję randint() są pseudolosowe, a nie prawdziwie losowe?
Funkcja randint() generuje wartości pseudolosowe, ponieważ opiera się na algorytmie deterministycznym, który zaczyna swoje działanie od ustalonej wartości początkowej (tzw. "seed"). 
Dzięki temu, choć wartości wydają się losowe, są one generowane według przewidywalnego wzorca, jeśli znamy wartość "seed". 
W prawdziwej losowości nie byłoby możliwe przewidzenie kolejnych wyników, co jest trudne do osiągnięcia w komputerach, dlatego generują one liczby pseudolosowe.
'''