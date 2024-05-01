from estructuras.error import error

class errores:
 errs=[]
 def agregar_error(descripcion,ambito,linea,columna,tipo):
     errores.errs.append(error(descripcion,ambito,linea,columna,tipo))

 def get_errores():
     for error in errores.errs:
         print(error.descripcion+" "+error.ambito+" "+str(error.linea)+" "+str(error.columna)+" "+error.tipo)
 def generar_html_errores():
     cadena=""
     for error in errores.errs:
         cadena+="<tr>"
         cadena+="<td>"+error.descripcion+"</td>"
         cadena+="<td>"+error.ambito+"</td>"
         cadena+="<td>"+str(error.linea)+"</td>"
         cadena+="<td>"+str(error.columna)+"</td>"
         cadena+="<td>"+error.tipo+"</td>"
         cadena+="</tr>"
     return cadena
 
 def vaciar_errores():
     errores.errs=[]