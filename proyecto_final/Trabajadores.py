
#------------------------------------------------------ SUB MENU 1 -----------------------------------------------------

#Crea un  diccionario trabajador donde almacenar a los trabajadores-----------------------------------------------------
trabajador = {}

trabajador["Nombre"] = [30, 123, "Profesion", True ]
#------------------------------------------------------- opcion 1 ------------------------------------------------------
#Crea un trabajador y lo guarda en la lista trabajadores----------------------------------------------------------------
def agregar (trabajador):
    while True :
        Nombre = input ("INGRESE NOMBRE\n")
        if Nombre in trabajador.keys():
                print("TRABAJADOR REGISTRADO")
                break 
        else :
            while True : 
                try: 
                    Edad = int(input ("INGRESE EDAD\n"))
                    break
                except:
                    print ("ERROR , INTENTE NUEVAMENTE\n")
            while True :
                try:
                    Dni = int(input ("INGRESE DNI\n"))
                    break
                except : 
                    print ("ERROR , INTENTE NUEVAMENTE\n")

            Profesion = input ("INGRESE PROFESION\n")
            Activo = input ("EN ACTIVIDAD Y/N\n")
            while(Activo != True and Activo != False):
                if(Activo=="Y"):
                    Activo=True
                elif(Activo=="N"):
                    Activo=False
                else:
                    Activo = input ("ERROR , INTENTE NUEVAMENTE\n")
            trabajador[Nombre] = [Edad, Dni, Profesion, Activo ]
            print ("TRABAJADOR CARGADO CON EXITO")
            break

#------------------------------------------------------- opcion 2 ------------------------------------------------------        
#Recorre la lista trabajadores y modifica el valor seleccionado del al trabajador con el nombre ingresado--------------- 
def modificar (trabajador):
    while True:
        Nombre  = input ("INGRESAR NOMBRE DE TRABAJADOR\n")
        if Nombre not in trabajador.keys():
            print ("no se encontro el trabajador")
        else :
            opcion = input (f'''========== MODIFICAR ==========
            escoja una opcion
            1 - MODIFICAR NOMBRE
            2 - MODIFICAR EDAD
            3 - MODIFICAR DNI 
            4 - MODIFICAR PROFESION\n''')
            if opcion == "1":
                modificarNombre(Nombre,trabajador)
                break
            elif opcion == "2":
                modificarEdad(Nombre,trabajador)
                break
            elif opcion == "3":
                modificarDni(Nombre,trabajador)
                break
            elif opcion == "4":
                modificarProfesion(Nombre,trabajador)
                break
            else :
                print("seleccion incorrecta")

#Recorre la lista trabajadores y modifica el nombre del trabajador seleccionado ----------------------------------------- 
def modificarNombre(Nombre,trabajador):

    cambio = input ("ingrese nuevo nombre\n")
    while cambio in trabajador.keys():
        cambio = input("trabajador ya existente , ingrese otro\n")
    trabajador[cambio]=trabajador[Nombre]
    trabajador.pop(Nombre)
    print ("SE AGREGO CORRECTAMENTE")

#Recorre la lista trabajadores y modifica la edad del trabajador seleccionado -------------------------------------------
def modificarEdad(Nombre,trabajador):
    while True:
        try: 
            Edad = int(input ("INGRESE EDAD\n"))
            break
        except:
            print ("ERROR , INTENTE NUEVAMENTE\n")
    trabajador[Nombre][0]=Edad
    print ("SE AGREGO CORRECTAMENTE")

#Recorre la lista trabajadores y modifica el dni del trabajador seleccionado -------------------------------------------
def modificarDni(Nombre,trabajador):
    while True:
        try: 
            Dni = int(input ("INGRESE DNI\n"))
            break
        except:
            print ("ERROR , INTENTE NUEVAMENTE\n")
    trabajador[Nombre][1]=Dni
    print ("SE AGREGO CORRECTAMENTE")

