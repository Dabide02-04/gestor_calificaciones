from src.calificaciones import calcular_promedio
import pytest
def test_calcular_promedio_de_tres_notas():
    resultado = calcular_promedio([4.0,3.0, 5.0])
    assert resultado == 4.0
def test_calcular_promedio_lista_vacia():
    with pytest.raises(ValueError):
        calcular_promedio([])
def test_calificaciones_no_pueden_ser_menores_a_cero():
    with pytest.raises(ValueError):
        calcular_promedio([-1.0, 3.0])

def test_calificaciones_no_pueden_ser_mayores_a_cinco():
    with pytest.raises(ValueError):
        calcular_promedio([4.0, 5.5])

def test_valores_limite_son_validos():
    resultado = calcular_promedio([0.0, 5.0])
    assert resultado == 2.5