
class Pregunta:

  def __init__(self, id, descripcion,nivel,categoria):
    self.__id  = id
    self.__descripcion  = descripcion
    self.__nivel = nivel
    self.__categoria   = categoria

  def dime_descripcion(self):
      return self.__descripcion
      
  def dime_id(self):
      return self.__id

  def dime_nivel(self):
      return self.__nivel

  def dime_categoria(self):
      return self.__categoria

