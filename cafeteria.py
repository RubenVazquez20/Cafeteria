import re

def agregar_nueva_bebida(drink):

    
    drinkInfo = drink.replace(" ", "").split(",")
    size = [int(ze) for ze in drinkInfo[1:] if ze.isdigit()]
    name = drinkInfo[0]

    #Taste Cases 
    #item name is less than 2
    if len(name) < 2:
        return "El nombre de la bebida debe contar con al menos 2 caracteres"
    
    elif len(name) > 15:
        return "El nombre de la bebida debe contar con maximo 15 caracteres"
    
    elif len(name) == 1:
        return "El nombre de la bebida no puede contar con solo 1 caracter"
    
    #item name isn't alphabethic
    elif name.isalpha() == False:
        return "El nombre solo debe contener caracteres alfabeticos"

    #Size value is less than 1
    elif len(size) < 1:
        return "El tamaño de la bebida debe ser mayor a 1"
    
    elif len(size) > 48:
        return "El tamaño de la bebida debe ser menor a 48"
    
    elif type(size) == float:
        return "Los tamaños no pueden ser decimales"
    
    elif type(size) == chr:
        return "Los tamaños no pueden ser caracteres"

    #Size values entered in nonascending order
    elif size != sorted(size):
        return "Los tamaños deben ser ascendentes"
    
    elif len(size) == 0:
        return "Se necesita al menos 1 tamaño de la bebida" 
    
    elif len(size) > 5:
        return "Solo se admiten 5 tamaños por bebida"
    
    #When the drink name isn't in the correct place
    for ze in size: 
        if type(ze) != int and len(ze) >= 2:
            return "El nombre del producto debe estar al inicio"
    
    blankSpaces = drink.split(",")
    for item in blankSpaces:
        if item == " ":
            return "Los espacios en blanco seran ignorados"

    else:
        return "Se agrego la bebida"
        #print("Se agregó la bebida {} con los tamaños {}.".format(nombre, tamanos))