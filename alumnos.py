# Diccionario de diccionarios, tiene una clave unica (DNI) 
# el cual no vamos a modificar, pero sus datos internos son mutables
#por lo tanto podemos hacer modificaciones


def buscar_dni(alumno, dni_buscado):
    """Busca un DNI"""
    
    for dni_existente in alumno:
        if dni_existente == dni_buscado:
            return dni_existente
    
    return None


def registrar_alumno(alumno, dni, nombre, apellido, edad, nota):
    """Agrega alumnos al diccionario principal (alumno)"""

    alumno[dni] = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Edad": edad,
        "Nota": nota
    }


def existen_alumnos(alumno):
    """Comprueba si existen alumnos registrados."""

    if len(alumno) >= 1:
        return True

    return False


def modificar_alumnos(alumno, dni, campo, nuevo_valor):
    """Modifica el valor de una clave (edad, nota, nombre, apellido)
    de un alumno registrado"""
    
    alumno[dni][campo] = nuevo_valor

