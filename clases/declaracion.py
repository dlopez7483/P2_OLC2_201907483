from interfaz.instruccion import instruccion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from entorno.entorno import entorno
from estructuras.errores import errores
##tipo,tipo_dato, valor, fila, columna

class declaracion(instruccion):
 def __init__(self,tipo,tipo_dato,id,valor, linea, columna):
     self.tipo = tipo
     self.tipo_dato = tipo_dato
     self.id = id
     self.valor = valor
     self.linea = linea
     self.columna = columna  
     
     
 def execute(self,entorno):
     
     if self.valor != None:
         valor = self.valor.execute(entorno)
         if self.tipo_dato == 'NUMBER' and isinstance(valor,int):
             entorno.agregar_simbolo(self.id,self.tipo,self.tipo_dato,valor,'',self.linea,self.columna)
         elif self.tipo_dato == 'FLOAT' and isinstance(valor,float):
             entorno.agregar_simbolo(self.id,self.tipo,self.tipo_dato,valor,'',self.linea,self.columna)
         elif self.tipo_dato == 'STRING' and isinstance(valor,str):
             entorno.agregar_simbolo(self.id,self.tipo,self.tipo_dato,valor,'',self.linea,self.columna)
         elif self.tipo_dato == 'BOOLEAN' and isinstance(valor,bool):
             entorno.agregar_simbolo(self.id,self.tipo,self.tipo_dato,valor,'',self.linea,self.columna)
         elif self.tipo_dato == 'CHAR' and isinstance(valor,str) and len(valor) == 1:
             print("entro a char")
             entorno.agregar_simbolo(self.id,self.tipo,self.tipo_dato,valor,self.linea,self.columna)
         elif self.tipo_dato == 'FLOAT' and isinstance(valor,int):
             entorno.agregar_simbolo(self.id,self.tipo,self.tipo_dato,valor,'',self.linea,self.columna)
         else:
             entorno.agregar_simbolo(self.id,self.tipo,self.tipo_dato,valor,'',self.linea,self.columna)

            
             
        
         
    
     else:
         if self.tipo_dato == 'NUMBER':
             entorno.agregar_simbolo(self.id,self.tipo,self.tipo_dato,valor,'',self.linea,self.columna)
         elif self.tipo_dato =='FLOAT':
             entorno.agregar_simbolo(self.id,self.tipo,self.tipo_dato,valor,'',self.linea,self.columna)
         elif self.tipo_dato == 'STRING':
             entorno.agregar_simbolo(self.id,self.tipo,self.tipo_dato,valor,'',self.linea,self.columna)
         elif self.tipo_dato == 'BOOLEAN':
             entorno.agregar_simbolo(self.id,self.tipo,self.tipo_dato,False,self.linea,self.columna)
         elif self.tipo_dato == 'CHAR':
             entorno.agregar_simbolo(self.id,self.tipo,self.tipo_dato,"",self.linea,self.columna)
             
             
     return None
        
     
     
##self,nombre,tipo,tipo_dato, valor, fila, columna
 def traducir(self,entorno,gen):
     val=self.valor
     if val.tipo== self.tipo_dato:
         gen.add_br()
         if self.tipo_dato=="NUMBER":
             gen.variable_data(self.id, 'word', str(self.valor.valor))
         elif self.tipo_dato=="STRING":
             gen.variable_data(self.id, 'string', '\"'+str(self.valor.valor)+'\"')
         elif self.tipo_dato=="BOOLEAN":
             val=self.valor.valor
             if val == True:
                 gen.variable_data(self.id, 'word', '1')
             elif val == False:
                 gen.variable_data(self.id, 'word', '0')
         elif self.tipo_dato=="FLOAT":
             gen.variable_data(self.id, 'float', str(self.valor.valor))
         elif self.tipo_dato=="CHAR":
             gen.variable_data(self.id, 'byte', str(self.valor.valor))
         entorno.agregar_simbolo(self.id,self.tipo,self.tipo_dato,self.valor.valor,"",self.linea,self.columna)
             
         
     
     
     gen.add_br()
     

            
             

    