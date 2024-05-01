from interfaz.instruccion import instruccion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from entorno.entorno import entorno

class matriz(instruccion):
 def __init__(self,tipo,tipo_dato,nombre,dimensiones,valores,linea,columna):
     self.tipo=tipo
     self.tipo_dato=tipo_dato
     self.nombre=nombre
     self.valores=valores
     self.dimensiones=dimensiones
     self.linea=linea
     self.columna=columna
     

     
     
 
    
