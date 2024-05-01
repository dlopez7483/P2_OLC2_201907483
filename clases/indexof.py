from interfaz.instruccion import instruccion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from entorno.entorno import entorno
from estructuras.errores import errores
class indexof(instruccion):
 def __init__(self,id,expresion,linea,columna):
     self.id=id
     self.expresion=expresion
     self.linea=linea
     self.columna=columna
     
 def execute(self,Entorno):
     simbolo = Entorno.buscar_simbolo(self.id)
     valor=self.expresion.execute(Entorno)
     if simbolo != None:
         
         if (isinstance(simbolo.valor,list)):
                 if len(simbolo.valor)>0:
                     if valor in simbolo.valor:
                         return simbolo.valor.index(valor)
                     else:
                         return -1
                 else:
                     return -1
         else:
                errores.agregar_error("El valor "+self.id+" no es de tipo lista","IndexOf "+Entorno.nombre,self.linea,self.columna,"Semantico")
                return None
      