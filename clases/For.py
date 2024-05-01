from interfaz.instruccion import instruccion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from entorno.entorno import entorno
from clases.asignacion import asignacion
from estructuras.instrucciones import salida_instrucciones
from clases.Break import Break
from clases.Continue import Continue
from clases.Return import Return
from entorno.entornos import entornos
from estructuras.errores import errores
from clases.id import id
class For (instruccion):
 def __init__(self, variable, condicion, incremento, instrucciones, linea, columna):
        self.variable = variable
        self.condicion = condicion
        self.incremento = incremento
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna
        self.Entorno = None
        self.Entorno_ins=None

 def traducir(self, Entorno,gen):
        
        cond=self.condicion
        izq=cond.izq
        
        operador=cond.operador
        for_label="FOR"+str(gen.new_label())
        skip="SKIP"+str(gen.new_label())
        gen.add_label(for_label)
        val=self.variable.execute(Entorno,gen)
        der=cond.der.execute(Entorno,gen)
        
        
        
        
        tipo=Entorno.buscar_simbolo(izq.id).tipo_dato
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
               
               
        if 't' in str(der.value):
               gen.add_move('t3', str(der.value))
        else:
               gen.add_li('t3', str(der.value)) 
        gen.add_lw('t5', '0(t3)')
        temp = gen.new_temp()
       
        if(tipo=='NUMBER' and der.type=='NUMBER'):
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
        
        gen.add_li('t3','1')
        gen.add_operation('add', 't6', 't6', 't3')
        gen.add_la('t4',self.variable.id)
        gen.add_sw('t6','0(t4)')
        
        
        
        
        
        
        gen.add_jmp(for_label)
        gen.add_label(skip)
 def execute(self, Entorno):
     print("entro a for")
     nuevo_entorno = entorno("for",Entorno)
     self.Entorno = nuevo_entorno
     entornos.agregar_entorno(self.Entorno)
     self.variable.execute(self.Entorno)
     instrucciones = ""
     entorno_ins=entorno("for_ins",self.Entorno)
     entornos.agregar_entorno(entorno_ins)
     while self.condicion.execute(self.Entorno):
         i=0
         while i<len(self.instrucciones):
             inst=self.instrucciones[i]
             ins=inst.execute(entorno_ins)
             if isinstance(ins,Break):
                 return None
             elif isinstance(ins,Continue):
                    i+=1
             elif isinstance(ins,Return):
                     valor=ins.execute(entorno_ins)
                     if valor!=None:
                         return ins
                     else:
                         errores.agregar_error("Error en la ejecucion del return","Return "+self.Entorno.nombre,self.linea,self.columna,"Semantico")
                         return None 
             i+=1
         entorno_ins.vaciar_simbolos()
         self.Entorno.incrementar_valor_simbolo(self.incremento,1)