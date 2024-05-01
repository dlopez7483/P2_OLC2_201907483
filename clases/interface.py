from interfaz.instruccion import instruccion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from entorno.entorno import entorno

class interface(instruccion):
 def __init__(self,nombre,at,linea,columna):
     self.nombre=nombre
     self.at=at
     self.atributos={}
     self.linea=linea
     self.columna=columna
 def execute(self,Entorno):
     for a in self.at:
         self.atributos[a.nombre]=a.tipo
     Entorno.agregar_interface(self.nombre,self.atributos)
     
     