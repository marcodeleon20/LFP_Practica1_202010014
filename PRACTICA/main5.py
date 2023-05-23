import os
from tkinter.filedialog import askopenfilename


NombreCurso= []
Parametro = []
nombreCursoxd=""
parametro = ''
contadorAPR = 0
ContadorREP = 0
ContadorClase = 0
x = ""
promedio = 0

def analizar(contenido):
    global nombreCursoxd
    global NombreCurso
    global parametro
    global contadorAPR 
    global ContadorREP
    global ContadorClase
    global x
    global promedio
         #titulo del cuso
    nombreCurso = ''
    for c in contenido:
        if c == '=':
            break
        else:
            nombreCurso += c
            nombreCursoxd +=c

    
    for a in nombreCurso:
        NombreCurso.append(a)
        
    
    #Curso antes de llaves 
    estudiantes = ''
    bandera = False
    for c in contenido:
        if c == '{':
            bandera = True
            continue

        if c != '}' and bandera :
            estudiantes += c
        elif c == '}':
            break

    #Leyendo estudiantes:

    estudiantes2 = ''
    bandera2 = False
    for c in estudiantes:
        if c == '<':
            bandera2 = True
            continue
        if c != '"' and bandera2:
            estudiantes2 += c
        elif c == '>':
            break
    #Leyendo estudiantes2:
    estudiantes3 = ''
    bandera3 = False
    for c in estudiantes2.strip(''and ';'and ','):
        if c == '>':
            bandera3 = True
            continue
        if c != '>' and bandera3:
            estudiantes3 += c
        elif c == '<':
            break


    #print(txtEstudiantes3.strip(' 'and';' and ','))
    
    #Mostrando datos en consola        
    lineas = splitear(estudiantes3.strip(';' and ','), ',')
    alumnos = obtenerEstudiantes(lineas)
    #desordenado
    print("****************************************")
    print("NOTAS FINALES CUARTO SEMESTRE")        
    print(nombreCurso + ":")
    print("****************************************")
    for a in alumnos:
        ContadorClase = ContadorClase+1
        print("*******************************************") 
        print("Nombre:", a.nombre,"," , "" ,"Nota:", a.nota)
        print("*******************************************")
    print("****************************************")
    print("La cantidad de alumnos en clase es:", ContadorClase)


    #Obteniendo parametros
    
    bandera = False
    for c in contenido:
        if c == '}':
            bandera = True
            continue

        if c != ' ' and bandera :
            parametro += c
        elif c == '}':
            break
    x = splitear(parametro,',')

    #PARÁMETROS
    for c in x:
        print("Parámetro:" + c)
        #ASC = Ordenar ascendentemente las notas de los estudiantes.
        if c == 'ASC':
            print("Ascendente")
            ordenarAscendentemente(lineas)

        #DESC = Ordenar descendentemente las notas de los estudiantes.
        elif c == 'DESC':
             print("Descendente")
             ordenarDescendentemente(lineas)
         
        #APR = Obtener el número de estudiantes aprobados en el curso.
        elif c == 'APR':
            print("Aprobados")
            for a in alumnos:
             if a.nota >= 61:
               contadorAPR = contadorAPR +1 
               print("*******************************************") 
               print("Nombre:", a.nombre,"," , "" ,"Nota:", a.nota)
               print("*******************************************")
             
            print("La cantidad de alumnos aprobados son :", contadorAPR) 

        #REP = Obtener el número de estudiantes reprobados en el curso.
        elif c == 'REP':
                print("Reprobados")
                for a in alumnos:
                 if a.nota <=60:  
                     ContadorREP = ContadorREP+1
                     print("*******************************************") 
                     print("Nombre:", a.nombre,"," , "" ,"Nota:", a.nota)
                     print("*******************************************")
                     
                print("La cantidad de alumnos reprobados son :", ContadorREP)

        #AVG = Obtener el promedio de los estudiantes del curso.
        elif c == 'AVG':
            print("OBTENER PROMEDIO")
            suma = 0
            pos = 0
            for a in alumnos:
                num = a.nota
                if num > 0:
                    suma+=num
                    pos +=1
            promedio = suma/pos
            print("Promedio de la clase", nombreCurso,"es:")
            print(round(promedio))

        #MIN = Obtener la nota mínima de los estudiantes del curso.
        elif c == 'MIN':
            menor(lineas)

        #MAX = Obtener la nota máxima de los estudiantes del curso.
        elif c == 'MAX':
           mayor(lineas)

    
    reporte = crearReporte(alumnos)
    crearArchivo('REPORTE.html', reporte)
    
