# Importar módulos
import alumnos
import validaciones
import archivos


# Inicializar el diccionario
alumno = archivos.cargar_alumno()


# Solicitar los datos del alumno
print("Registrarás un nuevo alumno/a.")

dni = input("Ingresa su DNI: ") 
while not validaciones.validar_dni_ingresado(alumno, dni):
    print("Error. El DNI debe contener 8 dígitos y no estar registrado.")
    dni = input("Ingrese un nuevo DNI: ")


nombre = input("Ingresa su NOMBRE: ")
while not validaciones.validar_nombre_apellido(nombre):
    print("Error. Debe ingresar un nombre válido de hasta 14 caracteres.")
    nombre = input("Ingrese NOMBRE: ")


apellido = input("Ingresa su APELLIDO: ")
while not validaciones.validar_nombre_apellido(apellido):
    print("Error. Debe ingresar un apellido válido de hasta 14 caracteres.")
    apellido = input("Ingrese APELLIDO: ")


edad = input("Ingresa su EDAD: ")
while not validaciones.validar_edad_ingresada(edad):
    print("Error. Debe ingresar un número entero mayor a cero.")
    edad = input("Ingrese nuevamente EDAD: ")
    
edad = int(edad)
    
    
nota = input("Ingresa su NOTA: ")
while not validaciones.validar_nota_ingresada(nota):
    print("Error. Debe ingresar una nota válida.")
    nota = input("Ingrese nuevamente NOTA: ")
    
nota = float(nota)


# Llamar a la función registrar alumno
alumnos.registrar_alumno(alumno, dni, nombre, apellido, edad, nota)


#Guardar cambios en JSON
archivos.guardar_alumno(alumno)


print("========== LISTADO DE ALUMNOS ==========")

if alumnos.existen_alumnos(alumno):

    for dni in alumno.keys():
        print("DNI:", dni)
        print("Nombre:", alumno[dni]["Nombre"])
        print("Apellido:", alumno[dni]["Apellido"])
        print("Edad:", alumno[dni]["Edad"])
        print("Nota:", alumno[dni]["Nota"])
        print("------------------------")

else:
    print("No hay alumnos registrados en el sistema.")
    


print("========== BUSCAR ALUMNO ==========")

dni_buscado = input("Ingrese el DNI que desea buscar: ")

while not validaciones.validar_formato_dni(dni_buscado):
    print("Error. El DNI debe contener 8 dígitos.")
    dni_buscado = input("Ingrese nuevamente el DNI: ")

dni_encontrado = alumnos.buscar_dni(alumno, dni_buscado)

if dni_encontrado == None:
    print("No se encuentra alumno registrado con el DNI ingresado.")
else:
    print("Alumno encontrado.")
    print("DNI:", dni_encontrado)
    print("Nombre:", alumno[dni_encontrado]["Nombre"])
    print("Apellido:", alumno[dni_encontrado]["Apellido"])
    print("Edad:", alumno[dni_encontrado]["Edad"])
    print("Nota:", alumno[dni_encontrado]["Nota"])


print("========== MODIFICAR ALUMNO ==========")

dni_modificar = input("Ingrese el DNI del alumno que desea modificar: ")

while not validaciones.validar_formato_dni(dni_modificar):
    print("Error. El DNI debe contener 8 dígitos.")
    dni_modificar = input("Ingrese nuevamente el DNI: ")

dni_encontrado = alumnos.buscar_dni(alumno, dni_modificar)    
if dni_encontrado == None:
    print("No se encuentra alumno registrado con el DNI ingresado.")
