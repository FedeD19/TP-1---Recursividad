def usar_la_fuerza(mochila, indice=0, intentos=0):
    #Caso base 1: la mochila está vacía (no quedan más objetos)
    if indice >= len(mochila):
        print("La mochila está vacía.")
        return False, intentos

    #Sacar el objeto actual
    objeto = mochila[indice]
    intentos += 1
    print(f"[{intentos}] El Jedi saca: {objeto}")

    #Caso base 2: se encontró el sable de luz
    if objeto.lower() == "sable de luz":
        print(f"El Jedi encontró el sable de luz. Lo usó después de sacar {intentos} objeto(s).")
        return True, intentos

    #Caso recursivo: seguir buscando con el siguiente objeto
    return usar_la_fuerza(mochila, indice+1, intentos)


def analizar_mochila(mochila):    
    if not mochila:
        print("La mochila está vacía desde el principio.")
        return

    print(f"Contenido original de la mochila: {mochila}")
    print(f"Total de objetos: {len(mochila)}")
    print("Buscando el sable de luz")

    encontrado, intentos = usar_la_fuerza(mochila)

    if encontrado:
        print(f"¿Contiene sable de luz? SÍ")
        print(f"Objetos sacados para encontrarlo: {intentos}")
    else:
        print(f"¿Contiene sable de luz? NO")
        print(f"Objetos revisados (total): {intentos}")


#Casos de prueba
#Caso 1: el sable está en el medio
mochila_luke = [
    "comlink",
    "raciones",
    "sable de luz",
    "capa",
       "holocrón",
]
analizar_mochila(mochila_luke)
print()

#Caso 2: el sable está al final
mochila_obi_wan = [
    "binoculares",
    "medpac",
    "mapa estelar",
    "sable de luz",
]
analizar_mochila(mochila_obi_wan)
print()

#Caso 3: no hay sable de luz
mochila_rey = [
    "bastón",
    "gafas",
    "comida de raciones",
    "cuerda",
]
analizar_mochila(mochila_rey)
print()

#Caso 4: mochila vacía
mochila_vacia = []
analizar_mochila(mochila_vacia)
