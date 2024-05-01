from interfaz.instruccion import instruccion
from interfaz.expresion import expresion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from entorno.entorno import entorno
from estructuras.errores import errores
class Tostring(instruccion):
    def __init__(self,expresion,linea,columna):
        self.expresion=expresion
        self.linea=linea
        self.columna=columna
    def execute(self,entorno):
     valor = None
     if isinstance(self.expresion,expresion) | isinstance(self.expresion,instruccion):
         valor = self.expresion.execute(entorno)
     elif isinstance(self.expresion,str):
         valor=entorno.buscar_simbolo(self.expresion).valor
     
     if valor!=None:
         try:
             if (isinstance(valor,str),isinstance(valor,int),isinstance(valor,float),isinstance(valor,bool)):
                 return str(valor)
         except:
             errores.agregar_error('No se pudo convertir a string','To String',self.linea,self.columna,'Semantico')
             return None
     else:
         return None
    def traducir(self,entorno,gen):
     return None