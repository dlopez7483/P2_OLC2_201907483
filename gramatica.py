import ply.lex as Lex
import ply.yacc as yacc
from estructuras.instrucciones import salida_instrucciones
from entorno.simbolo import simbolo
from entorno.types import Tipo
from interfaz.instruccion import instruccion
from interfaz.expresion import expresion
from clases.operacion import operacion
from clases.primitivo import primitivo
from clases.console import console
from clases.switch import Switch
from clases.caso import caso
from clases.IF import IF
from clases.While import While
from clases.default import default
from clases.id import id
from entorno.entorno import entorno
from clases.declaracion import declaracion
from clases.asignacion import asignacion
from clases.parametro import parametro
from clases.For import For
from clases.funcion import funcion
from clases.llamado import llamado
from clases.Return import Return
from clases.arreglo import arreglo
from clases.indice_arreglo import indice_arreglo
from clases.Len import Len
from clases.Pop import Pop
from clases.indexof import indexof
from clases.Join import Join
from clases.Push import Push
from clases.interface import interface
from clases.instancia import instancia
from clases.atributo import atributo
from clases.parse_int import parse_int
from clases.parse_float import parse_float
from clases.Tostring import Tostring
from clases.LowerCase import LowerCase
from clases.UpperCase import UpperCase
from clases.object_values import object_values
from clases.atributo_declarado import atributo_declarado
from clases.typeOf import typeOf
from clases.llave_objeto import llave_objeto
from clases.object_keys import object_keys
from clases.ternario import ternario
from clases.for_each import For_each
from clases.Break import Break
from clases.Continue import Continue
from estructuras.errores import errores
from entorno.entornos import entornos
from entorno.generador import generador
# Listado de tokens
class codeParams:
 def __init__(self, line, column):
     self.line = line
     self.column = column

ins=[]
reservadas = {

    'console': 'CONSOLE',
    'log': 'LOG',
    'number': 'NUMBER',
    'string': 'STRING',
    'boolean': 'BOOLEAN',
     'char': 'CHAR',
     'float': 'FLOAT',
    'if': 'IF',
    'var': 'VAR',
    'const': 'CONST',
    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'for': 'FOR',
    'while': 'WHILE',
    'return': 'RETURN',
    'function': 'FUNCTION',
    'null': 'NULL',
    'else': 'ELSE',
    'toString': 'TO_STRING',
    'of': 'OF',
    'push': 'PUSH',
    'pop': 'POP',
    'length': 'LENGTH',
    'join': 'JOIN',
    'const': 'CONST',
    'indexOf': 'INDEX_OF',
    'parseInt': 'PARSE_INT',
    'parseFloat': 'PARSE_FLOAT',
    'toLowerCase': 'TO_LOWER_CASE',
    'toUpperCase': 'TO_UPPER_CASE',
    'typeof': 'TYPEOF',
    'interface': 'INTERFACE',
    'Object': 'OBJECT',
    'keys': 'KEYS',
    'values': 'VALUES'
    
    
}


tokens = [
    'PARIZQ',
    'PARDER',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'MODULO',
    'PUNTO',
    'PUNTOCOMA',
    'CADENA',
    'ENTERO',
    'DECIMAL',
    'ID',
    'BOLEANO',
    'CORCHETEIZQ',
    'CORCHETEDER',
    'DOSPUNTOS',
    'COMA',
    'MAYORQUE',
    'MENORQUE',
    'MAYORIGUAL',
    'MENORIGUAL',
    'IGUAL',
    'DISTINTO',
    'AND',
    'OR',
    'NOT',
    'IGUALIGUAL',
    'SUMA_IGUAL',
    'RESTA_IGUAL',
    'LLAVEIZQ',
    'LLAVEDER',
    'INTERROGACION',
    'CARACTER'
]+ list(reservadas.values())

