# Punto 9
# Desarrollado por: Camilo Andrés Acevedo Cuevas

class Temperatura:
    """
    Esta clase permite almacenar temperaturas máximas, mínimas e ideales de varios días y realizar operaciones con ellas.

    Métodos:
        add_temperatura_maxima(): Valida y añade una temperatura máxima a la lista de temperaturas máximas.
        add_temperatura_minima(): Valida y añade una temperatura mínima a la lista de temperaturas mínimas.
        add_temperatura_ideal(): Valida y añade una temperatura ideal a la lista de temperaturas ideales.
        get_temperatura_media(dia): Devuelve la temperatura media de un día.
        get_dia_menor_temperatura(): Devuelve el día con la menor temperatura mínima.
        get_temperatura_minima(dia): Devuelve la temperatura mínima de un día.
    """
  
    def __init__(self):
        self.temperaturas_maximas = []
        self.temperaturas_minimas = []
        self.temperaturas_ideales = []

    def add_temperatura_maxima(self):
        while True:
            try:
                temperatura_maxima = float(input("Ingrese la temperatura máxima:\n"))
                self.temperaturas_maximas.append(temperatura_maxima)
            except ValueError:
                print("Error: Ingrese un número.\n")
                continue
            else:
                break

    def add_temperatura_minima(self):
        while True:
            try:
                temperatura_minima = float(input("Ingrese la temperatura mínima:\n"))
                if temperatura_minima > self.temperaturas_maximas[len(self.temperaturas_maximas) - 1]:
                    print("Error: La temperatura mínima no puede ser mayor que la temperatura máxima.\n")
                    continue
                self.temperaturas_minimas.append(temperatura_minima)
            except ValueError:
                print("Error: Ingrese un número.\n")
                continue
            else:
                break

    def add_temperatura_ideal(self):
        while True:
            try:
                temperatura_ideal = float(input("Ingrese la temperatura ideal:\n"))
                self.temperaturas_ideales.append(temperatura_ideal)
            except ValueError:
                print("Error: Ingrese un número.\n")
                continue
            else:
                break

    def get_temperatura_media(self, dia):
        temperatura_media = (self.temperaturas_maximas[dia] + self.temperaturas_minimas[dia]) / 2
        return temperatura_media
  
    def get_dia_menor_temperatura(self):
        dia_menor_temperatura = self.temperaturas_minimas.index(min(self.temperaturas_minimas)) + 1
        return dia_menor_temperatura
  
    def get_temperatura_minima(self, dia):
        temperatura_minima = self.temperaturas_minimas[dia - 1]
        return temperatura_minima

# Main
def main():
    temperatura = Temperatura()

    dia = 1
    while dia != 0:
        print(f"\nDía {dia}\n")

        # Ingresar temperaturas
        temperatura.add_temperatura_maxima()
        temperatura.add_temperatura_minima()
        temperatura.add_temperatura_ideal()

        while True:
            aux = input(f"\nIngresar datos día {dia + 1} (0 = No, 1 = Sí)\n")
            if aux == "0":
                aux = dia
                dia = 0
                break
            elif aux == "1":
                dia += 1
                break
            else:
                print("Error: Ingrese 0 o 1.")

    # Mostrar temperaturas medias
    dias = aux
    print("\nTemperaturas medias:")
    for dia in range(dias):
        print(f"Día--- {dia + 1}: {temperatura.get_temperatura_media(dia)}°")

    # Mostrar días con menor temperatura
    print("\nDías con menor temperatura:")
    sorted = list(temperatura.temperaturas_minimas)
    sorted.sort()
    for dia in range(dias):
        print(f"Día--- {dia + 1}: {sorted[dia]}°")

    # Buscar día(s) con temperatura máxima
    print("\nIngrese la temperatura máxima a buscar:\n")
    temperatura_maxima = float(input())
    if temperatura_maxima in temperatura.temperaturas_maximas:
        print(f"\nDía(s) con temperatura máxima = {temperatura_maxima}°:")
        for dia in range(dias):
            if temperatura_maxima == temperatura.temperaturas_maximas[dia]:
                print("Día---", dia + 1)
    else:
        print(f"\nNo hay días con temperatura máxima = {temperatura_maxima}°.")

if __name__ == "__main__":
    main()