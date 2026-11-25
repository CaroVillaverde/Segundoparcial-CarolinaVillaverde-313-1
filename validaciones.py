#Funciones ordenadas alfabeticamente
"""
def pedir_decimal(nota):
    
    texto = input(nota)
    
    while not validar_decimal(texto):
        print("Debe ingresar un número entero válido, no negativo")
        texto = input(nota)
        
    return float(nota)


def pedir_entero(x):
    
    texto = input(x)
    
    while not validar_entero_no_negativo(x):
        print("Debe ingresar un número entero válido, no negativo")
        texto = input(x)
        
    return int(x)


def pedir_texto(mensaje):
    
    texto = input(mensaje)
    
    while not validar_texto(texto):
        print("Error. El campo no puede estar vacío.")
        texto = input(mensaje)
        
    return texto
"""


def validar_decimal(nota):
    """ Comprueba que lo ingresado sea un decimal """
    valido = True
    puntos = 0
    
    if nota == "" or nota == ".":
        valido = False
    
    for i in range(len(nota)):
        if nota [i] == ".":
            puntos += 1 
        elif nota[i] < "0" or nota[i] > "9":
            valido = False
    
    if puntos > 1:
        valido = False
        
    return valido 


#Validar que DNI no se repita
def validar_dni_duplicado(alumno, dni):
    """Comprueba si un DNI está registrado"""
    
    for clave in alumno.keys():
        if dni == clave:
            return True
        
    return False 


def validar_dni_ingresado(alumno, dni):
    """Comprueba el dni que se ingresa y verifica que no esté registrado"""
    if validar_formato_dni(dni) and validar_dni_duplicado(alumno, dni) == False:
        return True
    
    return False
        
        
        
def validar_edad(edad: int):
    """ Comprueba que la edad sea mayor a cero."""
    
    valido = True
    
    if edad < 1:
        valido = False
    
    return valido


def validar_edad_ingresada(edad: str):
    """Comprueba que la edad sea entero y su rango."""

    if validar_entero_no_negativo(edad):
        edad = int(edad)
        return validar_edad(edad)

    return False


def validar_entero_no_negativo(dato: str):
    """Comprueba que el número no sea negativo y sea un entero"""
    
    valido = True
    
    if dato == "":
        valido =  False
        
    for i in range(len(dato)):
        if dato[i] < "0" or dato[i] > "9": 
            valido = False
    
    return valido 


def validar_formato_dni(dni: str):
    """Comprueba que el DNI tenga 8 dígitos y que sean números."""

    valido = False
    
    if validar_entero_no_negativo(dni) and len(dni) == 8:
        valido = True

    return valido


def validar_letras_espacios(texto: str):
    """Comprueba que el texto solo tenga letras y espacios."""
    
    valido = True 
    
    for i in range(len(texto)):
        if texto[i].isalpha() == False and texto[i] != " ":
            valido = False
    
    return valido 

def validar_nombre_apellido(texto: str):
    "Comprueba el formato y longitud del nombre/apellido"
    
    if validar_texto(texto) and len(texto) <= 14 and validar_letras_espacios(texto):
        valido = True
    else:
        valido = False
    
    return valido
    
    
def validar_nota_ingresada(nota: str):
    """Comprueba la nota y su rango."""
    
    if validar_decimal(nota):
        nota = float(nota)
        return validar_rango_nota(nota)
    
    return False           
    
    
def validar_opcion_modificar(opcion: str):
    """Valida la opción del submenu que tiene MODIFICAR"""
    
    if len(opcion) == 1 and "0" <= opcion <= "4":
        return True
    else:
        return False 

        
def validar_rango_nota(nota: float):
    """Comprueba que la nota esté entre 1 y 10 inclusive."""

    valido = True

    if nota < 1 or nota > 10:
        valido = False

    return valido


def validar_texto(texto: str):
    return texto.strip() != ""