def menu():
  while True:
    #print(f"=========Menu de opciones=========\n\
    #====>1. Cargar archivo <====\n\
    #====>2. Mostrar reporte en consola <====\n\
    #====>3. Exportar reporte <====\n\
    #====>4. Salir <====\n\ ")
    print("=========Menu de opciones=========")
    print("[ 1. Cargar archivo              ]")
    print("[ 2. Mostrar reporte en consola  ]")
    print("[ 3. Cargar archivo              ]")
    print("[ 4. Salir                       ]")
    print("==================================")
    opcion=input()
    if opcion=='1':
        filename = askopenfilename()
        codigo = leerArchivo(filename)
        print(f"Archivo cargado exitósamente.")
        print(f"Presione cualquier tecla para regresar al menú.")
    elif opcion=='2':
        
        analizar(codigo)

        print(f"El reporte ha sido mostrado exitósamente.")
        print(f"Presione cualquier tecla para regresar al menú.")
    elif opcion=='3':


        print(f"El reporte ha sido exportado exitósamente.")
        print(f"Presione cualquier tecla para regresar al menú.")
   
    elif opcion=='4':
        print("¡Muchas gracias por utilizar el programa!")
        break
    input()
    os.system("cls")

def crearArchivo(ruta, contenido):
    archivo = open(ruta, 'w')
    archivo.write(contenido)
    archivo.close()

class Alumno(object):
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

def leerArchivo(ruta):
    archivo = open(ruta, 'r')
    contenido = archivo.read()
    archivo.close()
    return contenido

def analizador2(contenido):
    parametro = ''
    bandera = False
    for c in contenido:
        if c == '}':
            bandera = True
            continue

        if c != ' ' and bandera :
            parametro += c
        elif c == '}':
            break
    x = splitear(parametro,',')
    for c in x:
        print("Parámetro:" + c)

def splitear(cadena, caracter):
    temporal = ""
    listaTemporal = []
    for i in cadena:
        if i == caracter:
            listaTemporal.append(temporal.strip())
            temporal = ""
        else:
            temporal += i
    if temporal.strip() != "":
        listaTemporal.append(temporal.strip())
    return listaTemporal

def obtenerEstudiantes(lnueva):
    listaNueva = []
    for linea in lnueva:
        datos = splitear(linea, ';')
        nombre = datos[0]
        nota = int(datos[1])
        persona = Alumno(nombre, nota)
        listaNueva.append(persona)
    return listaNueva

ListaNota=[]
ListaNombre=[]
ListaNota2=[]
ListaNombre2=[]

#Ordenamientos de notas
def ordenarAscendentemente(lista):
    global ListaNota
    global ListaNombre
    
    alumnos = obtenerEstudiantes(lista)
    for a in alumnos:
        ListaNota.append(a.nota)
        ListaNombre.append(a.nombre)
    
        
    ordenado=False
    while ordenado==False:
        ordenado=True
        for w in range(len(ListaNota)-1):
            if ListaNota[w]<ListaNota[w+1]:
                auxiliar=ListaNota[w]
                ListaNota[w]=ListaNota[w+1]
                ListaNota[w+1]=auxiliar
                auxiliar2=ListaNombre[w]
                ListaNombre[w]=ListaNombre[w+1]
                ListaNombre[w+1]=auxiliar2
                ordenado=False
    cont=0
    for i in ListaNota:
        print("Nombre:",",", ListaNombre[cont],"Nota:", i)
        cont=cont+1

