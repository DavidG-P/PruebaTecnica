class Respuesta:
  def __init__(self, id, opcion,preguntaId,isTrue):
    self.__id  = id
    self.__opcion  = opcion
    self.__preguntaId = preguntaId
    self.__isTrue   = isTrue
 
  def dime_opcion(self):
      return self.__opcion
      
  def dime_id(self):
      return self.__id

  def dime_preguntaId(self):
      return self.__preguntaId

  def dime_isTrue(self):
      return self.__isTrue
  
