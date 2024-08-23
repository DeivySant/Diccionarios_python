asignaturas = {
    "matematicas" : 6,
    "fisica" : 4,
    "quimica" : 5
    }
creditos = 0
for key, value in asignaturas.items():
    print(f"La asignatura {key} tiene {value} creditos ")
    creditos = creditos + value
    
print(f"La suma de los creditos es {creditos}")