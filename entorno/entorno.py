from entorno.simbolo import simbolo
from estructuras.errores import errores
class entorno:
 def __init__ (self,nombre,anterior):
     self.nombre = nombre
     self.anterior = anterior
     self.tabla_simbolos = {}
     self.tabla_funciones = {}
     self.tabla_interfaces = {}
     self.salidas_ins=""
     
 def agregar_simbolo(self,nombre,tipo,tipo_dato, valor, value,fila, columna):
     if self.buscar_simbolo(nombre) == None:
         self.tabla_simbolos[nombre] = simbolo(tipo,tipo_dato,valor,value,fila,columna)
     else:
         errores.agregar_error("El simbolo "+nombre+" ya existe","Entorno "+self.nombre,fila,columna,"Semantico")
         print("Error: El simbolo "+nombre+" ya existe en este entorno")
 
 def buscar_interface(self,nombre):
     actual = self
     while actual != None:
         if actual.tabla_interfaces.get(nombre) != None:
             return actual.tabla_interfaces.get(nombre)
         actual = actual.anterior
     return None
 
 def agregar_interface(self,nombre,interface):
        if self.buscar_interface(nombre) == None:
         self.tabla_interfaces[nombre] = interface
        else:
         errores.agregar_error("La interface "+nombre+" ya existe","Entorno "+self.nombre,0,0,"Semantico")
         print("Error: La interface "+nombre+" ya existe en este entorno")
 
 def vaciar_simbolos(self):
     self.tabla_simbolos = {}
     
 def buscar_simbolo(self,nombre):
     actual = self
     while actual != None:
         if actual.tabla_simbolos.get(nombre) != None:
             return actual.tabla_simbolos.get(nombre)
         actual = actual.anterior
     return None
      
 def incrementar_valor_simbolo(self,nombre,valor):
     simbolo = self.buscar_simbolo(nombre)
     if simbolo != None:
         simbolo.valor += valor
     else:
         print("Error: El simbolo "+nombre+" no existe")
     
 def encontrar_entorno(self,nombre):
     actual = self
     while actual != None:
         if actual.nombre == nombre:
             return True
         actual = actual.anterior
     return False
 
 
 def buscar_funcion(self,nombre):
        actual = self
        while actual != None:
            if actual.tabla_funciones.get(nombre) != None:
                return actual.tabla_funciones.get(nombre)
            actual = actual.anterior
        return None
    
    
 def agregar_funcion(self,nombre,funcion):
     if self.buscar_funcion(nombre) == None:
         self.tabla_funciones[nombre] = funcion
     else:
         errores.agregar_error("La funcion "+nombre+" ya existe","Entorno "+self.nombre,0,0,"Semantico")
         print("Error: La funcion "+nombre+" ya existe en este entorno")    
     
 def obtener_tabla_simbolos(self):
     return self.tabla_simbolos