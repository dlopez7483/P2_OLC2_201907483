from interfaz.instruccion import instruccion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from entorno.entorno import entorno
from estructuras.instrucciones import salida_instrucciones
from clases.Break import Break
from clases.Continue import Continue
from clases.Return import Return
from entorno.entornos import entornos
from estructuras.errores import errores
from clases.operacion import operacion
from clases.id import id
class While(instruccion):
 def __init__(self,condicion,instrucciones,linea,columna):
     self.condicion = condicion
     self.instrucciones = instrucciones
     self.linea = linea
     self.columna = columna
     self.Entorno=None
     
 def traducir(self,Entorno,gen):
     
     if isinstance(self.condicion,operacion):
          
        
         izq=self.condicion.izq
         der=self.condicion.der
         operador=self.condicion.operador
         gen.comment('Inicio While')
         While_="While"+str(gen.new_while())
         skip="SKIP"+str(gen.new_label())
         gen.add_label(While_)
         if isinstance(izq,id):
             gen.add_la('t1',izq.id)
             gen.add_lw('t6','0(t1)')
         else:
             izq=izq.execute(Entorno,gen)
             if 't' in str(izq.value):
                 gen.add_move('t3',str(izq.value))
             else:
                 gen.add_li('t3',str(izq.value))
             gen.add_lw('t6','0(t3)')
             
         if isinstance(der,id):
             gen.add_la('t2',der.id)
             gen.add_lw('t5','0(t2)')
         else:
             der=der.execute(Entorno,gen)
             if 't' in str(der.value):
                 gen.add_move('t3', str(der.value))
             else:
                 gen.add_li('t3', str(der.value)) 
             gen.add_lw('t5', '0(t3)')
                
         
         
         
         
         
         
         
         if operador == '==':
                 gen.add_operation('bne', 't6', 't5', skip)
         elif operador == '!=':
                 gen.add_operation('beq', 't6', 't5', skip)
         elif operador == '>':
                 gen.add_operation('ble', 't6', 't5', skip)
         elif operador == '<':
                 gen.add_operation('bge', 't6', 't5', skip)
         elif operador == '>=':
                 gen.add_operation('blt', 't6', 't5', skip)
         elif operador == '<=':
                 gen.add_operation('bgt', 't6', 't5', skip)
         for i in self.instrucciones:
             i.execute(Entorno,gen)
             if isinstance(i, Break):
                 gen.add_jmp(skip)
         gen.add_jmp(While_)
         gen.add_label(skip)
 def execute(self,Entorno):
     new_entorno = entorno("while",Entorno)
     self.Entorno=new_entorno
     entornos.agregar_entorno(self.Entorno)
     instrucciones=""
     while self.condicion.execute(Entorno):
         i=0
         while i<len(self.instrucciones):
             ins = self.instrucciones[i].execute(self.Entorno)
             if ins is not None:
                 if isinstance(ins, Break):
                     return None
                 elif isinstance(ins, Continue):
                     i+=1
                 elif isinstance(ins, Return):
                     valor = ins.execute(self.Entorno)
                     if valor is not None:
                         return ins
                     else:
                         print("Error en la ejecucion del return")
             
                         return None
             i+=1

     
        

             