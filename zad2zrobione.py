import math
import matplotlib.pyplot as plt
import random

# Przyspieszenie grawitacyjne
g = 9.81  # przyspieszenie grawitacyjne w m/s^2

# Funkcja do obliczania zasięgu pocisku
def oblicz_traektorie(v, h, kat):
    kat_rad = math.radians(kat)  # zamiana kąta na radiany
    
    # Równania ruchu
    t_max = (v * math.sin(kat_rad) + math.sqrt((v * math.sin(kat_rad))**2 + 2 * g * h)) / g  # czas lotu
    x = v * math.cos(kat_rad) * t_max  # zasięg poziomy
    
    return x, t_max

# Generowanie losowego celu w zakresie 50 - 340 m
cel = random.randint(50, 340)
print(f"Cel: {cel} m (z marginesem błędu 5 m)")

# Ustalona prędkość i wysokość
v = 50  # prędkość początkowa (m/s)
h = 100  # wysokość początkowa (m)

# Petla nieskończona do próbowania
proby = 0
while True:
    # Pobranie kąta od użytkownika
    kat = float(input("Podaj kąt wyrzutu (w stopniach): "))
    
    # Obliczanie zasięgu
    x, _ = oblicz_traektorie(v, h, kat)
    
    # Sprawdzanie, czy trafił w cel
    proby += 1
    if abs(x - cel) <= 5:
        print(f"Cel trafiony! Liczba prób: {proby}")
        break
    else:
        print(f"Chybione! Zasięg: {x:.2f} m. Spróbuj ponownie.")

    # Rysowanie trajektorii
    t_max = (v * math.sin(math.radians(kat)) + math.sqrt((v * math.sin(math.radians(kat)))**2 + 2 * g * h)) / g
    t_points = [i * t_max / 100 for i in range(101)]
    x_points = [v * math.cos(math.radians(kat)) * t for t in t_points]
    y_points = [h + v * math.sin(math.radians(kat)) * t - 0.5 * g * t**2 for t in t_points]
    
    plt.figure(figsize=(8, 6))
    plt.plot(x_points, y_points, label=f"Kąt = {kat}°")
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(cel, color='red', linestyle='--', label=f"Cel: {cel} m")
    plt.xlabel('Odległość (m)')
    plt.ylabel('Wysokość (m)')
    plt.title('Trajektoria lotu pocisku')
    plt.legend()
    plt.grid(True)
    plt.xlim(0, max(x_points) + 50)
    plt.ylim(0, max(y_points) + 10)
    plt.savefig('trajektoria.png')
    plt.show()

#czas spedzony: 8 minut bo byl blad