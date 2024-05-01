from interfaz.instruccion import instruccion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from clases.indice_arreglo import indice_arreglo
from estructuras.errores import errores
from clases.llave_objeto import llave_objeto
from clases.id import id
class asignacion (instruccion):
 def __init__(self,id,tipo_as,expresion,linea,columna):
     self.id=id
     self.tipo_as=tipo_as
     self.expresion=expresion
     self.incrementador=0
     self.linea=linea
     self.columna=columna
     

     
     
     
 def retornar_pocision_arreglo(self,entorno,simbolo,indice,tamanio_llamado,valor):
     print("aaaaa")
     
     print(tamanio_llamado)
     if (self.incrementador<tamanio_llamado-1 and isinstance(simbolo,list)):
         self.incrementador+=1
         nuevo_arreglo=simbolo[indice]
         self.retornar_pocision_arreglo(entorno,nuevo_arreglo,self.id.expresion[self.incrementador][0].execute(entorno),tamanio_llamado,valor)
     elif (self.incrementador==tamanio_llamado-1):
         if ( indice>=0 and indice<len(simbolo)):
             simbolo[indice]=valor
        
     
     
     
     
 def execute(self,entorno):
     if (isinstance(self.id,str)):
         simbolo = entorno.buscar_simbolo(self.id)
         if simbolo != None:
             valor = self.expresion.execute(entorno)
             if valor != None:
                 if simbolo != None:
                     if simbolo.tipo!="const":
                         if self.tipo_as =="=":
                             if simbolo.tipo_dato == "NUMBER" and isinstance(valor,int):
                                 simbolo.valor = valor
                             elif simbolo.tipo_dato == "FLOAT" and isinstance(valor,float):
                                 simbolo.valor = valor
                             elif simbolo.tipo_dato == "FLOAT" and isinstance(valor,int):
                                 simbolo.valor = float(valor)
                             elif simbolo.tipo_dato == "STRING" and isinstance(valor,str):
                                 simbolo.valor = valor
                             elif simbolo.tipo_dato == "BOOLEAN" and isinstance(valor,bool):
                                 simbolo.valor = valor
                             elif simbolo.tipo_dato == "CHAR" and isinstance(valor,str) and len(valor) == 1:
                                 simbolo.valor = valor
                             elif simbolo.tipo_dato == "NUMBER" and isinstance(valor,list):
                                 arreglo = []
                                 for i in valor:
                                     val=i
                                     if isinstance(val,int):
                                         arreglo.append(val)
                                     else:
                                         errores.agregar_error("El tipo de dato no coincide con el valor de "+self.id,"Asignacion "+entorno.nombre,self.linea,self.columna,"Semantico")
                                 simbolo.valor = arreglo
                             elif simbolo.tipo_dato == "FLOAT" and isinstance(valor,list):
                                    arreglo = []
                                    for i in valor:
                                        val=i
                                        if isinstance(val,float):
                                            arreglo.append(val)
                                        elif isinstance(val,int):
                                            arreglo.append(float(val))
                                        else:
                                           errores.agregar_error("El tipo de dato no coincide con el valor de "+self.id,"Asignacion "+entorno.nombre,self.linea,self.columna,"Semantico")
                                    simbolo.valor = arreglo
                             elif simbolo.tipo_dato == "STRING" and isinstance(valor,list):
                                    arreglo = []
                                    for i in valor:
                                        val=i
                                        if isinstance(val,str):
                                            arreglo.append(val)
                                        else:
                                           errores.agregar_error("El tipo de dato no coincide con el valor de "+self.id,"Asignacion "+entorno.nombre,self.linea,self.columna,"Semantico")
                                    simbolo.valor = arreglo
                             elif simbolo.tipo_dato == "BOOLEAN" and isinstance(valor,list):
                                 arreglo = []
                                 for i in valor:
                                        val=i
                                        if isinstance(val,bool):
                                            arreglo.append(val)
                                        else:
                                            errores.agregar_error("El tipo de dato no coincide con el valor de "+self.id,"Asignacion "+entorno.nombre,self.linea,self.columna,"Semantico")
                                 simbolo.valor = arreglo
                             elif simbolo.tipo_dato == "CHAR" and isinstance(valor,list):
                                    arreglo = []
                                    for i in valor:
                                            val=i
                                            if isinstance(val,str) and len(val) == 1:
                                                arreglo.append(val)
                                            else:
                                                errores.agregar_error("El tipo de dato no coincide con el valor de "+self.id,"Asignacion "+entorno.nombre,self.linea,self.columna,"Semantico")
                                    simbolo.valor = arreglo
                            
                             else:
                                 errores.agregar_error("El tipo de dato no coincide con el valor de "+self.id,"Asignacion "+entorno.nombre,self.linea,self.columna,"Semantico")
                         elif self.tipo_as == "+=":
                             if simbolo.tipo_dato == "NUMBER" and isinstance(valor,int):
                                 simbolo.valor += valor
                             elif simbolo.tipo_dato == "FLOAT" and isinstance(valor,float):
                                 simbolo.valor += valor
                             elif simbolo.tipo_dato == "FLOAT" and isinstance(valor,int):
                                 simbolo.valor += float(valor)
                             elif simbolo.tipo_dato == "STRING" and isinstance(valor,str):
                                 simbolo.valor += valor
                         elif self.tipo_as == "-=":
                             if simbolo.tipo_dato == "NUMBER" and isinstance(valor,int):
                                 simbolo.valor -= valor
                             elif simbolo.tipo_dato == "FLOAT" and isinstance(valor,float):
                                 simbolo.valor -= valor
                             elif simbolo.tipo_dato == "FLOAT" and isinstance(valor,int):
                                 simbolo.valor -= float(valor)
                             else:
                                 errores.agregar_error("El tipo de dato no coincide con el valor de "+self.id,"Asignacion "+entorno.nombre,self.linea,self.columna,"Semantico")   
                     else:
                         errores.agregar_error("No se puede modificar el valor de una constante","Asignacion "+entorno.nombre,self.linea,self.columna,"Semantico")
         else:
             errores.agregar_error("El valor "+self.id+" no existe","Asignacion "+entorno.nombre,self.linea,self.columna,"Semantico")
             return None
     elif (isinstance(self.id,indice_arreglo)):
         nombre=self.id.id
         print("indice arreglo")
         print(self.id.expresion)
         print(len(self.id.expresion))
        
         simbolo=entorno.buscar_simbolo(nombre)
         if (simbolo!=None):
             if (len(self.id.expresion)==1):
                     indice=self.id.expresion[0][0].execute(entorno)
                     print(indice)
                     if (isinstance(indice,int)):
                          if (indice>=0 and indice<len(simbolo.valor)):
                             valor=self.expresion.execute(entorno)
                             if (valor!=None):
                         
                                 if (simbolo.tipo!="const"):
                                     if self.tipo_as=="=":
                                         if simbolo.tipo_dato=="NUMBER" and isinstance(valor,int):
                                             simbolo.valor[indice]=valor
                                         elif simbolo.tipo_dato=="FLOAT" and isinstance(valor,float):
                                             simbolo.valor[indice]=valor
                                         elif simbolo.tipo_dato=="FLOAT" and isinstance(valor,int):
                                             simbolo.valor[indice]=float(valor)
                                         elif simbolo.tipo_dato=="STRING" and isinstance(valor,str):
                                             simbolo.valor[indice]=valor
                                         elif simbolo.tipo_dato=="BOOLEAN" and isinstance(valor,bool):
                                             simbolo.valor[indice]=valor
                                         elif simbolo.tipo_dato=="CHAR" and isinstance(valor,str) and len(valor)==1:
                                             simbolo.valor[indice]=valor
                                         else:
                                             errores.agregar_error("El tipo de dato no coincide con el valor","Asignacion "+entorno.nombre,self.linea,self.columna,"Semantico")
                                     elif self.tipo_as=="+=":
                                         if simbolo.tipo_dato=="NUMBER" and isinstance(valor,int):
                                             simbolo.valor[indice]+=valor
                                         elif simbolo.tipo_dato=="FLOAT" and isinstance(valor,float):
                                             simbolo.valor[indice]+=valor
                                         elif simbolo.tipo_dato=="FLOAT" and isinstance(valor,int):
                                             simbolo.valor[indice]+=float(valor)
                                         elif simbolo.tipo_dato=="STRING" and isinstance(valor,str):
                                             simbolo.valor[indice]+=valor
                                         else:
                                             errores.agregar_error("El tipo de dato no coincide con el valor","Asignacion "+entorno.nombre,self.linea,self.columna,"Semantico")
                                     elif self.tipo_as=="-=":
                                         if simbolo.tipo_dato=="NUMBER" and isinstance(valor,int):
                                             simbolo.valor[indice]-=valor
                                         elif simbolo.tipo_dato=="FLOAT" and isinstance(valor,float):
                                             simbolo.valor[indice]-=valor
                                         elif simbolo.tipo_dato=="FLOAT" and isinstance(valor,int):
                                             simbolo.valor[indice]-=float(valor)
                                         else:
                                             errores.agregar_error("El tipo de dato no coincide con el valor","Asignacion "+entorno.nombre,self.linea,self.columna,"Semantico")
                                 else:
          
                                     errores.agregar_error("No se puede modificar el valor de una constante","Asignacion "+entorno.nombre,self.linea,self.columna,"Semantico")
             elif len(self.id.expresion)>1:
                 valor=self.expresion.execute(entorno)
                 self.retornar_pocision_arreglo(entorno,simbolo.valor,self.id.expresion[self.incrementador][0].execute(entorno),len(self.id.expresion),valor)
                     
                                        
                                     
                            
                                     
                                     
     elif(isinstance(self.id,llave_objeto)):
         nombre=self.id.id
         atributo=self.id.atributo
         simbolo=entorno.buscar_simbolo(nombre)
         if (simbolo!=None):
             if len(atributo)==1:
                 if atributo[0] in simbolo.valor:
                      simbolo.valor[atributo[0]]=self.expresion.execute(entorno)
                 else:
                     errores.agregar_error("El atributo no existe en el objeto","Llave_Objeto "+entorno.nombre,self.linea,self.columna,"Semantico")
                     return None
             elif len(atributo)>1:
                 if atributo[0] in simbolo.valor:
                     obj=simbolo.valor[atributo[0]]
                     for a in atributo[1:]:
                         if a in obj:
                             obj=obj[a]
                         else:
                             errores.agregar_error("El atributo no existe en el objeto","Llave_Objeto "+Entorno.nombre,self.linea,self.columna,"Semantico")
                             return None
                     obj=self.expresion.execute(entorno)
                 else:
                     errores.agregar_error("El atributo no existe en el objeto","Llave_Objeto "+Entorno.nombre,self.linea,self.columna,"Semantico")
                     return None
 def traducir(self,entorno,gen):
     
     if(isinstance(self.id,str)):
         simb=entorno.buscar_simbolo(str(self.id))
         if simb.tipo!="CONST":
             
        
             op=self.expresion.traducir(entorno,gen)
             if 't' in str(op.value):
                  gen.add_move('t3',str(op.value))
             else:
                 gen.add_li('t3',str(op.value))
             gen.add_lw('t1','0(t3)')
     
             if (self.tipo_as=="="):
                 id_=entorno.buscar_simbolo(str(self.id))
                 if id_!=None:
                     if id_.tipo_dato==op.type:
                         gen.add_la('t0',str(self.id))
                         gen.add_sw('t1','0(t0)')
                 
             
             
         
             elif (self.tipo_as=="+="):
                 id_=entorno.buscar_simbolo(str(self.id))
                 if id_!=None:
                     if id_.tipo_dato==op.type:
                         gen.add_la('t0',str(self.id))
                         gen.add_lw('t2','0(t0)')
                         gen.add_operation('add','t2','t2','t1')
                         gen.add_la('t4',str(self.id))
                         gen.add_sw('t2','0(t4)')
         
             elif (self.tipo_as=="-="):
                 id_=entorno.buscar_simbolo(str(self.id))
                 if id_!=None:
                     if id_.tipo_dato==op.type:
                         gen.add_la('t0',str(self.id))
                         gen.add_lw('t2','0(t0)')
                         gen.add_operation('sub','t2','t2','t1')
                         gen.add_la('t4',str(self.id))
                         gen.add_sw('t2','0(t4)')
         
     elif (isinstance(self.id,indice_arreglo)):
         simb=entorno.buscar_simbolo(str(self.id.id))
         gen.add_br()
         gen.comment('Asignacion a un arreglo')
         if simb!=None and simb.tipo!="CONST":
             index=self.id.expresion[0][0].traducir(entorno,gen)
             if index.type!="NUMBER":
                 errores.append(nodo_error(self.linea,self.columna,'Semantico','El indice del arreglo debe ser de tipo NUMBER'))
                 return None
             if 't' in str(index.value):
                 gen.add_move('t3', str(index.value))
             else:
                 gen.add_li('t3', str(index.value))
             gen.add_lw('t1', '0(t3)')
             gen.add_move('t0', 't1')
             gen.add_slli('t0', 't0', '2')
             gen.add_la('t1',simb.value)
             gen.add_lw('t1', '0(t1)')
             gen.add_operation('add', 't2', 't1', 't0')
             op=self.expresion.traducir(entorno,gen)
             if (op.type==simb.tipo_dato):
                 if 't' in str(op.value):
                     gen.add_move('t3',str(op.value))
                 else:
                     gen.add_li('t3',str(op.value))
                     gen.add_lw('t1','0(t3)')
                     gen.add_sw('t1','0(t2)')
        