#Recorre la lista trabajadores y modifica la profesion del trabajador seleccionado --------------------------------------
def modificarProfesion(Nombre,trabajador):

    Profesion = input ("INGRESE PROFESION\n")
    trabajador[Nombre][2]=Profesion

#------------------------------------------------------- opcion 3 ------------------------------------------------------
#Recorre la lista trabajadores y elimina al trabajador con el nombre ingresado------------------------------------------ 
def eliminar (trabajador):

    Nombre = input ("INGRESE NOMBRE A ELIMINAR\n")
    if Nombre not in trabajador.keys():
        print("no se encontro el trabajador")
    else :
        trabajador.pop(Nombre)
        print("trabajador eliminado con exito")

#------------------------------------------------------ SUB MENU 2 -----------------------------------------------------

#------------------------------------------------------- opcion 1 ------------------------------------------------------
#Recorre la lista trabajadores y muestra a los trabajadores activos-----------------------------------------------------            
def mostrarActivos (trabajador):
    
    vacio = True
    print (" ______________ TRABAJADORES ACTIVOS ______________")
    for Nombre in trabajador.keys():
        if (trabajador[Nombre][3] == True):
            print(f'''
            Nombre: {Nombre}
            Edad: {trabajador [Nombre][0]}
            Dni: {trabajador [Nombre][1] }
            Profesion: {trabajador[Nombre][2]}
            Activo: {trabajador[Nombre][3]}''')
            vacio = False
    if(vacio == True):
        print("no existen trabajadores desocupados con la edad ingresada")  

#------------------------------------------------------- opcion 2 ------------------------------------------------------
#Recorre la lista trabajadores y muestra a los trabajadores desocupados-------------------------------------------------            
def mostrarDesocupados (trabajador):

    vacio = True
    print ("______________ TRABAJADORES DESOCUPADOS ______________")
    for Nombre in trabajador.keys():
        if (trabajador[Nombre][3] == False):
            print(f''' 
            Nombre: {Nombre}
            Edad: {trabajador [Nombre][0]}
            Dni: {trabajador [Nombre][1] }
            Profesion: {trabajador[Nombre][2]}
            Activo: {trabajador[Nombre][3]}''')
            vacio = False
    if(vacio == True):
        print("no existen trabajadores desocupados")          

#------------------------------------------------------- opcion 3 ------------------------------------------------------
#Recorre la lista trabajadores y muestra a los trabajadores desocupados de la edad ingresada----------------------------            
def desocupadosEdad (trabajador):
    vacio = True
    while True:
        try: 
            Edad = int(input ("INGRESE EDAD\n"))
            break
        except:
            print ("ERROR , INTENTE NUEVAMENTE\n")
    print ("______________ TRABAJADORES DESOCUPADOS CON {Edad} AÑOS ______________")
    for Nombre in trabajador.keys():
        if (trabajador[trabajador][3] == False and trabajador[Nombre][0] == Edad):
            print(f''' 
            Nombre: {Nombre}
            Edad: {trabajador [Nombre][0]}
            Dni: {trabajador [Nombre][1] }
            Profesion: {trabajador[Nombre][2]}
            Activo: {trabajador[Nombre][3]}''')
            vacio = False
    if(vacio == True):
        print("no existen trabajadores desocupados con la edad ingresada")

#------------------------------------------------------- opcion 4 ------------------------------------------------------
#Recorre la lista trabajadores y muestra a los trabajadores segun la profesion ingresada -------------------------------            
def mostrarProfesion (trabajador):
    vacio = True
    Profesion = input ("INGRESE PROFESION\n")
    print (" ______________ TRABAJADORES ______________")
    for Nombre in trabajador.keys():
        if (trabajador[Nombre][2] == Profesion):
            print(f'''
            Nombre: {Nombre}
            Edad: {trabajador [Nombre][0]}
            Dni: {trabajador [Nombre][1] }
            Profesion: {trabajador[Nombre][2]}
            Activo: {trabajador[Nombre][3]}''')
            vacio = False
    if(vacio == True):
        print("no existen trabajadores con la profesion ingresada")