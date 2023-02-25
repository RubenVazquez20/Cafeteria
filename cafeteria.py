import re

def agregar_nueva_bebida(drink):

    
    drinkInfo = drink.replace(" ", "").split(",")
    size = drinkInfo[1:]
    name = drinkInfo[0]

    #Taste Cases 
    #item name is less than 2
    if len(name) < 2:
        return "El nombre de la bebida debe contar con al menos 2 caracteres"
    
    if len(name) > 15:
        return "El nombre de la bebida debe contar con maximo 15 caracteres"
    
    if len(name) == 1:
        return "El nombre de la bebida debe contar con al menos 2 caracteres"
    
    #item name isn't alphabethic
    if name.isalpha() == False:
        return "El nombre solo debe contener caracteres alfabeticos"
         
    if type(size) == chr:
        return "Los tamaños no pueden ser caracteres"

    if len(size) == 0:
        return "Se necesita al menos 1 tamaño de la bebida" 
    
    if len(size) > 5:
        return "Solo se admiten 5 tamaños por bebida"
        #Size value is less than 1

    for ze in size:
        if int(ze) < 1:
            return "El tamaño de la bebida debe ser mayor a 1"
    
    for ze in size:
        if int(ze) > 48:
            return "El tamaño de la bebida debe ser menor a 48"
        
    for ze in size:
        if type(ze) == float:
            return "Los tamaños no pueden ser decimales"
        
    #When the drink name isn't in the correct place
    for ze in size: 
        if type(ze) != int and len(ze) >= 2:
            return "El nombre del producto debe estar al inicio"
    
    blankSpaces = drink.split(",")
    for item in blankSpaces:
        if item == " ":
            return "Los espacios en blanco seran ignorados"
        
        #Size values entered in nonascending order
    if size != sorted(size):
        return "Los tamaños deben ser ascendentes"

    else:
        return "Se agrego la bebida"
        #print("Se agregó la beit commiida {} con los tamaños {}.".format(nombre, tamanos))