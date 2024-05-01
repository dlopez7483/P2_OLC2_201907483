import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from estructuras.instrucciones import salida_instrucciones
from estructuras.errores import errores
from entorno.entornos import entornos
from gramatica import *
import os

nombre_archivo=""
def abrir_archivo():
 seleccion=combo_box.get()
 if seleccion=='abrir':
    
       text_area.delete("1.0",END)
       
       archivo = filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Archivos de texto", "*.olc"), ("Todos los archivos", "*.*")))
       if archivo != "":
             file = open(archivo, "r")
             contenido = file.read()
             global nombre_archivo
             nombre_archivo=os.path.basename(archivo)
             text_area.insert(INSERT, contenido)
             file.close()
 elif seleccion=='guardar':
       with open(nombre_archivo, "w") as archivo:
             archivo.write(text_area.get("1.0",END))
       archivo.close()
 elif seleccion=='crear':
            errores.vaciar_errores()
            entornos.vaciar_entornos()
            archivo = filedialog.asksaveasfile(title="Guardar", initialdir="C:", filetypes=(("Archivos de texto", "*.olc"), ("Todos los archivos", "*.*")))
            if archivo != None:
                  archivo.write(text_area.get("1.0",END))
                  archivo.close()
       
     
     
     
def ejecutar():
      
   errores.vaciar_errores()
   entornos.vaciar_entornos()
   text_consola.delete("1.0",END)
   texto=text_area.get("1.0",END)
   ingresar_texto(texto)
   text_consola.insert(INSERT,salida_instrucciones.instrucciones)


def generar_html_errores():
   html_errores="<html><head><title>Errores</title></head><body><table border='1'><tr><td>Descripcion</td><td>Ambito</td><td>Linea</td><td>Columna</td><td>Tipo</td></tr>" 
   html_errores+=errores.generar_html_errores()+"</table></body></html>"
   ruta_errores="errores.html"
   try:
         archivo=open(ruta_errores,"w")
         archivo.write(html_errores)
         archivo.close()
   except:
         print("Error al generar el archivo de errores")   

def generar_html_simbolos():
   html_simbolos="<html><head><title>Tabla de Simbolos</title></head><body><table border='1'><tr><td>Ambito</td><td>Nombre</td><td>Tipo</td><td>Valor</td><td>Fila</td><td>Columna</td></tr>"
   html_simbolos+=entornos.generar_html_simbolos()+"</table></body></html>"
   ruta_simbolos="simbolos.html"
   try:
         archivo=open(ruta_simbolos,"w")
         archivo.write(html_simbolos)
         archivo.close()
   except:
         print("Error al generar el archivo de simbolos")
     
ventana = tk.Tk()

ventana.title("OLC2")


boton_archivo = Button(ventana, text="Archivo",command=abrir_archivo)
boton_archivo.place(x=10, y=10)

boton_editar = Button(ventana, text="Editar")
boton_editar.place(x=70, y=10)
boton_ejecutar = Button(ventana, text="Ejecutar",command=ejecutar)
boton_ejecutar.place(x=200, y=10)


elementos=['crear','guardar','abrir']
combo_box=ttk.Combobox(ventana,values=elementos)
combo_box.place(x=340,y=10)


boton_tabla_simbolos = Button(ventana, text="Tabla de Simbolos",command=generar_html_simbolos)
boton_tabla_simbolos.place(x=10, y=380)

boton_errores = Button(ventana, text="Errores",command=generar_html_errores)
boton_errores.place(x=130, y=380)

text_area = Text(ventana, width=90, height=20)
text_area.place(x=10, y=50)

text_consola = Text(ventana, width=170, height=10)
text_consola.place(x=10, y=420)

ventana.geometry("800x600")

ventana.mainloop()