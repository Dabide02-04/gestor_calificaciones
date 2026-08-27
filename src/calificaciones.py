def calcular_promedio(calificaciones):
    if len(calificaciones) == 0:
        raise ValueError("La lista no puede estar vacia")
    return sum(calificaciones ) / len(calificaciones)