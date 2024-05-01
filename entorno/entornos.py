class entornos:
 ents=[]
 def agregar_entorno(entorno):
     entornos.ents.append(entorno)
 
 def obtener_tablas_simbolo():
     for ent in entornos.ents:
         print(ent.nombre)
         tabla=ent.obtener_tabla_simbolos()
         for key in tabla:
             print(key)
             print(tabla[key].tipo)
             print(tabla[key].valor)
             print(tabla[key].fila)
             print(tabla[key].columna)
             print(" ")
             
             
 def generar_html_simbolos():
     cadena=""
     for ent in entornos.ents:
         tabla=ent.obtener_tabla_simbolos()
         for key in tabla:
             cadena+="<tr>"
             cadena+="<td>"+ent.nombre+"</td>"
             cadena+="<td>"+key+"</td>"
             cadena+="<td>"+tabla[key].tipo+"</td>"
             cadena+="<td>"+str(tabla[key].valor)+"</td>"
             cadena+="<td>"+str(tabla[key].fila)+"</td>"
             cadena+="<td>"+str(tabla[key].columna)+"</td>"
             cadena+="</tr>"
     print("EJECUCION DE GENERAR HTML SIMBOLOS")
     return cadena
 def vaciar_entornos():
     entornos.ents=[]