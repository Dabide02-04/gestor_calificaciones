from src.calificaciones import calcular_promedio
def test_calcular_promedio_de_tres_notas():
    resultado = calcular_promedio([4.0,3.0, 5.0])
    assert resultado == 4.0