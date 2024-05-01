from interfaz.instruccion import instruccion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from entorno.entorno import entorno
from estructuras.errores import errores
from interfaz.expresion import expresion
class UpperCase(instruccion):
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
        #descripcion,ambito,linea,columna,tipo
        if (isinstance(valor,str)):
             return valor.upper()
        else:
             errores.agregar_error('No se puede convertir a mayusculas','Upper Case',self.linea,self.columna,'Semantico')
             return None
    def traducir(self,entorno,gen):
     return None
        