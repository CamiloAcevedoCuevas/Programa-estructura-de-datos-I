# Punto 9
# Desarrollado por: Camilo Andrés Acevedo Cuevas

class Dia:

    """
    Esta clase permite almacenar temperaturas máximas, mínimas e ideales de varios días.

    Métodos:
        add_temp_max(temp_max): Añade una temperatura máxima.
        add_temp_min(temp_min): Valida y añade una temperatura mínima.
        add_temp_idl(temp_idl): Añade una temperatura ideal.
        get_answer(): Retorna la cantidad de días ingresados.

    Atributos:
        temps_maxs: Lista de temperaturas máximas.
        temps_mins: Lista de temperaturas mínimas.
        temps_idls: Lista de temperaturas ideales.
        dia: Día actual.
        temp_max: Temperatura máxima actual.
        temp_min: Temperatura mínima actual.
        temp_idl: Temperatura ideal actual.
        temp_med: Temperatura media actual.
    """
    
    temps_maxs = []
    temps_mins = []
    temps_idls = []
    
    def __init__(self):
        self.dia = 1
        self.temp_max = None
        self.temp_min = None
        self.temp_idl = None
        self.temp_med = None

    def add_temp_max(self, temp_max):
        self.temps_maxs.append(temp_max)

    def add_temp_min(self, temp_min):
        temp = Temperatura()
        if float(temp.validar_temp(temp_min, "mínima")) > float(self.temp_max):
            temp_min = temp.validar_temp(input(f"\nError: La temperatura mínima no puede ser mayor que la máxima.\n\nIngrese la temperatura mínima: "), "mínima")
            self.add_temp_min(temp_min)
        else:
            self.temp_min = float(temp_min)
            self.temps_mins.append(self.temp_min)

    def add_temp_idl(self, temp_idl):
        self.temps_idls.append(temp_idl)
    
    def get_answer(self):
        while True:
            aux = input(f"\nIngresar datos día {self.dia + 1} ¿(0 = No, 1 = Sí)?: ")
            if aux == "0":
                dias = self.dia
                self.dia = 0
                return dias
            elif aux == "1":
                self.dia += 1
                break
            else:
                print("Error: Ingrese 0 o 1.")
    
class Temperatura:

    """
    Esta clase permite validar temperaturas y almacenar temperaturas medias.

    Métodos:
        get_val_temp(temp, str): Valida y retorna una temperatura.
        get_temp_med(dia): Retorna la temperatura media de un día.
        
    """
    
    def __init__(self):
        pass
    
    def validar_temp(self, temp, str):
        while True:
            try:
                isinstance(float(temp), float)
                return float(temp)
            except ValueError:
                temp = input(f"\nError: Ingrese un número.\n\nIngrese la temperatura {str}: ")
                continue
    
    def get_temp_med(self, d):
        dia = Dia()
        dia.temp_med = (dia.temps_maxs[d] + dia.temps_mins[d]) / 2
        return dia.temp_med
    
    
def main():
    dia = Dia()
    temp = Temperatura()
    
    # Ingresar temperaturas
    while dia.dia != 0:
        print("\nDía---", dia.dia)
        dia.temp_max = temp.validar_temp(input("\nIngrese la temperatura máxima: "), "máxima")
        dia.add_temp_max(dia.temp_max)
        dia.temp_min = temp.validar_temp(input("\nIngrese la temperatura mínima: "), "mínima")
        dia.add_temp_min(dia.temp_min)
        dia.temp_idl = temp.validar_temp(input("\nIngrese la temperatura ideal: "), "ideal")
        dia.add_temp_idl(dia.temp_idl)
        dias = dia.get_answer()

    # Mostrar temperaturas medias
    print("_________________________________________________\n\nTemperaturas medias:\n")
    for d in range(dias):
        dia.temp_med = temp.get_temp_med(d)
        print(f"Día--- {d + 1}: {dia.temp_med}°\n")

    # Mostrar días con menor temperatura
    print("_________________________________________________\n\nDías con menor temperatura:\n")
    sorted = list(dia.temps_mins)
    sorted.sort()
    for d in range(dias):
        print(f"Día--- {d + 1}: {sorted[d]}°\n")

    # Buscar día(s) con temperatura máxima
    temp_max = temp.validar_temp(input("_________________________________________________\n\nIngrese la temperatura máxima a buscar: "), "máxima a buscar")
    if float(temp_max) in dia.temps_maxs:
        print(f"_________________________________________________\n\nDía(s) con temperatura máxima = {temp_max}°:\n")
        for d in range(dias):
            if float(temp_max) == dia.temps_maxs[d]:
                print(f"Día--- {d + 1}\n")
    else:
        print(f"_________________________________________________\n\nNo hay días con temperatura máxima = {temp_max}°.\n")

if __name__ == "__main__":
    main()