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
class Switch(instruccion):
 def __init__(self,expresion,casos,default,linea,columna):
     self.expresion=expresion
     self.casos=casos
     self.linea=linea
     self.columna=columna
     self.default=default
     self.Entorno=None
 def traducir(self,Entorno,gen):
     exp=self.expresion.execute(Entorno,gen)
     if 't' in str(exp.value):
         gen.add_move('t3',str(exp.value))
     else:
         gen.add_li('t3',str(exp.value))
     gen.add_lw('t4','0(t3)')
     
     fin_switch="FIN_SWITCH"+str(gen.new_label())
     
     
     for c in self.casos:
         e=c.expresion.execute(Entorno,gen)
         skip="SKIP"+str(gen.new_label())
         if 't' in str(e.value):
             gen.add_move('t3',str(e.value))
         else:
             gen.add_li('t3',str(e.value))
         gen.add_lw('t2','0(t3)')
         gen.add_operation('bne','t4','t2',skip)
         c.execute(Entorno,gen)
         gen.add_jmp(fin_switch)
         gen.add_label(skip)
         
     if self.default!=None:
         self.default.execute(Entorno,gen)
     gen.add_label(fin_switch)
      
 def execute(self,Entorno):
     nuevo_entorno = entorno("switch",Entorno)   
     self.Entorno=nuevo_entorno
     entornos.agregar_entorno(self.Entorno)
     valor = self.expresion.execute(Entorno)
     for caso in self.casos:
         if caso.expresion.execute(entorno)==valor:
             resultado=""
             for instruccion in caso.instrucciones:
                 ins=instruccion.execute(self.Entorno)
                 if isinstance(ins,Break):
                     valor=ins.execute(self.Entorno)
                     if valor!=None:
                            return ins
                     else:
                            errores.agregar_error("Error break no se encuentra en un ciclo","Switch",self.linea,self.columna,"Semantico")
                            return None
                 elif isinstance(ins,Continue):
                     valor=ins.execute(self.Entorno)
                     if valor!=None:
                            return ins
                     else:
                            errores.agregar_error("Error continue no se encuentra en un ciclo","Switch",self.linea,self.columna,"Semantico")
                            return None
                 elif isinstance(ins,Return):
                     valor=ins.execute(self.Entorno)
                     if valor!=None:
                         return ins
                     else:
                         errores.agregar_error("Error en la ejecucion del return","Switch",self.linea,self.columna,"Semantico")
                         return None
             return None
               
             
     if self.default != None:
         
         
         
         self.default.execute(self.Entorno)
         return None
        
         
         
        