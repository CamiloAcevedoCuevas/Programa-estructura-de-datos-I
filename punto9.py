# Punto 9
# Desarrollado por: Camilo Andrés Acevedo Cuevas

class Temperatura:

  """_Summary_
  Esta clase permite almacenar temperaturas máximas, mínimas e ideales de varios días y realizar operaciones con ellas.

  Returns:
      add_temperatura_maxima: Añade una temperatura máxima a la lista de temperaturas máximas.
      add_temperatura_minima: Añade una temperatura mínima a la lista de temperaturas mínimas.
      add_temperatura_ideal: Añade una temperatura ideal a la lista de temperaturas ideales.
      get_temperatura_media: Devuelve la temperatura media de un día.
      get_dia_menor_temperatura: Debuelve el día con la menor temperatura mínima.
      get_temperatura_minima: Devuelve la temperatura mínima de un día.
  """

  temperaturas_maximas = []
  temperaturas_minimas = []
  temperaturas_ideales = []
  
  def __init__(self):
    self.temperaturas_maximas = []
    self.temperaturas_minimas = []
    self.temperaturas_ideales = []

  def add_temperatura_maxima(self):
    temperatura_maxima = float(input("Ingrese la temperatura máxima: "))
    self.temperaturas_maximas.append(temperatura_maxima)

  def add_temperatura_minima(self):
    temperatura_minima = float(input("Ingrese la temperatura mínima: "))
    self.temperaturas_minimas.append(temperatura_minima)

  def add_temperatura_ideal(self):
    temperatura_ideal = float(input("Ingrese la temperatura ideal: "))
    self.temperaturas_ideales.append(temperatura_ideal)

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

    temperatura.add_temperatura_maxima()
    temperatura.add_temperatura_minima()
    temperatura.add_temperatura_ideal()

    print("\n¿Desea ingresar datos de otro día? (0 = No, 1 = Sí)")
    aux = input()
    if aux == "0":
      aux = dia
      dia = 0
    else:
      dia += 1
  
  # Mostrar temperaturas medias
  dias = aux
  print("\nTemperaturas medias:")
  for dia in range(dias):
    print(f"Día {dia + 1}: {temperatura.get_temperatura_media(dia)}°")

  # Mostrar días con menor temperatura
  print("\nDías con menor temperatura:")
  for dia in range(dias):
    dia_menor_temperatura = temperatura.get_dia_menor_temperatura()
    temperatura_minima = temperatura.get_temperatura_minima(dia_menor_temperatura)
    print(f"Día {dia_menor_temperatura}: {temperatura_minima}°")
    temperatura.temperaturas_minimas[dia_menor_temperatura - 1] = float(1000)

  # Buscar día(s) con temperatura máxima
  print("\nIngrese la temperatura máxima a buscar:")
  temperatura_maxima = float(input())
  if temperatura_maxima in temperatura.temperaturas_maximas:
    print(f"\nDía(s) con temperatura máxima = {temperatura_maxima}°:")
    for dia in range(dias):
      if temperatura_maxima == temperatura.temperaturas_maximas[dia]:
        print(f"Día {dia + 1}")
  else:
    print(f"\nNo hay días con temperatura máxima = {temperatura_maxima}°.")

if __name__ == "__main__":
  main()