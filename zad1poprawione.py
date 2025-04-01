import math
from datetime import datetime

# Funkcja konwertująca datę z formatu tekstowego na obiekt datetime
def convDate(pelnaData):
    try:
        return datetime.strptime(pelnaData, '%Y%m%d')
    except ValueError:
        print("Błędny format daty. Użyj formatu YYYYMMDD.")
        return None

# Funkcja obliczająca biorytmy
def obliczBiorytmy(t):
    # Obliczanie biorytmów (fizyczny, emocjonalny, intelektualny)
    yp = math.sin((2 * math.pi / 23) * t)  # Biorytm fizyczny (23 dni)
    ye = math.sin((2 * math.pi / 28) * t)  # Biorytm emocjonalny (28 dni)
    yi = math.sin((2 * math.pi / 33) * t)  # Biorytm intelektualny (33 dni)

    # Logika dla dobrego dnia
    if yp > 0.5 and ye > 0.5 and yi > 0.5:
        return "Gratulacje dobrego wyniku! To twój dobry dzień."
    
    # Sprawdzanie, czy jutro będzie lepiej
    yp_jutro = math.sin((2 * math.pi / 23) * (t + 1))
    ye_jutro = math.sin((2 * math.pi / 28) * (t + 1))
    yi_jutro = math.sin((2 * math.pi / 33) * (t + 1))
    
    if yp_jutro > yp and ye_jutro > ye and yi_jutro > yi:
        return "Jutro będzie lepiej!"
    else:
        return "Dziś może być trudniej, ale to się zmieni!"

# Główna część programu
print("Wpisz swoje imię:")
imie = input()

print("Wpisz rok urodzenia (np. 1995):")
rok = input()

print("Wpisz miesiąc urodzenia (np. 03):")
miesiac = input()

print("Wpisz dzień urodzenia (np. 21):")
dzien = input()

print("Cześć", imie)

# Łączenie wprowadzonego roku, miesiąca i dnia w jedną datę
pelnaData = rok + miesiac + dzien

# Konwersja daty
birth_date = convDate(pelnaData)

# Jeśli data została poprawnie skonwertowana
if birth_date:
    dzis = datetime.now()
    t = (dzis - birth_date).days  # Liczba dni od narodzin

    print(f"Data urodzenia: {birth_date.strftime('%Y-%m-%d')}")
    print(f"Liczba dni od urodzin: {t}")
    
    # Obliczenie biorytmów
    print(obliczBiorytmy(t))
