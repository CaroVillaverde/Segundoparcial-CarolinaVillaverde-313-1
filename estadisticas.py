import alumnos

def calcular_cantidad_aprobados(alumno):
    """Calcula la cantidad de alumnos aprobados"""
    
    contador = 0 
    
    for datos in alumno.values():
        if datos["Nota"] >= 6: 
            contador += 1
    
    return contador 


def calcular_cantidad_desaprobados(alumno):
    """Calcula la cantidad de alumnos desaprobados"""
    
    contador = 0 
    
    for datos in alumno.values():
        if datos["Nota"] < 6: 
            contador += 1
    
    return contador 

    
def calcular_mayor_nota(alumno):
    """Obtiene la nota más alta de los alumnos registrados."""

    
    if alumnos.existen_alumnos(alumno):
        nota_maxima = 0

        for datos in alumno.values():
            if datos["Nota"] > nota_maxima:
                nota_maxima = datos["Nota"]

        return nota_maxima

    return None
        
        
def calcular_promedio_general(alumno):
    """Calcula el promedio general de las notas."""

    if alumnos.existen_alumnos(alumno):
        acumulador = 0

        for datos in alumno.values():
            acumulador += datos["Nota"]

        promedio = acumulador / calcular_total_alumnos(alumno)

        return promedio

    return None


def calcular_total_alumnos(alumno):
    """Calcula la cantidad de alumnos registrados."""

    return len(alumno)


