# Importar módulos
import alumnos
import validaciones
import archivos
import estadisticas

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
            print("Has ingresado 0. Modificación cancelada.")  
        


print("========== ELIMINAR ALUMNO ==========")

eliminar_dni = input("Ingrese el DNI del alumno que desea eliminar: ")

while not validaciones.validar_formato_dni(eliminar_dni):
    print("Error. El DNI debe contener 8 dígitos.")
    eliminar_dni = input("Ingrese nuevamente el DNI: ")
    
dni_encontrado = alumnos.buscar_dni(alumno, eliminar_dni)

if dni_encontrado == None:
    print("No se encuentra alumno registrado con el DNI ingresado.")
else:
    alumnos.eliminar_alumno(alumno, dni_encontrado)

    archivos.guardar_alumno(alumno)

    print("Alumno eliminado correctamente.")



print("========== ESTADÍSTICAS ==========")

total = estadisticas.calcular_total_alumnos(alumno)
print("Cantidad total de alumnos:", total)


promedio = estadisticas.calcular_promedio_general(alumno)

if promedio == None:
    print("No existen alumnos para calcular el promedio.")
else:
    print("Promedio general de notas:", promedio)


mayor_nota = estadisticas.calcular_mayor_nota(alumno)

if mayor_nota == None:
    print("No existen alumnos para calcular la nota máxima.")
else:
    print("La nota máxima es:", mayor_nota)



aprobados = estadisticas.calcular_cantidad_aprobados(alumno)
print("La cantidad de aprobados es: ", aprobados)

desaprobados = estadisticas.calcular_cantidad_desaprobados(alumno)
print("La cantidad de desaprobados es: ", desaprobados) 
  
  

  
    
    
"""
def iniciar_menu(alumno):
    
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
                #Registrar alumno
                

iniciar_menu()
"""