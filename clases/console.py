from interfaz.instruccion import instruccion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from estructuras.instrucciones import salida_instrucciones
class console(instruccion):
 def __init__(self,expresion,linea,columna):
     self.expresion=expresion
     self.linea=linea
     self.columna=columna
 def traducir(self,entorno,gen):
     for exp in self.expresion:
            val = exp.traducir(entorno, gen)
            if (val.type == "NUMBER"):
                # Imprimiendo expresion
                gen.add_br()
                if 't' in str(val.value):
                    gen.add_move('t3', str(val.value))
                else:
                    gen.add_li('t3', str(val.value))
                gen.add_lw('a0', '0(t3)')
                gen.add_li('a7', '1')
                gen.add_system_call()
            elif (val.type == "STRING"):
                gen.add_br()
                if 't' in str(val.value) and len(str(val.value)) < 2:
                    gen.add_move('a0', str(val.value))
                else:
                    gen.add_la('a0', str(val.value))
                gen.add_li('a7', '4')
                gen.add_system_call()
            elif (val.type == "BOOLEAN"):
                   # Imprimiendo expresion
                gen.add_br()
                if 't' in str(val.value):
                    gen.add_move('t3', str(val.value))
                else:
                    gen.add_li('t3', str(val.value))
                gen.add_lw('a0', '0(t3)')
                gen.add_li('a7', '1')
                gen.add_system_call()
            elif (val.type == "CHAR"):
                gen.add_br()
                if 't' in str(val.value) and len(str(val.value)) < 2:
                    gen.add_move('a0', str(val.value))
                else:
                    gen.add_la('a0', str(val.value))
                gen.add_li('a7', '4')
                gen.add_system_call()
            elif (val.type == "FLOAT"):
                gen.add_br()
                gen.add_la('t0', str(val.value))
                gen.add_flw('fa0', '0(t0)')
                gen.add_li('a7', '2')
                
                gen.add_system_call()
                gen.add_li('a0', '10')
                gen.add_li('a7', '11')
                gen.add_system_call()
                return None
                
                
        # Imprimiendo salto de linea
     gen.add_br()
     gen.add_li('a0', '10')
     gen.add_li('a7', '11')
     gen.add_system_call()

     return None
 def execute(self,entorno):
     ins=""
     for exp in self.expresion:
         valor=exp.execute(entorno)
         if valor!=None:
             ins+=str(valor)
     salida_instrucciones.instrucciones+=ins+"\n"
     
