from interfaz.instruccion import instruccion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from estructuras.errores import errores
class Return(instruccion):
    def __init__(self,expresion,linea,columna):
        self.expresion=expresion
        self.linea=linea
        self.columna=columna
    def execute(self,Entorno):
        if (Entorno.encontrar_entorno("funcion")==None):
         errores.agregar_error("Return fuera de una funcion","funcion",self.linea,self.columna,"Semantico")
         print("Return fuera de una funcion")
         return None
        else:
         return self