from interfaz.expresion import expresion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from clases.primitivo import primitivo
from estructuras.errores import errores
from entorno.value import Value
class operacion(expresion):
 def __init__(self, izq, der, operador, linea, columna):
     self.izq = izq
     self.der = der
     self.operador = operador
     self.linea = linea
     self.columna = columna

 def traducir(self, entorno,gen):
     
     if (self.izq!=None):
         izq=self.izq.execute(entorno,gen)
         der=self.der.execute(entorno,gen)
         gen.add_br()
         gen.comment('Operacion')
         if 't' in str(izq.value):
             gen.add_move('t3',str(izq.value))
         elif 'f' in str(izq.value):
             gen.add_la('t0',str(izq.value))
             gen.add_flw('f1','0(t0)')
         else:
             gen.add_li('t3',str(izq.value))
         if 'f' not in str(der.value):
             gen.add_lw('t1','0(t3)')
         if 't' in str(der.value):
             gen.add_move('t3', str(der.value))
         elif 'f' in str(der.value):
             gen.add_la('t0', str(der.value))
             gen.add_flw('f2', '0(t0)')
         else:
             gen.add_li('t3', str(der.value)) 
         if 'f' not in str(der.value):
             gen.add_lw('t2', '0(t3)')
         temp = gen.new_temp()
         if self.operador == '+':
             if izq.type == 'NUMBER' and der.type == 'NUMBER':
                 gen.add_operation('add', 't0', 't1', 't2')
                 gen.add_li('t3', str(temp))
                 gen.add_sw('t0', '0(t3)')
                 return Value(str(temp), True, 'NUMBER', [], [], [])
             if izq.type=='FLOAT' and der.type=='FLOAT':
                 gen.comment('Suma de dos flotantes')
                 gen.add_operation('fadd.s','f0','f1','f2')
                 gen.variable_data('res_floa_'+str(temp), 'float', '0.0')
                 gen.add_la('t0','res_floa_'+str(temp))
                 gen.add_fsw('f0','0(t0)')
                 return Value('res_floa_'+str(temp),True,'FLOAT',[],[],[])
         elif self.operador == '-':
             if izq.type == 'NUMBER' and der.type == 'NUMBER':
                 gen.add_operation('sub', 't0', 't1', 't2')
                 gen.add_li('t3', str(temp))
                 gen.add_sw('t0', '0(t3)')
                 return Value(str(temp), True, 'NUMBER', [], [], [])
         elif self.operador == '*':
                if izq.type == 'NUMBER' and der.type == 'NUMBER':
                    gen.add_operation('mul', 't0', 't1', 't2')
                    gen.add_li('t3', str(temp))
                    gen.add_sw('t0', '0(t3)')
                    return Value(str(temp), True, 'NUMBER', [], [], [])
         elif self.operador == '/':
             if izq.type == 'NUMBER' and der.type == 'NUMBER':
                 gen.add_operation('div', 't0', 't1', 't2')
                 gen.add_li('t3', str(temp))
                 gen.add_sw('t0', '0(t3)')
                 return Value(str(temp), True, 'NUMBER', [], [], [])
         elif self.operador == '%':
             if izq.type == 'NUMBER' and der.type == 'NUMBER':
                 gen.add_operation('rem', 't0', 't1', 't2')
                 gen.add_li('t3', str(temp))
                 gen.add_sw('t0', '0(t3)')
                 return Value(str(temp), True, 'NUMBER', [], [], [])
         elif self.operador =="==":
             if izq.type == 'NUMBER' and der.type == 'NUMBER':
                 diff="Diferente"+str(gen.new_label())
                 fin_igual_igual="FinIgualIgual"+str(gen.new_label())
                 gen.add_operation('bne', 't0', 't1',diff)
                 gen.add_li('t0', '1')
                 gen.add_li('t3', str(temp))
                 gen.add_sw('t0', '0(t3)')
                 gen.add_jmp(fin_igual_igual)
                 gen.add_label(diff)
                 gen.add_li('t3', str(temp))
                 gen.add_sw('t0', '0(t3)')
                 gen.add_label(fin_igual_igual)
                 return Value(str(temp), True, 'BOOLEAN', [], [], [])
         elif self.operador =="<":
             if izq.type == 'NUMBER' and der.type == 'NUMBER':
                    gen.add_operation('slt', 't0', 't1', 't2')
                    gen.add_li('t3', str(temp))
                    gen.add_sw('t0', '0(t3)')
                    return Value(str(temp), True, 'BOOLEAN', [], [], [])
         elif self.operador ==">":
             if izq.type == 'NUMBER' and der.type == 'NUMBER':
                        gen.add_operation('sgt', 't0', 't1', 't2')
                        gen.add_li('t3', str(temp))
                        gen.add_sw('t0', '0(t3)')
                        return Value(str(temp), True, 'BOOLEAN', [], [], [])
         elif self.operador =="<=":
             if izq.type == 'NUMBER' and der.type == 'NUMBER':
                     mayor="Mayor"+str(gen.new_label())
                     fin_menor_igual="FinMenorIgual"+str(gen.new_label())
                     gen.add_operation('bgt', 't1', 't2',mayor)
                     gen.add_li('t0', '1')
                     gen.add_li('t3', str(temp))
                     gen.add_sw('t0', '0(t3)')
                     gen.add_jmp(fin_menor_igual)
                     gen.add_label(mayor)
                     gen.add_li('t0', '0')
                     gen.add_li('t3', str(temp))
                     gen.add_sw('t0', '0(t3)')
                     gen.add_label(fin_menor_igual)
                     return Value(str(temp), True, 'BOOLEAN', [], [], [])
         elif self.operador ==">=":
                if izq.type == 'NUMBER' and der.type == 'NUMBER':
                     menor="Menpr"+str(gen.new_label())
                     fin_mayor_igual="FinMayorIgual"+str(gen.new_label())
                     gen.add_operation('blt', 't1', 't2',menor)
                     gen.add_li('t0', '1')
                     gen.add_li('t3', str(temp))
                     gen.add_sw('t0', '0(t3)')
                     gen.add_jmp(fin_mayor_igual)
                     gen.add_label(menor)
                     gen.add_li('t0', '0')
                     gen.add_li('t3', str(temp))
                     gen.add_sw('t0', '0(t3)')
                     gen.add_label(fin_mayor_igual)
                     return Value(str(temp), True, 'BOOLEAN', [], [], [])
         elif self.operador =="!=":
             if izq.type == 'NUMBER' and der.type == 'NUMBER':
                 igual="Igual"+str(gen.new_label())
                 fin_diferente="FinDiferente"+str(gen.new_label())
                 gen.add_operation('beq', 't1', 't2',igual)
                 gen.add_li('t0', '1')
                 gen.add_li('t3', str(temp))
                 gen.add_sw('t0', '0(t3)')
                 gen.add_jmp(fin_diferente)
                 gen.add_label(igual)
                 gen.add_li('t0', '0')
                 gen.add_li('t3', str(temp))
                 gen.add_sw('t0', '0(t3)')
                 gen.add_label(fin_diferente)
                 return Value(str(temp), True, 'BOOLEAN', [], [], [])
         elif self.operador =="and":
             if izq.type == 'BOOLEAN' and der.type == 'BOOLEAN':
                 gen.add_operation('and', 't0', 't1', 't2')
                 gen.add_li('t3', str(temp))
                 gen.add_sw('t0', '0(t3)')
                 return Value(str(temp), True, 'BOOLEAN', [], [], [])
         elif self.operador =="or":
                if izq.type == 'BOOLEAN' and der.type == 'BOOLEAN':
                 gen.add_operation('or', 't0', 't1', 't2')
                 gen.add_li('t3', str(temp))
                 gen.add_sw('t0', '0(t3)')
                 return Value(str(temp), True, 'BOOLEAN', [], [], [])
         return None
     elif (self.izq==None):
         der=self.der.execute(entorno,gen)
         if 't' in str(der.value):
               gen.add_move('t3',str(der.value))
         else:
               gen.add_li('t3',str(der.value))
         gen.add_lw('t0','0(t3)')
         temp = gen.new_temp()
         if self.operador == '-':
             if der.type == 'NUMBER':
                 gen.add_li('t1', '0')
                 gen.add_operation('sub', 't0', 't1', 't0')
                 gen.add_li('t3', str(temp))
                 gen.add_sw('t0', '0(t3)')
                 return Value(str(temp), True, 'NUMBER', [], [], [])
         elif self.operador == '!':
              if der.type == 'BOOLEAN':
                
                 
                 gen.add_operation('xori', 't2', 't0', '1')
                 gen.add_li('t3', str(temp))
                 gen.add_sw('t2', '0(t3)')
                 return Value(str(temp), True, 'BOOLEAN', [], [], [])
             
         
         
 def execute(self, entorno):
     
     if self.izq!=None:
         if self.operador == "+":
             izquierdo = self.izq.execute(entorno)
             derecho = self.der.execute(entorno)
             
             if  isinstance(izquierdo, str) or isinstance(derecho, str):
                 
                 return str(izquierdo) + str(derecho)
             elif isinstance(izquierdo, int) and isinstance(derecho, int):
                   
                 return izquierdo + derecho
             elif isinstance(izquierdo, float) and isinstance(derecho, float):
                 return izquierdo + derecho
             elif isinstance(izquierdo, int) and isinstance(derecho, float):
                 return izquierdo + derecho
             elif isinstance(izquierdo, float) and isinstance(derecho, int):
                 return izquierdo + derecho
             else:
                 errores.agregar_error("Error de tipos en la suma","Operacion suma "+entorno.nombre,self.linea,self.columna,"Semantico")
         elif self.operador=="-":
             izquierdo = self.izq.execute(entorno)
             derecho = self.der.execute(entorno)
             if isinstance(izquierdo, int) and isinstance(derecho, int):
                 return izquierdo - derecho
             elif isinstance(izquierdo, float) and isinstance(derecho, float):
                 return izquierdo - derecho
             elif isinstance(izquierdo, int) and isinstance(derecho, float):
                 return izquierdo - derecho
             elif isinstance(izquierdo, float) and isinstance(derecho, int):
                 return izquierdo - derecho
            
             
             else:
                    errores.agregar_error("Error de tipos en la resta","Operacion resta "+entorno.nombre,self.linea,self.columna,"Semantico")
         elif self.operador=="*":
             izquierdo = self.izq.execute(entorno)
             derecho = self.der.execute(entorno)
             if isinstance(izquierdo, int) and isinstance(derecho, int):
                 return izquierdo * derecho
             elif isinstance(izquierdo, float) and isinstance(derecho, float):
                 return izquierdo * derecho
             elif isinstance(izquierdo, int) and isinstance(derecho, float):
                 return izquierdo * derecho
             elif isinstance(izquierdo, float) and isinstance(derecho, int):
                 return izquierdo * derecho
             
                 
             else:
                 errores.agregar_error("Error de tipos en la multiplicacion","Operacion multiplicacion "+entorno.nombre,self.linea,self.columna,"Semantico")
         elif self.operador=="/":
             izquierdo = self.izq.execute(entorno)
             derecho = self.der.execute(entorno)
             if isinstance(izquierdo, int) and isinstance(derecho, int) and derecho!=0:
                 return izquierdo / derecho
             elif isinstance(izquierdo, float) and isinstance(derecho, float) and derecho!=0.0:
                 return izquierdo / derecho
             elif isinstance(izquierdo, int) and isinstance(derecho, float) and derecho!=0.0:
                 return izquierdo / derecho
             elif isinstance(izquierdo, float) and isinstance(derecho, int) and derecho!=0:
                 return izquierdo / derecho
             elif derecho==0 or derecho==0.0:
                 errores.agregar_error("Error division entre 0","Operacion division "+entorno.nombre,self.linea,self.columna,"Semantico")
         elif self.operador=="%":
             izquierdo = self.izq.execute(entorno)
             derecho = self.der.execute(entorno)
             if isinstance(izquierdo, int) and isinstance(derecho, int):
                 return izquierdo % derecho
                
             else:
                 errores.agregar_error("Error de tipos en el modulo","Operacion modulo "+entorno.nombre,self.linea,self.columna,"Semantico")
         elif self.operador=="&&":
             izquierdo = self.izq.execute(entorno)
             derecho = self.der.execute(entorno)
             if isinstance(izquierdo, bool) and isinstance(derecho, bool):
                 return izquierdo and derecho
             
             else:
                 errores.agregar_error("Error de tipos en el and","Operacion and "+entorno.nombre,self.linea,self.columna,"Semantico")
         elif self.operador=="||":
             izquierdo = self.izq.execute(entorno)
             derecho = self.der.execute(entorno)
             if isinstance(izquierdo, bool) and isinstance(derecho, bool):
                 return izquierdo or derecho
             else:
                 errores.agregar_error("Error de tipos en el or","Operacion or "+entorno.nombre,self.linea,self.columna,"Semantico")
                 
         elif self.operador=="==":
             izquierdo = self.izq.execute(entorno)
             derecho = self.der.execute(entorno)
             if isinstance(izquierdo, int) and isinstance(derecho, int):
                 return izquierdo == derecho
             elif isinstance(izquierdo, float) and isinstance(derecho, float):
                 return izquierdo == derecho
             elif isinstance(izquierdo, float) and isinstance(derecho, int):
                    return izquierdo == derecho
             elif isinstance(izquierdo, int) and isinstance(derecho, float):
                    return izquierdo == derecho
             elif isinstance(izquierdo, str) and isinstance(derecho, str):
                 return izquierdo == derecho
             elif isinstance(izquierdo, bool) and isinstance(derecho, bool):
                 return izquierdo == derecho
             elif isinstance(izquierdo,str) and isinstance(derecho,str) and len(izquierdo)==1 and len(derecho)==1:
                 return izquierdo == derecho
             else:
                 errores.agregar_error("Error de tipos en el igual","Operacion igual "+entorno.nombre,self.linea,self.columna,"Semantico")
         elif self.operador=="!=":
                izquierdo = self.izq.execute(entorno)
                derecho = self.der.execute(entorno)
                if isinstance(izquierdo, int) and isinstance(derecho, int):
                    return izquierdo != derecho
                elif isinstance(izquierdo, float) and isinstance(derecho, float):
                    return izquierdo != derecho
                elif isinstance(izquierdo, float) and isinstance(derecho, int):
                    return izquierdo != derecho
                elif isinstance(izquierdo, int) and isinstance(derecho, float):
                    return izquierdo != derecho
                elif isinstance(izquierdo, str) and isinstance(derecho, str):
                    return izquierdo != derecho
                elif isinstance(izquierdo, bool) and isinstance(derecho, bool):
                    return izquierdo != derecho
                elif isinstance(izquierdo,str) and isinstance(derecho,str) and len(izquierdo)==1 and len(derecho)==1:
                    return izquierdo != derecho
                else:
                    errores.agregar_error("Error de tipos en el diferente","Operacion diferente "+entorno.nombre,self.linea,self.columna,"Semantico")
         elif self.operador=="<":
                izquierdo = self.izq.execute(entorno)
                derecho = self.der.execute(entorno)
                if isinstance(izquierdo, int) and isinstance(derecho, int):
                    return izquierdo < derecho
                elif isinstance(izquierdo, float) and isinstance(derecho, float):
                    return izquierdo < derecho
                elif isinstance(izquierdo, float) and isinstance(derecho, int):
                    return izquierdo < derecho
                elif isinstance(izquierdo, int) and isinstance(derecho, float):
                    return izquierdo < derecho
                elif isinstance(izquierdo, str) and isinstance(derecho, str):
                    return izquierdo < derecho
                elif isinstance(izquierdo,str) and isinstance(derecho,str) and len(izquierdo)==1 and len(derecho)==1:
                    return izquierdo < derecho
                else:
                    errores.agregar_error("Error de tipos en el menor que","Operacion menor que "+entorno.nombre,self.linea,self.columna,"Semantico")
         elif self.operador==">":
                izquierdo = self.izq.execute(entorno)
                derecho = self.der.execute(entorno)
                if isinstance(izquierdo, int) and isinstance(derecho, int):
                    return izquierdo > derecho
                elif isinstance(izquierdo, float) and isinstance(derecho, float):
                    return izquierdo > derecho
                elif isinstance(izquierdo, float) and isinstance(derecho, int):
                    return izquierdo > derecho
                elif isinstance(izquierdo, int) and isinstance(derecho, float):
                    return izquierdo > derecho
                elif isinstance(izquierdo, str) and isinstance(derecho, str):
                    return izquierdo > derecho
                elif  isinstance(izquierdo,str) and isinstance(derecho,str) and len(izquierdo)==1 and len(derecho)==1:
                    return izquierdo > derecho
                else:
                    errores.agregar_error("Error de tipos en el mayor que","Operacion mayor que "+entorno.nombre,self.linea,self.columna,"Semantico")
         elif self.operador=="<=":
                izquierdo = self.izq.execute(entorno)
                derecho = self.der.execute(entorno)
                if isinstance(izquierdo, int) and isinstance(derecho, int):
                    return izquierdo <= derecho
                elif isinstance(izquierdo, float) and isinstance(derecho, float):
                    return izquierdo <= derecho
                elif isinstance(izquierdo, float) and isinstance(derecho, int):
                    return izquierdo <= derecho
                elif isinstance(izquierdo, int) and isinstance(derecho, float):
                    return izquierdo <= derecho
                elif isinstance(izquierdo, str) and isinstance(derecho, str):
                    return izquierdo <= derecho
                elif  isinstance(izquierdo,str) and isinstance(derecho,str) and len(izquierdo)==1 and len(derecho)==1:
                    return izquierdo <= derecho
                else:
                    errores.agregar_error("Error de tipos en el menor igual que","Operacion menor igual que "+entorno.nombre,self.linea,self.columna,"Semantico")
         elif self.operador==">=":
                izquierdo = self.izq.execute(entorno)
                derecho = self.der.execute(entorno)
                if isinstance(izquierdo, int) and isinstance(derecho, int):
                    return izquierdo >= derecho
                elif isinstance(izquierdo, float) and isinstance(derecho, float):
                    return izquierdo >= derecho
                elif isinstance(izquierdo, float) and isinstance(derecho, int):
                    return izquierdo >= derecho
                elif isinstance(izquierdo, int) and isinstance(derecho, float):
                    return izquierdo >= derecho
                elif isinstance(izquierdo, str) and isinstance(derecho, str):
                    return izquierdo >= derecho
                elif isinstance(izquierdo,str) and isinstance(derecho,str) and len(izquierdo)==1 and len(derecho)==1:
                    return izquierdo >= derecho
                else:
                    errores.agregar_error("Error de tipos en el mayor igual que","Operacion mayor igual que "+entorno.nombre,self.linea,self.columna,"Semantico")
     else:
         if self.operador=="-":
             der=self.der.execute(entorno)
             if isinstance(der,int):
                 
                 return -1*der
             elif isinstance(der,float):
                 return -1*der
             else:
                 errores.agregar_error("Error de tipos en el menos unario","Operacion menos unario "+entorno.nombre,self.linea,self.columna,"Semantico")
         elif self.operador=="!":
                der=self.der.execute(entorno)
                if isinstance(der,bool):
                    self.tipo = Tipo.BOOLEAN
                    return not der
                else:
                    errores.agregar_error("Error de tipos en el not","Operacion not "+entorno.nombre,self.linea,self.columna,"Semantico")
            
                  