def ordenarDescendentemente(lista):

    global ListaNota2
    global ListaNombre2
    
    alumnos = obtenerEstudiantes(lista)
    for a in alumnos:
        ListaNota2.append(a.nota)
        ListaNombre2.append(a.nombre)
       
    ordenado=False
    while ordenado==False:
        ordenado=True
        for w in range(len(ListaNota2)-1):
            if ListaNota2[w]>ListaNota2[w+1]:
                auxiliar=ListaNota2[w]
                ListaNota2[w]=ListaNota2[w+1]
                ListaNota2[w+1]=auxiliar
                auxiliar2=ListaNombre2[w]
                ListaNombre2[w]=ListaNombre2[w+1]
                ListaNombre2[w+1]=auxiliar2
                ordenado=False
    contador=0
    for i in ListaNota2:
        print("Nombre:", ListaNombre2[contador],",","Nota:", i)
        contador=contador+1

NotaAlta=[]

z = 0
w = 0
#Max y min de las notas
def mayor(lista):
    global ListaNota
    global ListaNombre
    global z

    z = max(ListaNota)
    print("la nota máxima es:", z)

def menor(lista):
    global ListaNota
    global ListaNombre
    global w

    w = min(ListaNota)
    print("la nota mínima es:", w)

def crearReporte(lista):
    global NombreCurso
    global nombreCursoxd
    global parametro
    global contadorAPR 
    global ContadorREP
    global ContadorClase
    global x
    global promedio
    global z
    global w
    global ListaNota
    global ListaNombre
    global ListaNota2
    global ListaNombre2


    cont=ContadorClase
    contaAPR = str(contadorAPR)
    contaREP = str(ContadorREP)
    prom = round(promedio)

    inicio = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>REPORTES</title></head><body>\n  <center>\n<div class=\"jumbotron text-center\">\n  <h1><b><u>UNIVERSIDAD DE SAN CARLOS DE GUATEMALA</u></b></h1>\n </center>\n  <center>\n <h2>Se muestras los datos solicitados:</h2> </center>\n  <body  bgcolor=\"FFE5C4\">\n   <font size =\"4\" color=\"white\" face=\"Comic Sans MS,arial\">  </div>\n   '
   
   
    fin = '</table> </body> <div class=\"well well-sm\" style=\"background-color: black;\">\n <font size=5 color=\"white\" face=\"Comic Sans MS,arial\"> <center>\n  <h2>DATOS GENERALES</h2></font> </center>\n  </div>\n <br>\n <hr> <font size=5 color=\"Black\" face=\"Comic Sans MS,arial\"> <center>   <br><p>Facultad de Ingenieria</p>\n  <br>\n  <p>Escuela de Ciencias y Sistemas</p>\n <br>\n  <p>Lenguajes Formales y de Programacion</p>\n <br>\n <p>Seccion B+</p>\n  <br>\n  <p>Catedratico: Ing. David Morales</p>\n     <br>\n  <p>Tutor academico: Bryan Lopez</p>\n <br>\n  <p>Marco Alexander de Leon Hernandez</p>\n    <br>\n  <p>202010014</p>\n    <br>\n   <p>UNIVERSIDAD DE SAN CARLOS DE GUATEMALA.</p>\n  </center>  </font> </body>\n  \n     </html>'
    
    inicio += "<center>\n<tr><td><font size =\"10\", color =\"black\">" +nombreCursoxd  + "</font></td></tr></center>\n "

    inicio += "<center><img src=\"Usac_logo.png\"/></center>\n"

    inicio += "<center><img src=\"usac.png\"/></center>\n"

    inicio += "<br>"


    inicio += "<center>\n<table border=\"1\">\n<tr><th><font size=\"5\" color=\"black\">No.</font></th><th><font size=\"5\" color=\"black\">Nombre</font></th><th><font size=\"5\" color=\"black\">Nota</font></th></tr>\n"

    contador = 1
    for a in lista:
        if a.nota >= 61:
            inicio += "<tr><td><font size=\"5\" color=\"black\">" + str(contador) + "</font></td><td><font size=\"5\" color=\"blue\">" + a.nombre + "</font></td><td><font size=\"5\" color=\"blue\">" + str(a.nota) + "</font></td></tr>\n"
        elif a.nota <= 60:
            inicio += "<tr><td><font size=\"5\" color=\"black\">" + str(contador) + "</font></td><td><font size=\"5\" color=\"red\">" + a.nombre + "</font></td><td><font size=\"5\" color=\"red\">" + str(a.nota) + "</font></td></tr>\n"
        contador += 1
    
    inicio += "</table></center>\n"
    inicio += "<center>\n<table border=\"1\"><tr><td><font size=\"5\" color=\"black\">El numero de estudiantes en la clase es: " + str(cont) + "</font></td></tr></table></center>\n"



    #PARÁMETROS
    inicio += "<div class=\"well well-sm\" style=\"background-color: black;\">\n <center>\n  <h2>PARAMETROS</h2> </center>\n  </div>\n \n  </div>\n"
    
    for c in x:
        inicio += "<center>\n<table border=\"1\"><tr><td><font size =\"5\", color =\"black\">Parametros: " + c +"</font></td></tr></center>\n"
        inicio += "<br>"
        #ASC = Ordenar ascendentemente las notas de los estudiantes.
        if c == 'ASC':
            inicio += "<font size =\"5\", color =\"black\">Ascendente:\n</font>"
            cont=0
            inicio += "<center>\n<table border=\"1\">\n<tr><th><font size=\"5\" color=\"black\">Nombre</font></th><th><font size=\"5\" color=\"black\">Nota</font></th></tr>\n"

            for i in ListaNota2:
                inicio += "<tr><td><font size=\"5\" color=\"black\">" + ListaNombre2[cont] + "</font></td><td><font size=\"5\" color=\"black\">" + str(i) + "</font></td></tr>\n"
                cont += 1

            inicio += "</table></center>\n"

            #ordenarAscendentemente(lista)

        #DESC = Ordenar descendentemente las notas de los estudiantes.
        elif c == 'DESC':
            inicio += "<font size =\"5\", color =\"black\">Descendente:\n"
            cont=0
            inicio += "<center>\n<table border=\"1\">\n<tr><th><font size=\"5\" color=\"black\">Nombre</font></th><th><font size=\"5\" color=\"black\">Nota</font></th></tr>\n"

            for i in ListaNota:
                inicio += "<tr><td><font size=\"5\" color=\"black\">" + ListaNombre[cont] + "</font></td><td><font size=\"5\" color=\"black\">" + str(i) + "</font></td></tr>\n"
                cont += 1

            inicio += "</table></center>\n"

             #ordenarDescendentemente(lista)
         
        #APR = Obtener el número de estudiantes aprobados en el curso.
        elif c == 'APR':
            inicio += "<font size =\"5\", color =\"black\">Aprobados:\n"
        
            inicio +="<font size =\"5\", color =\"black\">La cantidad de alumnos aprobados son :" + contaAPR +"</font>"
            inicio += "<br>"

        #REP = Obtener el número de estudiantes reprobados en el curso.
        elif c == 'REP':
                inicio += "<font size =\"5\", color =\"black\">Reprobados:\n </font>"
                     
                inicio += "<font size =\"5\", color =\"black\">La cantidad de alumnos aprobados son :" + contaREP+"</font>"
                inicio += "<br>"

        #AVG = Obtener el promedio de los estudiantes del curso.
        elif c == 'AVG':
            inicio += "<font size =\"5\", color =\"black\">Promedio:\n"
          
            inicio += "<font size =\"5\", color =\"black\">Promedio de la clase\n" + nombreCursoxd +"es:"+"</font>"
            inicio += str(prom)  
            inicio += "<br>"          

        #MIN = Obtener la nota mínima de los estudiantes del curso.
        elif c == 'MIN':
            inicio += "<font size =\"5\", color =\"black\">La nota minima de\n" + nombreCursoxd+ "es:\n"+ str(w)+"</font>"
            inicio += "<br>"

        #MAX = Obtener la nota máxima de los estudiantes del curso.
        elif c == 'MAX':
            inicio += "<font size =\"5\", color =\"black\">La nota maxima de\n" + nombreCursoxd + "es:\n"+ str(z)+"</font>"
            inicio += "<br>"

   
    return inicio + fin


if __name__ == '__main__':

    menu()

   
    
    




