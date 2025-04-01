import numpy as np
import math
import matplotlib.pyplot as plt
import random

h = 100
g = 10
v0 = 50

def oblicz_czas_lotu(alfa_radiany):
    a = -0.5 * g
    b = v0 * math.sin(alfa_radiany)
    c = h
    delta = b**2 - 4 * a * c
    if delta < 0:
        return None
    t1 = (-b + math.sqrt(delta)) / (2 * a)
    t2 = (-b - math.sqrt(delta)) / (2 * a)
    return max(t1, t2)

def oblicz_trajektorie(alfa_radiany, t):
    time_points = np.linspace(0, t, num=500)
    x = v0 * math.cos(alfa_radiany) * time_points
    y = h + v0 * math.sin(alfa_radiany) * time_points - 0.5 * g * time_points**2
    return x, y

def rysuj_wykres(x, y, cel, trafiony):
    plt.figure()
    plt.plot(x, y, label="Trajektoria pocisku")
    plt.axhline(0, color="gray", linestyle="--", label="Ziemia")
    plt.axvline(cel, color="red", linestyle="--", label="Cel")
    plt.xlabel("Odległość [m]")
    plt.ylabel("Wysokość [m]")
    plt.title("Trajektoria pocisku z Trebusza")
    plt.legend()
    plt.grid()
    if trafiony:
        plt.savefig('trajektoria_trafiony.jpg')
    else:
        plt.savefig('trajektoria_nie_trafiony.jpg')
    plt.show()

def sprawdz_trafienie(R, cel):
    if cel - 10 <= R <= cel + 10:
        return True
    return False

def main():
    cel = random.randint(50, 320)
    print("CEL:", cel)

    while True:
        alfa = int(input("Podaj kąt wyrzutu w stopniach: "))
        alfa_radiany = math.radians(alfa)

        t = oblicz_czas_lotu(alfa_radiany)
        if t is None:
            print("Brak rzeczywistych rozwiązań - pocisk nie dotrze do ziemi.")
            continue

        x, y = oblicz_trajektorie(alfa_radiany, t)
        R = v0 * math.cos(alfa_radiany) * t
        
        trafiony = sprawdz_trafienie(R, cel)

        if trafiony:
            print("Trafiony!")
        else:
            print("Nie trafiłeś!")

        print(f"Pocisk przeleciał {R:.2f} metrów")

        rysuj_wykres(x, y, cel, trafiony)

        if trafiony:
            break

if __name__ == "__main__":
    main()

#czas spedzony: 42 min