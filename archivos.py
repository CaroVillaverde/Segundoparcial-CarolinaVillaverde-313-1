import json


def cargar_alumno():
    
    with open("alumnos.json", "r", encoding="utf-8") as archivo: 
        alumno = json.load(archivo)
    
    return alumno

def guardar_alumno(alumno):
    
    with open("alumnos.json", "w", encoding="utf-8") as archivo:
        json.dump(alumno, archivo, indent=4)