t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_PUNTO    = r'\.'
t_MODULO   = r'%'
t_PUNTOCOMA = r';'
t_DOSPUNTOS = r':'
t_COMA      = r','
t_MAYORQUE  = r'>'
t_MENORQUE  = r'<'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_IGUAL     = r'='
t_DISTINTO  = r'!='
t_AND       = r'&&'
t_OR        = r'\|\|'
t_NOT       = r'!'
t_IGUALIGUAL = r'=='
t_SUMA_IGUAL = r'\+='
t_RESTA_IGUAL = r'-='
t_LLAVEIZQ = r'{'
t_LLAVEDER = r'}'
t_INTERROGACION = r'\?'
t_CORCHETEIZQ = r'\['
t_CORCHETEDER = r'\]'

def t_CARACTER(t):
    r'\'.\''
    t.type = reservadas.get(t.value,'CARACTER')
    try:
        print("se ha encontrado caracter "+t.value)
        valor_sin_comillas = t.value[1:-1]
        t.value = str(valor_sin_comillas)
    except ValueError:
        print("Error al convertir caracter %d", t.value)
        t.value = ''
    return t

def t_BOLEANO(t):
    r'true|false'
    t.type = reservadas.get(t.value,'BOLEANO')
    try:
     if t.value == 'true':
         t.value = True
     elif t.value == 'false':
         t.value = False
    except ValueError:
        print("Error al convertir booleano %d", t.value)
        t.value = ''
    return t

#Función de reconocimiento
def t_CADENA(t):
    r'\"([^\\\n\r\t]|(\\.))*?\"'
    t.type = reservadas.get(t.value,'CADENA')
    try:
        valor_sin_comillas = t.value[1:-1]
        t.value = str(valor_sin_comillas)
    except ValueError:
        print("Error al convertir string %d", t.value)
        t.value = ''
    return t


def t_DECIMAL(t):
 r'\d+\.\d+'
 try:
     print("se ha encontrado decimal "+t.value)
     t.value = float(t.value)

 except ValueError:
     print("El valor del decimal es incorrecto %d", t.value)
     t.value = 0
 return t

def t_ENTERO(t):
 r'\d+'
 t.type = reservadas.get(t.value,'ENTERO')
 try:
     
     t.value = int(t.value)
        
 except ValueError:
     print("El valor del entero es incorrecto %d", t.value)
     t.value = 0
 return t


def t_ID(t):
 r'[a-zA-Z_][a-zA-Z_0-9]*'
 t.type = reservadas.get(t.value,'ID')
 return t

t_ignore = " \t"

t_ignore_COMMENTLINE = r'\/\/.*'

def t_ignore_COMMENTBLOCK(t):
    r'\/\*[^*]*\*+(?:[^/*][^*]*\*+)*\/'
    t.lexer.lineno += t.value.count('\n')

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    ##descripcion,ambito,linea,columna,tipo
    print("Error Léxico '%s'" % t.value[0])
    errores.agregar_error("Error Léxico '%s'" % t.value[0],"global",t.lineno,t.lexpos,"Lexico")
    t.lexer.skip(1)

#SINTACTICO
precedence=(
    ('left','OR'),
    ('left','AND'),
    ('left','MENORQUE','MAYORQUE','MENORIGUAL','MAYORIGUAL','IGUALIGUAL','DISTINTO'),
    ('left','MAS','MENOS'),
    ('left','DIVIDIDO','MODULO','POR'),
    ('right','UMENOS'),
    ('right','NOT'),
    ('nonassoc','PARIZQ','PARDER')
)

#START
def p_start(t):
    '''start : instrucciones_globales'''
    t[0] = t[1]
    


def p_instrucciones_globales(t):
    '''instrucciones_globales : instrucciones_globales instruccion_global
                    | instruccion_global '''
    if 2 < len(t):
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]
    
def p_instruccion_global(t):
    '''instruccion_global : instruccion
                        | funcion'''
    t[0] = t[1]

