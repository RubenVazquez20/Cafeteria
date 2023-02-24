def agregar_nueva_bebida(bebida_str):

    bebida_info = bebida_str.replace(" ", "").split(",")
    nombre = bebida_info[0]
    tamanos = [int(tam) for tam in bebida_info[1:] if tam.isdigit()]

    if len(nombre) < 2 or len(nombre) > 15:
        return "El nombre de la bebida debe tener entre 2 y 15 caracteres."

    elif len(tamanos) == 0:
        return "Debe ingresar al menos un tamaño para la bebida."

    elif any(tam < 1 or tam > 48 for tam in tamanos):
        return "El tamaño de la bebida debe estar en el rango de 1 a 48."

    elif tamanos != sorted(tamanos):
        return "Los tamaños deben ser ingresados en orden ascendente."

    else:
        # Agregar la nueva bebida a la base de datos o al menú
        # con el nombre y los tamaños especificados.
        return "Se agrego el producto"
        #print("Se agregó la bebida {} con los tamaños {}.".format(nombre, tamanos))
