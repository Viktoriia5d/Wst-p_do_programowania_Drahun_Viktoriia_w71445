#Zadania 6

#Cena paliwa za litr
cena_paliwa = 6.5 #zł/l

# Pobieranie danych od użytkownika
# Funkcja input() wyświetla pytanie i oczekuje na wpisanie wartości przez użytkownika
# Wartość zwracana przez input() jest traktowana jako tekst, więc musimy ją przekonwertować na liczbę za pomocą float()
dystans = float(input("Podaj przejechhany dystant (w km): "))
spalanie_na_100_km = float(input("Podaj średnie spalanie samochodu (litry na 100 km): "))

#Obliczanie zużycia paliwa i kosztów podróży
zuzycie_paliwa = (dystans / 100) * spalanie_na_100_km # Zużycie paliwa w litrach
koszt_podrozy = zuzycie_paliwa * cena_paliwa # Koszt całkowity podróży

#Wyświetlanie wyników
print(f"Przewidywane zużycie paliwa: {zuzycie_paliwa:.2f} litrów")
print(f"Szacowany koszt podróży: {koszt_podrozy:.2f} zł.")