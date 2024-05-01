from interfaz.instruccion import instruccion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from entorno.entorno import entorno
from estructuras.errores import errores
class instancia(instruccion):
    def __init__(self,tipo,nombre,atributos,linea,columna):
        self.nombre=nombre
        self.tipo=tipo
        self.atributos=atributos
        self.at={}
        self.linea=linea
        self.columna=columna
    def execute(self,Entorno):
     interfaz=Entorno.buscar_interface(self.tipo)
     validacion=True
     if interfaz!=None:
            for a in self.atributos:
                
                
                if a.nombre in interfaz:
                 valor=a.execute(Entorno)
                 if isinstance(valor,str) and interfaz[a.nombre]=='STRING':
                     self.at[a.nombre]=valor
                 elif isinstance(valor,int) and interfaz[a.nombre]=='NUMBER':
                     self.at[a.nombre]=valor
                 elif isinstance(valor,float) and interfaz[a.nombre]=='FLOAT':
                     self.at[a.nombre]=valor
                 elif isinstance(valor,bool) and interfaz[a.nombre]=='BOOLEAN':
                     self.at[a.nombre]=valor
                 elif isinstance(valor,str) and interfaz[a.nombre]=='CHAR':
                     self.at[a.nombre]=valor
                 elif isinstance(valor,int) and interfaz[a.nombre]=='FLOAT':
                     self.at[a.nombre]=float(valor)
                 elif isinstance(valor,dict):
                     self.at[a.nombre]=valor
                    
                     
                     
                 else:
                        validacion=False
                        errores.agregar_error("El valor "+a.nombre+" no es de tipo "+interfaz[a.nombre],"Instancia "+Entorno.nombre,self.linea,self.columna,"Semantico")
                        return None
                else:
                    validacion=False
                    errores.agregar_error("El atributo "+a.nombre+" no existe en la interfaz "+self.tipo,"Instancia "+Entorno.nombre,self.linea,self.columna,"Semantico")
                    return None
     ##self,nombre,tipo,tipo_dato, valor, fila, columna 
     if validacion:   
         Entorno.agregar_simbolo(self.nombre,'OBJETO',self.tipo,self.at,self.linea,self.columna)
         
     
        