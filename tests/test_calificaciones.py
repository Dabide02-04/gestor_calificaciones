from src.calificaciones import calcular_promedio, determinar_estado, obtener_nota_mayor, obtener_nota_menor
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
def test_determinar_estado_aprobado():
    resultado = determinar_estado([3.0, 3.0, 3.0])
    assert resultado == "Aprobado"


def test_determinar_estado_reprobado():
    resultado = determinar_estado([2.0, 3.0, 2.0])
    assert resultado == "Reprobado"
    
def test_obtener_nota_mayor():
    resultado = obtener_nota_mayor([4.0, 3.0, 5.0, 3.5])
    assert resultado == 5.0


def test_obtener_nota_menor():
    resultado = obtener_nota_menor([4.0, 3.0, 5.0, 3.5])
    assert resultado == 3.0

def test_obtener_nota_mayor_lista_vacia():
    with pytest.raises(ValueError):
        obtener_nota_mayor([])


def test_obtener_nota_menor_lista_vacia():
    with pytest.raises(ValueError):
        obtener_nota_menor([])