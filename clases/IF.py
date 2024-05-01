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
class IF(instruccion):
 def __init__(self,condicion,instrucciones,ELSE,else_if,linea,columna):
     self.condicion = condicion
     self.instrucciones = instrucciones
     self.ELSE=ELSE
     self.else_if=else_if
     self.linea = linea
     self.columna = columna
     self.Entorno=None
 def traducir(self,Entorno,gen):
     izq=self.condicion.izq.execute(Entorno,gen)
     der=self.condicion.der.execute(Entorno,gen)
     operador=self.condicion.operador
     
     gen.comment("Inicio del IF")
     
     if 't' in str(izq.value):
         gen.add_move('t3',str(izq.value))
     else:
         gen.add_li('t3',str(izq.value))
     gen.add_lw('t1','0(t3)')
     if 't' in str(der.value):
         gen.add_move('t3', str(der.value))
     else:
         gen.add_li('t3', str(der.value)) 
     gen.add_lw('t2', '0(t3)')
     temp = gen.new_temp()
     
     
     skip="SKIP"+str(gen.new_label())
     skip2="SKIP"+str(gen.new_label())
     
     if (self.else_if==None and self.ELSE==None):
         if izq.type == 'NUMBER' and der.type == 'NUMBER':
             if operador == '==':
                 gen.add_operation('bne', 't1', 't2', skip)
             elif operador == '!=':
                 gen.add_operation('beq', 't1', 't2', skip)
             elif operador == '>':
                 gen.add_operation('ble', 't1', 't2', skip)
             elif operador == '<':
                 gen.add_operation('bge', 't1', 't2', skip)
             elif operador == '>=':
                 gen.add_operation('blt', 't1', 't2', skip)
             elif operador == '<=':
                 gen.add_operation('bgt', 't1', 't2', skip)
         gen.add_br()
        
         for ins in self.instrucciones:
             ins.execute(Entorno,gen)
         
         gen.add_label(skip)
     elif (self.else_if==None and self.ELSE!=None):
         gen.comment("Inicio IF ELSE")
         if izq.type == 'NUMBER' and der.type == 'NUMBER':
             if operador == '==':
                 gen.add_operation('bne', 't1', 't2', skip)
             elif operador == '!=':
                 gen.add_operation('beq', 't1', 't2', skip)
             elif operador == '>':
                 gen.add_operation('ble', 't1', 't2', skip)
             elif operador == '<':
                 gen.add_operation('bge', 't1', 't2', skip)
             elif operador == '>=':
                 gen.add_operation('blt', 't1', 't2', skip)
             elif operador == '<=':
                 gen.add_operation('bgt', 't1', 't2', skip)
         gen.add_br()
         for ins in self.instrucciones:
             if isinstance(ins, Break) :
                 return ins
             else:
                 ins.execute(Entorno,gen)
             
             
         gen.add_jmp(skip2)
         gen.add_label(skip)
         for ins in self.ELSE:
             ins.execute(Entorno,gen)
         gen.add_label(skip2)
     elif (self.else_if!=None and self.ELSE==None):
         gen.comment("Inicio IF ELSE IF")
         if izq.type == 'NUMBER' and der.type == 'NUMBER':
             if operador == '==':
                 gen.add_operation('bne', 't1', 't2', skip)
             elif operador == '!=':
                 gen.add_operation('beq', 't1', 't2', skip)
             elif operador == '>':
                 gen.add_operation('ble', 't1', 't2', skip)
             elif operador == '<':
                 gen.add_operation('bge', 't1', 't2', skip)
             elif operador == '>=':
                 gen.add_operation('blt', 't1', 't2', skip)
             elif operador == '<=':
                 gen.add_operation('bgt', 't1', 't2', skip)  
         gen.add_br()
         for ins in self.instrucciones:
             ins.execute(Entorno,gen)
         gen.add_jmp(skip2)
         gen.add_label(skip)
         gen.comment("ELSE IF")
         for ins in self.else_if:
             ins.execute(Entorno,gen)
             gen.add_label(skip2)
     elif (self.else_if!=None and self.ELSE!=None):
         
         gen.comment("Inicio IF ELSE IF ELSE")
         if izq.type == 'NUMBER' and der.type == 'NUMBER':
                if operador == '==':
                    gen.add_operation('bne', 't1', 't2', skip)
                elif operador == '!=':
                    gen.add_operation('beq', 't1', 't2', skip)
                elif operador == '>':
                    gen.add_operation('ble', 't1', 't2', skip)
                elif operador == '<':
                    gen.add_operation('bge', 't1', 't2', skip)
                elif operador == '>=':
                    gen.add_operation('blt', 't1', 't2', skip)
                elif operador == '<=':
                    gen.add_operation('bgt', 't1', 't2', skip)
         gen.add_br()
         for ins in self.instrucciones:
             ins.execute(Entorno,gen)
         gen.add_jmp(skip2)
         gen.add_label(skip)
         gen.comment("ELSE IF")
         for ins in self.else_if:
             ins.execute(Entorno,gen) 
             
         for ins in self.ELSE:
             ins.execute(Entorno,gen)
         gen.add_label(skip2)
 def execute(self,Entorno):
     nuevo_entorno = entorno("IF",Entorno)
     self.Entorno=nuevo_entorno
     entornos.agregar_entorno(self.Entorno)
     if self.condicion.execute(Entorno):
         for inst in self.instrucciones:
             instruccion=inst.execute(self.Entorno)
             if isinstance(instruccion,Break):
                 valor=instruccion.execute(self.Entorno)
                 if valor!=None:
                     return instruccion
                 else:
                     errores.agregar_error("Error en la ejecucion del break","Break",self.linea,self.columna,"Semantico")
                     return None
             elif isinstance(instruccion,Continue):
                 valor=instruccion.execute(self.Entorno)
                 if valor!=None:
                     return instruccion
                 else:
                     errores.agregar_error("Error en la ejecucion del continue","Continue",self.linea,self.columna,"Semantico")
                     return None
             elif isinstance(instruccion,Return):
                     valor=instruccion.execute(self.Entorno)
                     if valor!=None:
                         return instruccion
                     else:
                         errores.agregar_error("Error en la ejecucion del return","Return",self.linea,self.columna,"Semantico")
                         return None  
            
                
         
     else:
         if self.else_if != None:
             resultado=""
             for inst in self.else_if:
                 
                 else_if_condicion=inst.condicion.execute(self.Entorno)
                 if (else_if_condicion):
                        
                        for instruccion in inst.instrucciones:
                         ins_else_if=instruccion.execute(self.Entorno)
                         if isinstance(ins_else_if,Break):
                             valor=ins_else_if.execute(self.Entorno)
                             if valor!=None:
                                 return ins_else_if
                             else:
                                 errores.agregar_error("Error en la ejecucion del break","Break",self.linea,self.columna,"Semantico")
                                 return None
                         elif isinstance(ins_else_if,Continue):
                                valor=ins_else_if.execute(self.Entorno)
                                if valor!=None:
                                    return ins_else_if
                                else:
                                    errores.agregar_error("Error en la ejecucion del continue","Continue",self.linea,self.columna,"Semantico")
                                    return None
                         elif isinstance(ins_else_if,Return):
                                valor=ins_else_if.execute(self.Entorno)
                                if valor!=None:
                                    return ins_else_if
                                else:
                                    errores.agregar_error("Error en la ejecucion del return","Return",self.linea,self.columna,"Semantico")
                                    return None
                        return None
                 
         if self.ELSE != None:
             
             for inst in self.ELSE:
                 instruccion=inst.execute(self.Entorno)
                 if isinstance(instruccion,Break):
                     valor=instruccion.execute(self.Entorno) 
                     if valor!=None:
                            return instruccion
                     else:
                            errores.agregar_error("Error en la ejecucion del break","Break",self.linea,self.columna,"Semantico")
                            return None
                 elif isinstance(instruccion,Continue):
                     valor=instruccion.execute(self.Entorno)
                     if valor!=None:
                            return instruccion
                     else:
                            errores.agregar_error("Error en la ejecucion del continue","Continue",self.linea,self.columna,"Semantico")
                            return None
                 elif isinstance(instruccion,Return):
                     valor=instruccion.execute(self.Entorno)
                     if valor!=None:
                         return instruccion
                     else:
                         errores.agregar_error("Error en la ejecucion del return","Return",self.linea,self.columna,"Semantico")
                         return None  
             return None
         
             
     return None
       
     
     