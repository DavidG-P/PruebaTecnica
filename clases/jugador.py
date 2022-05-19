

class Jugador:
  def __init__(self, nombres, apellidos):
    self.__nombres = nombres
    self.__apellidos = apellidos

  def descripcion(self):
    print("Nombre:",self.__nombres , ", edad:", self.__apellidos)