def p_funcion(t):
    '''funcion : funcion_parametros_tipo
                | funcion_tipo
                | funcion_parametros
                | funcion_simple
                '''
    t[0] = t[1]
    
#id, parametros, instrucciones, tipo, linea, columna
def p_funcion_simple(t):
    '''funcion_simple : FUNCTION ID PARIZQ PARDER LLAVEIZQ instrucciones LLAVEDER'''
    params = get_params(t)
    t[0] = funcion(t[2],None,t[6],None,params.line,params.column)
 
#id, parametros, instrucciones, tipo, linea, columna   
def p_funcion_parametros(t):
    '''funcion_parametros : FUNCTION ID PARIZQ parametros PARDER LLAVEIZQ instrucciones LLAVEDER'''
    params=get_params(t)
    t[0] = funcion(t[2],t[4],t[7],None,params.line,params.column)
def p_funcion_tipo(t):
    '''funcion_tipo : FUNCTION ID PARIZQ PARDER DOSPUNTOS tipo LLAVEIZQ instrucciones LLAVEDER'''
    params = get_params(t)
  
    t[0] = funcion(t[2],None,t[8],t[6],params.line,params.column)
def p_funcion_parametros_tipo(t):
    '''funcion_parametros_tipo : FUNCTION ID PARIZQ parametros PARDER DOSPUNTOS tipo LLAVEIZQ instrucciones LLAVEDER'''	
    params=get_params(t)
    #id, parametros, instrucciones, tipo, linea, columna  
    t[0] = funcion(t[2],t[4],t[9],t[7],params.line,params.column)
    
def p_parametros(t):
    '''parametros : parametros COMA parametro
                    | parametro'''
    if 2 < len(t):
        t[1].append(t[3])
        t[0] = t[1]
    else:
        t[0] = [t[1]]
        
def p_parametro(t):
    '''parametro : ID DOSPUNTOS tipo
                 | ID DOSPUNTOS tipo CORCHETEIZQ CORCHETEDER  '''
    params=get_params(t)
    if len(t) == 4:
     t[0] = parametro(t[3],t[1],params.line,params.column)
    elif len(t) == 6:
     t[0] = parametro(t[3],t[1],params.line,params.column)
    
    

def p_instrucciones_lista(t):
    '''instrucciones : instrucciones instruccion 
                    | instruccion '''
    if 2 < len(t):
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]
def p_instruccion(t):
    '''instruccion : instruccion_console
                
                    | declaracion_variables PUNTOCOMA
                    | declaracion_constantes PUNTOCOMA
                    | asignacion PUNTOCOMA
                    | if
                    | switch
                    | while
                    | for
                    | declaracion_arreglo PUNTOCOMA
                    | push PUNTOCOMA
                    | llamado_funcion PUNTOCOMA
                    | interfaz 
                    | declaracion_interfaz PUNTOCOMA
                    | break PUNTOCOMA
                    | continue PUNTOCOMA
                    | return PUNTOCOMA
                    
    '''
    t[0] = t[1]
    
def p_return(t):
    '''return : RETURN expresion'''
    params = get_params(t)
    t[0] = Return(t[2],params.line,params.column)    
    
def p_continue(t):
    '''continue : CONTINUE'''
    params = get_params(t)
    t[0] = Continue(params.line,params.column)    
def p_break(t):
    '''break : BREAK '''
    params = get_params(t)
    t[0] = Break(params.line,params.column)
##tipo,nombre,atributos,linea,columna
def p_declaracion_interfaz(t):
    '''declaracion_interfaz : VAR ID DOSPUNTOS ID IGUAL LLAVEIZQ atributos_declarados LLAVEDER
                            | CONST ID DOSPUNTOS ID IGUAL LLAVEIZQ atributos_declarados LLAVEDER'''
    params=get_params(t)  
    t[0] = instancia(t[4],t[2],t[7],params.line,params.column)  
    
