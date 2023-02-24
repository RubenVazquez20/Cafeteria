from cafeteria import *

def test_formatoCorrecto():
    assert agregar_nueva_bebida("Paopao,4,5,6,7,8") == "Se agrego el producto"

def test_formatoCorrecto1Tamano():
    assert agregar_nueva_bebida("Paopao,4") == "Se agrego el producto"

def test_03():
    assert agregar_nueva_bebida("Paopao,0,4,8,11") == "El tamaño de la bebida debe estar en el rango de 1 a 48."