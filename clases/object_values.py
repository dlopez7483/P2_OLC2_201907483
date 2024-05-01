from interfaz.expresion import expresion
from estructuras.errores import errores

class object_values(expresion):
 def __init__(self, id, linea, columna):
     self.id = id
     self.linea = linea
     self.columna = columna
 def execute(self, Entorno):
     simbolo = Entorno.buscar_simbolo(self.id)
     if simbolo != None and isinstance(simbolo.valor,dict):
         return list(simbolo.valor.values())
     else:
         errores.agregar_error("El objeto no existe o no es un objeto","Object_Values "+Entorno.nombre,self.linea,self.columna,"Semantico")
         return None