def p_atributos_declarados(t):
    '''atributos_declarados : atributos_declarados COMA atributo_declarado
                    | atributo_declarado'''
    if 2 < len(t):
        t[1].append(t[3])
        t[0] = t[1]
    else:
        t[0] = [t[1]] 
        
def p_atributo_declarado(t):
    '''atributo_declarado : ID DOSPUNTOS expresion'''
    params = get_params(t)
    t[0] = atributo_declarado(t[1],t[3],params.line,params.column)  
    
def p_interfaz(t):
    '''interfaz : INTERFACE ID LLAVEIZQ atributos LLAVEDER'''
    params=get_params(t)
    t[0] = interface(t[2],t[4],params.line,params.column)
    
def p_atributos(t):
    '''atributos : atributos atributo
                    | atributo'''
    if 2 < len(t):
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]
        
        
def p_atributo(t):
    '''atributo : ID DOSPUNTOS tipo PUNTOCOMA
                | ID DOSPUNTOS ID PUNTOCOMA    '''
   
    t[0] = atributo(t[1],t[3])
def p_push(t):
    '''push : ID PUNTO PUSH PARIZQ expresion PARDER'''
    params = get_params(t)
    t[0] = Push(t[1],t[5],params.line,params.column)
    
def p_declaracion_arreglo(t):
    '''
    declaracion_arreglo : VAR ID DOSPUNTOS tipo corchetes IGUAL  expresion
                        | CONST ID DOSPUNTOS tipo corchetes IGUAL expresion
    
    '''
    ##nombre,dimension,tipo,tipo_dato,expresiones,linea,columna
    print("se ha encontrado declaracion de arreglo")
    params=get_params(t)
    t[0]=arreglo(t[2],len(t[5]),t[1],t[4],t[7],params.line,params.column)


def p_corchetes(t):
    '''corchetes : corchetes CORCHETEIZQ CORCHETEDER
                | CORCHETEIZQ CORCHETEDER'''
    if 3 < len(t):
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]
        
        

def p_corchete_expresion(t):
    '''corchete_expresion : CORCHETEIZQ expresiones CORCHETEDER'''
    t[0] = t[2]
    

 
    
def p_expresiones(t):
    '''expresiones : expresiones COMA expresion
                    | expresion'''
    if 2 < len(t):
        t[1].append(t[3])
        t[0] = t[1]
    else:
        t[0] = [t[1]]
def p_for(t):
    '''for : for_simple
           | for_each
    '''
    t[0] = t[1]


##variable,arreglo,instrucciones,linea,columna
def p_for_each(t):
    '''for_each : FOR PARIZQ VAR ID OF ID PARDER LLAVEIZQ instrucciones LLAVEDER'''
    params = get_params(t)
    t[0] = For_each(t[4],t[6],t[9],params.line,params.column)
    
##variable, condicion, incremento, instrucciones, linea, columna
def p_for_simple(t):
    '''for_simple : FOR PARIZQ declaracion_variables PUNTOCOMA expresion PUNTOCOMA ID MAS MAS PARDER LLAVEIZQ instrucciones LLAVEDER'''
    params = get_params(t)
    t[0] = For(t[3],t[5],t[7],t[12],params.line,params.column)
def p_while(t):
    '''while : WHILE PARIZQ expresion PARDER LLAVEIZQ instrucciones LLAVEDER
    '''
    params = get_params(t)
    t[0] = While(t[3],t[6],params.line,params.column)



def p_switch(t):
    '''switch : switch_normal
              | switch_default'''
    t[0] = t[1]
def p_switch_normal(t):
    '''switch_normal : SWITCH PARIZQ expresion PARDER LLAVEIZQ cases LLAVEDER'''
    params = get_params(t)
    t[0] = Switch(t[3],t[6],None,params.line,params.column)       
