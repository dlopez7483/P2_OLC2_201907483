from interfaz.instruccion import instruccion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from entorno.entorno import entorno
from estructuras.errores import errores
from interfaz.expresion import expresion
from entorno.value import Value
class traducir(instruccion):
    def __init__(self,expresion,linea,columna):
        self.expresion=expresion
        self.linea=linea
        self.columna=columna
    def traducir(self,entorno,gen):
     valor=self.expresion
     if (isinstance(valor,expresion)):
            valor=valor.execute(entorno,gen)
            gen.add_br()
            
            gen.comment('Convirtiendo a minusculas')
            loop="loop_lower"+gen.new_label()
            not_upper="not_upper"+gen.new_label()
            end_lower="end_lower"+gen.new_label()
            if valor.type=='STRING'  or valor.type=='CHAR' :
                    gen.add_la('t0',str(valor.value))
                    gen.add_label(loop)
                    gen.add_lb('t1','0(t0)')
                    gen.add_beqz('t1',end_lower)
                    gen.add_li('t2','65')
                    gen.add_operation('blt','t1','t2',not_upper)
                    gen.add_li('t2','32')
                    gen.add_operation('sub','t1','t1','t2')
                    gen.add_label(not_upper)
                    gen.add_sb('t1','0(t0)')
                    gen.add_operation('addi','t0','t0','1')
                    gen.add_jmp(loop)
                    gen.add_label(end_lower)
                    return valor
     
     
     elif (isinstance(valor,str)):
         valor=entorno.buscar_simbolo(valor)
         v=self.expresion
         if valor!=None: 
             if valor.tipo_dato=='STRING' or valor.tipo_dato=='CHAR':  
                    gen.add_br()
                    
                    gen.comment('Convirtiendo a minusculas')
                    loop="loop_lower"+gen.new_label()
                    not_upper="not_upper"+gen.new_label()
                    end_lower="end_lower"+gen.new_label()
                    gen.add_la('t0',v)
                    gen.add_label(loop)
                    gen.add_lb('t1','0(t0)')
                    gen.add_beqz('t1',end_lower)
                    gen.add_li('t2','65')
                    gen.add_operation('blt','t1','t2',not_upper)
                    gen.add_li('t2','32')
                    gen.add_operation('sub','t1','t1','t2')
                    gen.add_label(not_upper)
                    gen.add_sb('t1','0(t0)')
                    gen.add_operation('addi','t0','t0','1')
                    gen.add_jmp(loop)
                    gen.add_label(end_lower)
                    return Value(v,True,valor.tipo_dato,[],[],[])
    def execute(self,entorno):
        valor=None
        if isinstance(self.expresion,expresion) | isinstance(self.expresion,instruccion):
         valor=self.expresion.execute(entorno)
        elif isinstance(self.expresion,str):
         valor=entorno.buscar_simbolo(self.expresion).valor
        
        
        
        if (isinstance(valor,str)):
            return valor.lower()
        else:
            errores.agregar_error("El valor no es de tipo string","LowerCase "+entorno.nombre,self.linea,self.columna,"Semantico")
            return None
    
                                
     