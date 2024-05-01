from interfaz.instruccion import instruccion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from entorno.entorno import entorno
from estructuras.errores import errores

class parse_float(instruccion):
    def __init__(self,expresion,linea,columna):
        self.expresion=expresion
        self.linea=linea
        self.columna=columna
    def execute(self,entorno):
     valor=self.expresion.execute(entorno)
     if valor!=None:
         if (isinstance(valor,str)):
             try:
                 return float(valor)
             except:
                 errores.agregar_error("No se pudo convertir el valor a number","ParseFloat",self.linea,self.columna,"Semantico")
                 return None
         else:
             errores.agregar_error("El valor no es de tipo string","ParseFloat",self.linea,self.columna,"Semantico")
             return None
         
        