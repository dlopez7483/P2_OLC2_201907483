from interfaz.expresion import expresion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from entorno.value import Value
class primitivo(expresion):
 def __init__(self,valor,tipo,linea,columna):
     self.valor=valor
     self.tipo=tipo
     self.linea=linea
     self.columna=columna
 def traducir(self, entorno,gen):
     temp=gen.new_temp() 
     print(self.tipo)
     if (self.tipo=="NUMBER"):
         
         gen.add_br()
         gen.comment('Agregando un primitivo numerico')
         gen.add_li('t0', str(self.valor))
         gen.add_li('t3', str(temp))
         gen.add_sw('t0', '0(t3)')
         return Value(str(temp), True, self.tipo, [], [], [])
     elif (self.tipo=="STRING"):
         nameId = 'str_'+str(temp)
         gen.variable_data(nameId, 'string', '\"'+str(self.valor)+'\"')
         return  Value(nameId, False, self.tipo, [], [], [])
     elif (self.tipo=="BOOLEAN"):
         gen.add_br()
         gen.comment('Agregando un primitivo booleano')
         valor=0
         if self.valor==True:
             valor=1
         gen.add_br()
         gen.add_li('t0', str(valor))
         gen.add_li('t3', str(temp))
         gen.add_sw('t0', '0(t3)')
         
         
         gen.comment('Fin de primitivo booleano')
         return Value(str(temp), True, self.tipo, [], [], [])
     elif(self.tipo=="CHAR"):
         nameId = 'str_'+str(temp)
         gen.variable_data(nameId, 'string', '\"'+str(self.valor)+'\"')
         return  Value(nameId, False, self.tipo, [], [], [])
     
     elif (self.tipo=="FLOAT"):
            gen.add_br()
            gen.comment('Agregando un primitivo float')
            gen.variable_data('floa_'+str(temp), 'float', str(self.valor))
            return Value('floa_'+str(temp), False, self.tipo, [], [], [])
 def execute(self, entorno): 
     return self.valor            