def p_switch_default(t):
    '''switch_default : SWITCH PARIZQ expresion PARDER LLAVEIZQ cases default  LLAVEDER'''
    params = get_params(t)
    t[0] = Switch(t[3],t[6],t[7],params.line,params.column)
    
def p_default(t):
    '''default : DEFAULT DOSPUNTOS instrucciones '''
    params = get_params(t)
    t[0] = default(t[3],params.line,params.column)
def p_cases(t):
    '''cases : cases case
            | case'''
    if 2 < len(t):
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]        
    
def p_case(t):
    '''case : CASE expresion DOSPUNTOS instrucciones BREAK PUNTOCOMA
    '''
    params = get_params(t)
    t[0] = caso(t[2],t[4],params.line,params.column)
def p_if(t):
    '''if : if_normal
            | if_else
            | if_else_if
            | if_else_if_else
            
            '''
    t[0] = t[1]
##self,condicion,instrucciones,ELSE,else_if,linea,columna
def p_if_normal(t):
    '''if_normal :  IF PARIZQ expresion PARDER LLAVEIZQ instrucciones LLAVEDER  '''
    params = get_params(t)
    t[0]=IF (t[3],t[6],None,None,params.line,params.column)
def p_if_else(t):
    '''if_else : IF PARIZQ expresion PARDER LLAVEIZQ instrucciones LLAVEDER ELSE LLAVEIZQ instrucciones LLAVEDER'''
    params = get_params(t)
    t[0]=IF (t[3],t[6],t[10],None,params.line,params.column)
def p_if_else_if(t):
    ''' if_else_if : IF PARIZQ expresion PARDER LLAVEIZQ instrucciones LLAVEDER elses_if '''
    params = get_params(t)
    t[0]=IF (t[3],t[6],None,t[8],params.line,params.column)

##self,condicion,instrucciones,ELSE,else_if,linea,columna
def p_if_else_if_else(t):
    '''if_else_if_else : IF PARIZQ expresion PARDER LLAVEIZQ instrucciones LLAVEDER elses_if ELSE LLAVEIZQ instrucciones LLAVEDER '''
    params = get_params(t)
    t[0]=IF (t[3],t[6],t[11],t[8],params.line,params.column)
def p_elses_if(t):
    '''elses_if : elses_if else_if
                | else_if'''
    params = get_params(t)
    if 2 < len(t):
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]
  
def p_else_if(t):
    '''else_if :  ELSE IF PARIZQ expresion PARDER LLAVEIZQ instrucciones LLAVEDER'''
    params = get_params(t)
    t[0]=IF (t[4],t[7],None,None,params.line,params.column)

##self,id,tipo_as,expresion,linea,columna
def p_asignacion(t):
    '''asignacion : ID IGUAL expresion
                    | ID SUMA_IGUAL expresion
                    | ID RESTA_IGUAL expresion
                    | llama_indice_arreglo IGUAL expresion
                    | llama_indice_arreglo SUMA_IGUAL expresion
                    | llama_indice_arreglo RESTA_IGUAL expresion
                    | llave_objeto IGUAL expresion
                    | llave_objeto SUMA_IGUAL expresion
                    | llave_objeto RESTA_IGUAL expresion
                    '''
    params = get_params(t)
    if len(t) == 4:
     if t[2] == '=':
         t[0]=asignacion(t[1],"=",t[3],params.line,params.column)
     elif t[2] == '+=':
         t[0]=asignacion(t[1],"+=",t[3],params.line,params.column)
     elif t[2] == '-=':
         t[0]=asignacion(t[1],"-=",t[3],params.line,params.column)
    elif len(t) == 6:
        if t[2] == '=':
         t[0]=asignacion(t[1],"=",t[4],params.line,params.column)

def p_declaracion_constantes(t):
    '''declaracion_constantes : constantes_con_tipo
                              | constantes_sin_tipo'''
    t[0] = t[1]
