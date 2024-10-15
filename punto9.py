# Punto 9

class Temperatura:

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
  
  def get_temperatura(self, dia):
    temperatura = self.temperaturas_minimas[dia - 1]
    return temperatura

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
  
  dias = aux
  print("\nTemperaturas medias:")
  for dia in range(dias):
    print(f"\nDía {dia + 1}: {temperatura.get_temperatura_media(dia)}°")

  print("\nLos días con menor temperatura fueron:")
  for dia in range(dias):
    dia_menor_temperatura = temperatura.get_dia_menor_temperatura()
    temperatura = temperatura.get_temperatura(dia_menor_temperatura)
    print(f"\nDía {dia_menor_temperatura}: {temperatura}°")
    temperatura.temperaturas_minimas[dia_menor_temperatura - 1] = 1000


if __name__ == "__main__":
  main()