else:
    print("Alumno encontrado.")
    print("DNI:", dni_encontrado)
    print("Nombre:", alumno[dni_encontrado]["Nombre"])
    print("Apellido:", alumno[dni_encontrado]["Apellido"])
    print("Edad:", alumno[dni_encontrado]["Edad"])
    print("Nota:", alumno[dni_encontrado]["Nota"])
    
    print("========== MODIFICAR DATOS ==========")
    print("1. Modificar nombre")
    print("2. Modificar apellido")
    print("3. Modificar edad")
    print("4. Modificar nota")
    print("0. Cancelar modificación")

    opcion_modificar = input("Seleccione una opción: ")
    
    while not validaciones.validar_opcion_modificar(opcion_modificar):
        print("Error. Debe ingresar una opción entre 0 y 4.")
        opcion_modificar = input("Seleccione una opción: ")
    
    match opcion_modificar:
        case "1":
            #Solicitar nombre y modificarlo
            nuevo_nombre = input("Ingrese el nuevo nombre: ")

            while not validaciones.validar_nombre_apellido(nuevo_nombre):
                print("Error. Debe ingresar un nombre válido.")
                nuevo_nombre = input("Ingrese el nuevo nombre: ")

            alumnos.modificar_alumnos(alumno, dni_encontrado, "Nombre", nuevo_nombre)

            archivos.guardar_alumno(alumno)

            print("Nombre modificado correctamente.")

        case "2":
            #Solicitar apellido y modificarlo
            nuevo_apellido = input("Ingrese el nuevo apellido: ")

            while not validaciones.validar_nombre_apellido(nuevo_apellido):
                print("Error. Debe ingresar un apellido válido.")
                nuevo_apellido = input("Ingrese el nuevo apellido: ")

            alumnos.modificar_alumnos(alumno, dni_encontrado, "Apellido", nuevo_apellido)

            archivos.guardar_alumno(alumno)

            print("Apellido modificado correctamente.")

        case "3":
            #Solicitar edad y modificarla
            nueva_edad = input("Ingrese edad actualizada: ")

            while not validaciones.validar_edad_ingresada(nueva_edad):
                print("Error. Debe ingresar una edad válida.")
                nueva_edad = input("Ingrese edad actualizada: ")
                

            nueva_edad = int(nueva_edad)
            
            alumnos.modificar_alumnos(alumno, dni_encontrado, "Edad", nueva_edad)

            archivos.guardar_alumno(alumno)

            print("Edad modificada correctamente.")

        case "4":
            #Solicitar nota y modificarla
            nueva_nota = input("Ingrese nota actualizada: ")

            while not validaciones.validar_nota_ingresada(nueva_nota):
                print("Error. Debe ingresar una nota válida.")
                nueva_nota = input("Ingrese nota actualizada: ")
                

            nueva_nota = float(nueva_nota)
            
            alumnos.modificar_alumnos(alumno, dni_encontrado, "Nota", nueva_nota)

            archivos.guardar_alumno(alumno)

            print("Nota modificada correctamente.")

        case "0":
            pass  
        

"""
def iniciar_menu():
    
    opcion = ""
    
    while opcion != "0":
    
        opcion = input(
                "¡Bienvenido/a!\n"
                "====== GESTIÓN DE AUMNOS ======\n"
                "1. Registrar alumno\n"
                "2. Listar alumnos\n"
                "3. Buscar alumno\n"
                "4. Modificar alumno\n"
                "5. Eliminar alumno\n"
                "6. Ver estadísticas\n"
                "0. Salir\n"
                "Selecciona una opción para continuar: "
            )
        
        match opcion:
            case "1":
                #Carga de libros
                #Solicitar cantidad para determinar valor de listas
                cantidad_alumnos = validaciones.validar_cantidad()
                    
                #Inicializacion de las listas paralelas
                nombres = [""] * cantidad_alumnos #str
        
                for i in range(cantidad_alumnos):
                    nombres[i] = input("Ingrese el nombre del alumno/a: ")
            
                    while not validaciones.validar_nombre(nombres[i]): #Validar que sea con más de 5 caracteres. No números, no espacio.
                        print("Nombre inválido, debe tener al menos 5 caracteres.")
                        nombres[i] = input("Ingrese el nombre del alumno: ")
            
            
                    parcial_1[i] = int(input("Ingrese la nota del parcial 1 (1 a 10): ")) #Ingresa nota  parcial 1(int)
            
                    while not validaciones.validar_nota(parcial_1[i]): #Llamar a la funcion para validar que la nota esté dentro del 1 al 10
                        parcial_1[i] = int(input("Número inválido. Ingrese un número del 1 al 10 para la primer nota: "))
            
            
                    parcial_2[i] = int(input("Ingrese la nota del parcial 2 (1 a 10): ")) #Ingresa nota parcial 2(int)
            
                    while not validaciones.validar_nota(parcial_2[i]): #Llamar a la funcion para validar que la nota esté dentro del 1 al 10
                        parcial_2[i] = int(input("Número inválido. Ingrese un número del 1 al 10 para la segunda nota: "))
        
                        
                    #Calcular promedio de cada alumno
                    promedio[i] = procesamiento.calcular_promedio(parcial_1[i], parcial_2[i])
                    
                print("Alumnos cargados con éxito.")
                alumnos_cargados = True
                    
                    
            case "2":
                
            
            case "3": #
                
                
        
            case "4": #Ranking
                
            case "5": #Buscar alumno
                
        
            case "6": #Juegos con un nombre
                
    
            case "0":
                print("Ha seleccionado la opción SALIR. Hasta pronto.")

            case _:
                print("Opción no válida. Ingrese una opción de 1 al 6 (o 0 para SALIR): ")


iniciar_menu()
"""