def p_constantes_con_tipo(t):
    '''constantes_con_tipo : CONST ID DOSPUNTOS tipo IGUAL expresion'''
    params = get_params(t)
    t[0] = declaracion(t[1],t[4],t[2],t[6],params.line,params.column)
def p_constantes_sin_tipo(t):
    '''constantes_sin_tipo : CONST ID IGUAL expresion'''
    params = get_params(t)
    t[0] = declaracion(t[1],None,t[2],t[4],params.line,params.column)

def p_declaracion_variables(t):
    ''' declaracion_variables : declaracion_tipo_valor
                              | declaracion_valor
                              | declaracion_tipo'''  
    t[0] = t[1]   
##self,tipo,tipo_dato,id,valor, fila, columna
def p_declaracion_valor(t):
    ''' declaracion_valor : VAR ID IGUAL expresion'''
    params=get_params(t)
    t[0] = declaracion(t[1],None,t[2],t[4],params.line,params.column)

def p_declaracion_tipo(t):
    '''declaracion_tipo : VAR ID DOSPUNTOS tipo'''
    params = get_params(t)
    t[0] = declaracion(t[1],t[4],t[2],None,params.line,params.column)
def p_declaracion_tipo_valor(t):
    '''declaracion_tipo_valor : VAR ID DOSPUNTOS tipo IGUAL expresion'''
    params = get_params(t)
    t[0] = declaracion(t[1],t[4],t[2],t[6],params.line,params.column)

#Listado de instrucciones
def p_instruccion_console(t):
    '''instruccion_console : CONSOLE PUNTO LOG PARIZQ expresiones PARDER PUNTOCOMA'''
    params = get_params(t)
    t[0] = console(t[5], params.line, params.column)

def p_tipo(t):
    '''tipo : NUMBER
            | STRING
            | BOOLEAN
            | CHAR
            | FLOAT
            
            
            '''
    if t[1] == 'number':
     t[0] = "NUMBER"
    elif t[1] == 'string':
     t[0] = "STRING"
    elif t[1] == 'boolean':
     t[0] = "BOOLEAN"
    elif t[1] == 'char':
     t[0] = "CHAR"
    elif t[1] == 'float':
     t[0] = "FLOAT"
