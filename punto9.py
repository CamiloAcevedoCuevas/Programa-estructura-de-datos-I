class Dia:
    """Esta clase permite almacenar temperaturas máximas, mínimas, ideales y medias de varios días."""
#hola
    temps_maxs = []
    temps_mins = []
    temps_idls = []
    temps_meds = []

    def __init__(self):
        self.dia = 1
        self.num_dias = 1
        self.temp_max = None
        self.temp_min = None
        self.temp_idl = None
        self.temp_med = None

    def add_temp_max(self, temp):
        """Añade una temperatura máxima.

        Args:
            temp (float): Temperatura máxima a añadir.
        """
        self.temps_maxs.append(temp)

    def add_temp_min(self, temp_min):
        """ Valida y añade una temperatura mínima.

        Args:
            temp_min (float): Temperatura mínima a añadir.
        """
        temp = Temperatura()
        if float(temp.validar_temp(temp_min, "mínima")) > float(self.temp_max):
            temp_min = temp.validar_temp(input(f"\nError: La temperatura mínima no puede ser mayor que la máxima.\n\nIngrese la temperatura mínima: "), "mínima")
            self.add_temp_min(temp_min)
        else:
            self.temp_min = float(temp_min)
            self.temps_mins.append(self.temp_min)

    def add_temp_idl(self, temp):
        """Añade una temperatura ideal."""
        self.temps_idls.append(temp)

    def add_temp_med(self, temp):
        """Añade una temperatura media."""
        self.temps_meds.append(temp)

    def set_dia(self):
        """Pregunta si se desea ingresar datos de un nuevo día."""
        aux = input(f"\nIngresar datos día {self.dia + 1} ¿(0 = No, 1 = Sí)?: ")
        if aux == "0":
            self.dia = 0
        elif aux == "1":
            self.dia += 1
            self.num_dias += 1
        else:
            print("\nError: Ingrese 0 o 1.")
            self.set_dia()

    def get_dia_men_temp(self, temp):
        """Retorna el día con la menor temperatura ingresada."""
        if temp == self.temps_mins[self.dia]:
            return self.dia + 1
        else:
            self.dia += 1
            return self.get_dia_men_temp(temp)

class Temperatura:
    """Esta clase permite validar temperaturas y conseguir temperaturas medias."""
    def __init__(self):
        pass
    
    def validar_temp(self, temp, str):
        """Valida y retorna una temperatura.

        Args:
            temp (float): Temperatura a validar.
            str (str): Cadena que indica el tipo de temperatura.

        Returns:
            temp: Temperatura validada.
        """
        try:
            isinstance(float(temp), float)
            return float(temp)
        except ValueError:
            return self.validar_temp(input(f"\nError: Ingrese un número.\n\nIngrese la temperatura {str}: "), str)
        
    def get_temp_med(self, d):
        """Retorna la temperatura media de un día.

        Args:
            d (int): Día del que se desea obtener la temperatura media.

        Returns:
            dia.temp_med: Día con la temperatura media.
        """
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
        dia.set_dia()

    # Mostrar temperaturas medias
    print("_________________________________________________\n\nTemperaturas medias:\n")
    for d in range(dia.num_dias):
        dia.add_temp_med(temp.get_temp_med(d))
        print(f"Día--- {d + 1}: {dia.temps_meds[d]}°\n")

    # Mostrar días con menor temperatura
    print("_________________________________________________\n\nDías con menor temperatura:\n")
    sorted = list(dia.temps_mins)
    sorted.sort()
    for i in range(dia.num_dias):
        dia.dia = dia.get_dia_men_temp(sorted[i])
        print(f"Día--- {dia.dia}: {sorted[i]}°\n")
        dia.dia = 0

    # Buscar día(s) con temperatura máxima
    dia.temp_max = temp.validar_temp(input("_________________________________________________\n\nIngrese la temperatura máxima a buscar: "), "máxima a buscar")
    if float(dia.temp_max) in dia.temps_maxs:
        print(f"_________________________________________________\n\nDía(s) con temperatura máxima = {dia.temp_max}°:\n")
        for d in range(dia.num_dias):
            if float(dia.temp_max) == dia.temps_maxs[d]:
                print(f"Día--- {d + 1}\n")
    else:
        print(f"_________________________________________________\n\nNo hay días con temperatura máxima = {dia.temp_max}°.\n")

if __name__ == "__main__":
    main()
