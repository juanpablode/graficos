class Shape:
  """
  Una forma en ASCII.

  Attributes:
    tamaño: El tamaño de la forma en caracteres.
  """

  def __init__(self, tamaño):
    self.tamaño = tamaño

  def dibujar(self):
    raise NotImplementedError()

class Linea(Shape):
  """
  Una línea en ASCII.

  Attributes:
    tamaño: El tamaño de la línea en caracteres.
  """

  def __init__(self, tamaño):
    super().__init__(tamaño)

  def dibujar(self):
    for i in range(self.tamaño):
      print("*", end="")

class Cuadrado(Shape):
  """
  Un cuadrado en ASCII.

  Attributes:
    tamaño: El tamaño del cuadrado en caracteres.
  """

  def __init__(self, tamaño):
    super().__init__(tamaño)

  def dibujar(self):
    def dibujar_linea(linea):
      for i in range(linea.tamaño):
        print("*", end="")

    for i in range(self.tamaño):
      dibujar_linea(Linea(self.tamaño))
      print()

    for i in range(self.tamaño - 2):
      dibujar_linea(Linea(1))
      print(" " * (self.tamaño - 2))
      dibujar_linea(Linea(1))

    dibujar_linea(Linea(self.tamaño))

if __name__ == "__main__":
  tamaño = int(input("Ingrese el tamaño del cuadrado: "))
  cuadrado = Cuadrado(tamaño)
  cuadrado.dibujar()
