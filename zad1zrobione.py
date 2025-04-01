import math
from datetime import datetime, timedelta

def oblicz_biorytm(dni_od_urodzin, cykl):
    """Funkcja obliczająca wartość biorytmu na podstawie liczby dni od urodzin i cyklu"""
    return math.sin((2 * math.pi * dni_od_urodzin) / cykl)

def oblicz_dni_od_urodzin(data_urodzenia):
    """Funkcja obliczająca dni od urodzin do dzisiejszego dnia"""
    dzisiaj = datetime.now()
    return (dzisiaj - data_urodzenia).days

def oblicz_biorytmy(data_urodzenia):
    """Funkcja obliczająca biorytmy: fizyczny, emocjonalny, intelektualny"""
    dni_od_urodzin = oblicz_dni_od_urodzin(data_urodzenia)
    
    fizyczny = oblicz_biorytm(dni_od_urodzin, 23)
    emocjonalny = oblicz_biorytm(dni_od_urodzin, 28)
    intelektualny = oblicz_biorytm(dni_od_urodzin, 33)
    
    return fizyczny, emocjonalny, intelektualny

def oblicz_biorytmy_na_jutro(data_urodzenia):
    """Funkcja obliczająca biorytmy na jutro"""
    dni_od_urodzin = oblicz_dni_od_urodzin(data_urodzenia) + 1
    
    fizyczny = oblicz_biorytm(dni_od_urodzin, 23)
    emocjonalny = oblicz_biorytm(dni_od_urodzin, 28)
    intelektualny = oblicz_biorytm(dni_od_urodzin, 33)
    
    return fizyczny, emocjonalny, intelektualny

def main():
    # Pobranie danych od użytkownika
    imie = input("Podaj swoje imię: ")
    rok = int(input("Podaj rok urodzenia: "))
    miesiac = int(input("Podaj miesiąc urodzenia: "))
    dzien = int(input("Podaj dzień urodzenia: "))
    
    # Ustalenie daty urodzenia
    data_urodzenia = datetime(rok, miesiac, dzien)
    
    # Obliczanie biorytmów na dzisiaj
    fizyczny, emocjonalny, intelektualny = oblicz_biorytmy(data_urodzenia)
    
    print(f"\nWitaj {imie}!")
    print(f"Biorytmy na dziś:")
    print(f"Fizyczny: {fizyczny:.4f}")
    print(f"Emocjonalny: {emocjonalny:.4f}")
    print(f"Intelektualny: {intelektualny:.4f}")
    
    # Sprawdzenie, czy biorytmy są powyżej 0.5
    if fizyczny > 0.5 and emocjonalny > 0.5 and intelektualny > 0.5:
        print("\nGratulacje, Twoje biorytmy są bardzo pozytywne!")
    else:
        # Obliczanie biorytmów na jutro
        fizyczny_jutro, emocjonalny_jutro, intelektualny_jutro = oblicz_biorytmy_na_jutro(data_urodzenia)
        
        print("\nBiorytmy na jutro:")
        print(f"Fizyczny: {fizyczny_jutro:.4f}")
        print(f"Emocjonalny: {emocjonalny_jutro:.4f}")
        print(f"Intelektualny: {intelektualny_jutro:.4f}")
        
        # Porównanie dzisiejszych i jutrzejszych wyników
        if (fizyczny_jutro > fizyczny and emocjonalny_jutro > emocjonalny and intelektualny_jutro > intelektualny):
            print("\nJutro będzie lepiej!")
        else:
            print("\nJutro będzie gorzej...")

# Uruchomienie programu
if __name__ == "__main__":
    main()
