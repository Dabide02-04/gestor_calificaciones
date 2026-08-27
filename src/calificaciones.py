def calcular_promedio(calificaciones):
    if len(calificaciones) == 0:
        raise ValueError("La lista no puede estar vacía")

    for nota in calificaciones:
        if nota < 0.0 or nota > 5.0:
            raise ValueError("Calificación fuera de rango")

    return sum(calificaciones) / len(calificaciones)