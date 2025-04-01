import math
from datetime import date, datetime
def convDate(pelnaData):
    format = '%Y%m%d'
    return datetime.strptime(pelnaData, format)

print("Wpisz swoje: imie ")
imie = input()
print("Wpisz rok urodzenia")
rok = input()
print("Wpisz miesiac urodzenia")
miesiac = input()
print("Wpisz dzien urodzenia")
dzien = input()
print("Cześć", imie)


pelnaData = rok + miesiac + dzien
birth_date = convDate(pelnaData)
dzis = datetime.now()
t = (dzis - birth_date).days



print(f"Data urodzenia: {birth_date.strftime('%Y-%m-%d')}")
print(f"Liczba dni od urodzin: {t}")
def obliczBiorytmy(t):
    yp = math.sin((2*math.pi)*t/23)
    ye = math.sin((2*math.pi)*t/28)
    yi = math.sin((2*math.pi)*t/33)
    if yp > 0.5 and ye > 0.5 and yi > 0.5:
        return ("Gratulacje dobrego wyniku")
    else:
        yp_jutro = math.sin(((2 * math.pi) / 23) * (t + 1))
        ye_jutro = math.sin(((2 * math.pi) / 28) * (t + 1))
        yi_jutro = math.sin(((2 * math.pi) / 33) * (t + 1))
        
        if yp_jutro > yp and ye_jutro > ye and yi_jutro > yi:
            return "Jutro będzie lepiej!"
        else:
            return "Dziś może być trudniej, ale to się zmieni!"


    
print(obliczBiorytmy(t))

# CZas spędzony: 36 minut, czas z czatemGPT: 3 minuty, bez poprawek potrzebnych