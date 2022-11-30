import Trabajadores

#Crea un  diccionario trabajador donde almacenar a los trabajadores-----------------------------------------------------
trabajador={}

#------------------------------------------------------ SUB MENU 3 -----------------------------------------------------

#------------------------------------------------------- opcion 1 ------------------------------------------------------
#Recorre la lista trabajadores y activa al trabajador seleccionado ----------------------------------------------------- 
def activar(trabajador):

    Nombre  = input ("INGRESAR NOMBRE DE TRABAJADOR\n")
    if Nombre not in trabajador.keys():
        print ("no se encontro el trabajador")
    else :
        trabajador[Nombre][3]=True
        print ("trabajador activado con exito")

#------------------------------------------------------- opcion 2 ------------------------------------------------------
#Recorre la lista trabajadores y desactiva al trabajador seleccionado ----------------------------------------------------- 
def desActivar(trabajador):

    Nombre  = input ("INGRESAR NOMBRE DE TRABAJADOR\n")
    if Nombre not in trabajador.keys():
        print ("no se encontro el trabajador")
    else :
        trabajador[Nombre][3]=False
        print ("trabajador desactivado con exito")

#---------------------------------------------------- MENU PRINCIPAL ----------------------------------------------------
while True:
    
    opcion = input (f'''========== CONSULTORA DE TRABAJO ==========
        1- GESTION DE TRABAJADORES
        2- REPORTE
        3- CAMBIAR EL ESTADO DE UN TRABAJADOR
        4 - SALIR\n''')

#------------------------------------------------------ sub menu 1 -----------------------------------------------------
    if opcion == "1":
        while True :
            opcion2 = input (f''' ========== GESTION DE TRABAJADORES ==========
            1- INGRESAR NUEVO TRABAJADOR
            2- MODIFICAR DATO DE TRABAJADOR
            3- ELIMINAR TRABAJADOR
            4 - VOLVER\n''')

            if opcion2 == "1":
                Trabajadores.agregar(trabajador)
            elif opcion2 == "2":
                Trabajadores.modificar(trabajador)
            elif opcion2 == "3":
                Trabajadores.eliminar(trabajador)
            elif opcion2 == "4":
                break
        
#------------------------------------------------------ sub menu 2 -----------------------------------------------------
    elif opcion == "2" :
        while True :
            opcion2 = input (f''' ========== REPORTE ==========
            1- TRABAJADORES ACTIVOS
            2- TRABAJADORES DESOCUPADOS
            3- DESOCUPADOS SEGUN EDAD
            4- TRABAJADORES SEGUN PROFESION
            5- VOLVER\n''')

            if opcion2 == "1":
                Trabajadores.mostrarActivos(trabajador)
            elif opcion2 == "2":
                Trabajadores.mostrarDesocupados(trabajador)
            elif opcion2 == "3":
                Trabajadores.desocupadosEdad(trabajador)
            elif opcion2 == "4":
                Trabajadores.mostrarProfesion(trabajador)                
            elif opcion2 == "5":
                break
        
#------------------------------------------------------ sub menu 3 -----------------------------------------------------
    elif opcion == "3" :
        while True :
            opcion2 = input ('''========== CAMBIAR ESTADO DE UN TRABAJADOR ==========
            1 - ACTIVO
            2 - INACTIVO
            3 - VOLVER\n''')
            
            if opcion2 == "1":
                activar (trabajador)
            elif opcion2 == "2":
                desActivar (trabajador)            
            elif opcion2 == "3":
                break
    
#-------------------------------------------------------- SALIDA -------------------------------------------------------
    elif  opcion == "4" :
        break
    else:
        print("Ingrese una opcion valida")