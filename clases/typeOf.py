from interfaz.instruccion import instruccion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from entorno.entorno import entorno
from estructuras.errores import errores
class typeOf(instruccion):
    def __init__(self,expresion,linea,columna):
        self.expresion=expresion
        self.linea=linea
        self.columna=columna
    def execute(self,entorno):
     valor = self.expresion.execute(entorno)
     
     print(valor)
     print(type(valor))
     
     if valor!=None:
         if (isinstance(valor,bool)):
             print(valor)
             return "boolean"
         elif (isinstance(valor,float)):
             return "float"
         elif (isinstance(valor,str)):
             if len(valor)==1:
                 return "char"
             return "string"
         elif (isinstance(valor,int)):
             return "number"
         elif (isinstance(valor,list)):
             return "array"
     else:
         #descripcion,ambito,linea,columna,tipo
         errores.agregar_error('No se puede obtener el tipo de dato', 'typeOf',self.linea,self.columna,'Semantico')
         return None
    
    def traducir(self,entorno,gen):
        return None