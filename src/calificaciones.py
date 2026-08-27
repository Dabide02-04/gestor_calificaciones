def calcular_promedio(calificaciones):
    if len(calificaciones) == 0:
        raise ValueError("La lista no puede estar vacía")

    for nota in calificaciones:
        if nota < 0.0 or nota > 5.0:
            raise ValueError("Calificación fuera de rango")

    return sum(calificaciones) / len(calificaciones)
def determinar_estado(calificaciones):
    promedio = calcular_promedio(calificaciones)

    if promedio >= 3.0:
        return "Aprobado"
    else:
        return "Reprobado"
def obtener_nota_mayor(calificaciones):
    if len(calificaciones) == 0:
        raise ValueError("La lista no puede estar vacía")

    return max(calificaciones)


def obtener_nota_menor(calificaciones):
    if len(calificaciones) == 0:
        raise ValueError("La lista no puede estar vacía")

    return min(calificaciones)