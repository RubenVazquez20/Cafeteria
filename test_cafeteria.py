from cafeteria import *


def test_isNotAlphabetic():
    assert agregar_nueva_bebida("44,5,6,10") == "El nombre solo debe contener caracteres alfabeticos"

def test_nameLengthLessThan2():
    assert agregar_nueva_bebida("p,4,5,6,7,8") == "El nombre de la bebida debe contar con al menos 2 caracteres"

def test_nameLengthEqualTo1():
    assert agregar_nueva_bebida("p,4,8,12") == "El nombre de la bebida no puede contar con solo 1 caracter"

def test_nameLengthGreaterThan15():
    assert agregar_nueva_bebida("PaoPao de Mango y Cereza, 5,6,9,10") == "El nombre de la bebida debe contar con maximo 15 caracteres"

def test_sizeValueLessThan1():
    assert agregar_nueva_bebida("Pao Pao,0,1,7,9") == "El tamaño de la bebida debe ser mayor a 1"

def test_sizeValueGreaterThan48():
    assert agregar_nueva_bebida("PaoPao,4,8,49") == "El tamaño de la bebida debe ser menor a 48"

def test_sizeValueIsDecimal():
    assert agregar_nueva_bebida("Pao Pao, 5,10.5,40.3,48") == "Los tamaños no pueden ser decimales"

def test_sizeValueisNonnumeric():
    assert agregar_nueva_bebida("PaoPao, 4,g,9,23") == "Los tamaños no pueden ser caracteres"

def test_sizeValuesNonascendingOrder():
    assert agregar_nueva_bebida("PaoPao, 2,6,4,8,3") == "Los tamaños deben ser ascendentes"

def test_NotSizeValuesEntered():
    assert agregar_nueva_bebida("PaoPao") == "Se necesita al menos 1 tamaño de la bebida" 

def test_MoreThan5SizeValues():
    assert agregar_nueva_bebida("PaoPao,3,4,5,6,7,8,9,12") == "Solo se admiten 5 tamaños por bebida"

def test_itemNameIsNotFirst():
    assert agregar_nueva_bebida("5,6,8,PaoPao,9") == "El nombre del producto debe estar al inicio"

def test_itemContainBlankSpaces():
    assert agregar_nueva_bebida("PaoPao, ,6,9") == "Los espacios en blanco seran ignorados"

#When all the carcateristics are ok
def test_formatoCorrecto():
    assert agregar_nueva_bebida("Pao pao,4,5,6,7,8") == "Se agrego la bebida"