#Expresion
def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                  | expresion MENOS expresion
                  | expresion POR expresion
                  | expresion DIVIDIDO expresion
                  | expresion MODULO expresion
                  | expresion MAYORQUE expresion
                  | expresion MENORQUE expresion
                  | expresion MAYORIGUAL expresion
                  | expresion MENORIGUAL expresion
                  | expresion IGUALIGUAL expresion
                  | expresion DISTINTO expresion
                  | expresion AND expresion
                  | expresion OR expresion
                  '''
    params = get_params(t)
    if t[2] == '+':
     
     t[0] = operacion(t[1], t[3], '+',params.line,params.column)
    elif t[2] == '-':
     t[0] = operacion(t[1], t[3], '-',params.line,params.column)
    elif t[2] == '*':
     t[0] = operacion(t[1], t[3], '*',params.line,params.column)
    elif t[2] == '/':
     t[0] = operacion(t[1], t[3], '/', params.line,params.column)
    elif t[2] == '%':
     t[0] = operacion(t[1], t[3], '%', params.line,params.column)
    elif t[2] == '>':
     t[0] = operacion(t[1], t[3], '>', params.line,params.column)
    elif t[2] == '<':
     t[0] = operacion(t[1], t[3], '<', params.line,params.column)
    elif t[2] == '>=':
     t[0] = operacion(t[1], t[3], '>=', params.line,params.column)
    elif t[2] == '<=':
     t[0] = operacion(t[1], t[3], '<=', params.line,params.column)
    elif t[2] == '==':
     t[0] = operacion(t[1], t[3], '==', params.line,params.column)
    elif t[2] == '!=':
     t[0] = operacion(t[1], t[3], '!=', params.line,params.column)
    elif t[2] == '&&':
     t[0] = operacion(t[1], t[3], '&&', params.line,params.column)
    elif t[2] == '||':
     t[0] = operacion(t[1], t[3], '||', params.line,params.column)
           
        

def p_expresion_unaria(t):
    '''expresion : MENOS expresion %prec UMENOS
                | NOT expresion'''
    params = get_params(t)
    if t[1] == '-':
     t[0] = operacion(None, t[2], '-',params.line,params.column)
    elif t[1] == '!':
     t[0] = operacion(None, t[2], '!',params.line,params.column)

def p_expresion_agrupacion(t):
    'expresion : PARIZQ expresion PARDER'
    t[0] = t[2]

def p_expresion_number(t):
    '''expresion    : ENTERO
                    | CADENA
                    | DECIMAL
                    | BOLEANO
                    | NULL
                    | CARACTER
                    | llamado_funcion
                    | llave_objeto
                    | corchete_expresion
                    
                    '''
    params = get_params(t)
    if isinstance(t[1],bool):
     print("se ha encontrado entero "+str(t[1]))
     t[0] = primitivo(t[1],"BOOLEAN",params.line,params.column)
     
    elif isinstance(t[1],str):
     if len(t[1]) == 1:
         t[0] = primitivo(t[1],"CHAR",params.line,params.column)
     else:
         t[0] = primitivo(t[1],"STRING",params.line,params.column)
    elif isinstance(t[1],float):
     
     t[0] = primitivo(t[1],"FLOAT",params.line,params.column)
     
    elif isinstance(t[1],int):
     t[0] = primitivo(t[1],"NUMBER",params.line,params.column)
    
    else:
     t[0] = t[1]

def p_ternario(t):
    '''expresion : expresion INTERROGACION expresion DOSPUNTOS expresion'''
    params = get_params(t)
    t[0] = ternario(t[1],t[3],t[5],params.line,params.column)
def p_object_values(t):
    '''expresion : OBJECT PUNTO VALUES PARIZQ ID PARDER'''
    params = get_params(t)
    t[0]=object_values(t[5],params.line,params.column)
def p_object_keys(t):
    '''expresion : OBJECT PUNTO KEYS PARIZQ ID PARDER'''
    params = get_params(t)
    t[0]=object_keys(t[5],params.line,params.column)

def p_llave_objeto(t):
    ''' llave_objeto : ID PUNTO llaves_objeto'''
    params = get_params(t)
    t[0] = llave_objeto(t[1],t[3],params.line,params.column)

def p_llaves_objeto(t):
    '''llaves_objeto : llaves_objeto PUNTO ID
                    | ID'''
    if 2 < len(t):
        t[1].append(t[3])
        t[0] = t[1]
    else:
        t[0] = [t[1]]
        
def p_to_upper_case(t):
    '''expresion : expresion PUNTO TO_UPPER_CASE PARIZQ PARDER
                 | ID PUNTO TO_UPPER_CASE PARIZQ PARDER 
     
    '''
    params = get_params(t)
    t[0] = UpperCase(t[1],params.line,params.column)

def p_type_of(t):
    '''expresion : TYPEOF expresion '''
    params = get_params(t)
    t[0] = typeOf(t[2],params.line,params.column)

def p_to_lower_case(t):
    '''expresion : expresion PUNTO  TO_LOWER_CASE PARIZQ  PARDER
                 | ID PUNTO TO_LOWER_CASE PARIZQ  PARDER'''
    params = get_params(t)
    t[0] = LowerCase(t[1],params.line,params.column)
def p_to_string(t):
    '''expresion : expresion PUNTO TO_STRING PARIZQ  PARDER
                 | ID PUNTO TO_STRING PARIZQ  PARDER
    '''
    params = get_params(t)
    t[0] = Tostring(t[1],params.line,params.column)     

def p_parse_float(t):
    '''expresion : PARSE_FLOAT PARIZQ expresion PARDER'''
    params = get_params(t)
    t[0] = parse_float(t[3],params.line,params.column)

def p_parse_int(t):
    '''expresion : PARSE_INT PARIZQ expresion PARDER'''
    params = get_params(t)
    t[0] = parse_int(t[3],params.line,params.column)

##self,nombre,expresiones,linea,columna
def p_llamado_funcion(t):
    '''llamado_funcion : ID PARIZQ PARDER
                        | ID PARIZQ expresiones PARDER'''
    params = get_params(t)
    if len(t) == 4:
     t[0] = llamado(t[1],None,params.line,params.column)
    else:
     t[0] = llamado(t[1],t[3],params.line,params.column)

def p_id(t):
    '''expresion : ID'''
    params = get_params(t)
    t[0] = id(t[1],params.line,params.column)


def p_operaciones_arreglo(t):
    '''expresion : llama_indice_arreglo
                    | pop
                    | length
                    | join
                    | index_of
                    
                    '''
    t[0] = t[1]

def p_llamada_indice_arreglo(t):
    '''llama_indice_arreglo : ID corchetes_expresion'''
    params = get_params(t)
    print(t[2])
    t[0] = indice_arreglo(t[1],t[2],params.line,params.column)

def p_corchetes_expresion(t):
    '''corchetes_expresion : corchetes_expresion corchete_expresion
                            | corchete_expresion'''
    if 2 < len(t):
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]


def p_index_of(t):
 '''index_of : ID PUNTO INDEX_OF PARIZQ expresion PARDER'''
 params=get_params(t)
 t[0] = indexof(t[1],t[5],params.line,params.column)
 
def p_length(t):
    '''length : ID PUNTO LENGTH'''
    params=get_params(t)
    t[0] = Len(t[1],params.line,params.column)

def p_join(t):
    '''join : ID PUNTO JOIN PARIZQ PARDER'''
    params=get_params(t)
    t[0] = Join(t[1],params.line,params.column)
def p_pop(t):
    '''pop : ID PUNTO POP PARIZQ PARDER'''
    params=get_params(t)
    t[0] = Pop(t[1],params.line,params.column)




def p_error(p):
    if p:
        
        print(f"Error de sintaxis en línea {p.lineno}, columna {p.lexpos}: Token inesperado '{p.value}'")
        ##descripcion,ambito,linea,columna,tipo
        errores.agregar_error(f"Token inesperado '{p.value}'","global",p.lineno,p.lexpos,"Sintáctico")
    else:
        print("Error de sintaxis")
        
        
def get_params(t):
 line = t.lexer.lineno  
 lexpos = t.lexpos if isinstance(t.lexpos, int) else 0  
 column = lexpos - t.lexer.lexdata.rfind('\n', 0, lexpos) 
 return codeParams(line, column)

if __name__ == '__main__':
    entorno_global = entorno("global",None)
    generador_=generador()
    entornos.agregar_entorno(entorno_global)
    f = open("./entrada.txt", "r")
    input_text = f.read()
    print("************ENTRADA***************")
    print(input_text)
    lexer = Lex.lex()
    parser = yacc.yacc()
    print("************SALIDA***************")
    result = parser.parse(input_text)
    for i in range(len(result)):
     valor= result[i].execute(entorno_global,generador_)
    
    print(generador_.get_final_code())
    
    
    
"""
def ingresar_texto(texto):
    entorno_global = entorno("global",None)
    entornos.agregar_entorno(entorno_global)
    input_text = texto
    print("************ENTRADA***************")
    print(input_text)
    lexer = Lex.lex()
    parser = yacc.yacc()
    print("************SALIDA***************")
    result = parser.parse(input_text)
    for i in range(len(result)):
     valor= result[i].execute(entorno_global)
    print(salida_instrucciones.instrucciones)
    print("************ERRORES***************")
    errores.get_errores()
"""