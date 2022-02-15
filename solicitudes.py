import random
from generarSpan import genera_span 
from get_module import get_info

#Obtener id del pokemon atraves del nombre
def obtenerId(pok_nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{pok_nombre}"
    datos_base = get_info(url)
    pok_id = datos_base["id"]
    return pok_id

#Obtener img del pokemon atraves del nombre
def obtenerImg(pok_nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{pok_nombre}"
    datos_base = get_info(url)
    pok_img = datos_base['sprites']['front_default']
    return pok_img


# Obtencion de las pre evoluciones
def obtenerPreEvol(pok_nombre):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pok_nombre}"
    datos_base = get_info(url)
    #pregunto si esta nulo o no
    if datos_base["evolves_from_species"] is None:
        pok_etapa = ""
    else:
    #le pido a la api que me entrege el objeto evolucion y me de el atributo name
        evolves_from = datos_base["evolves_from_species"]["name"]
        pok_etapa = f"Etapa Previa: {evolves_from.capitalize()}" #coloco que la respuesta tenga la primera letra sea mayuscula
    return pok_etapa

#Obtencion de los stats
def obtenerStats(pok_nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{pok_nombre}"
    datos_base = get_info(url)
    stats = [] #lista vacia para guardar los valores del stat
    for item in datos_base["stats"]:
        stats.append(item["base_stat"]) #guardo en la lista vacia cada valor obtenido base_stat del recorrido
    return stats

#Obtencion de los Type
def obtenerTipo(pok_nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{pok_nombre}"
    datos_base = get_info(url)
    tipos_lista = datos_base["types"]
    tipos = []
    for item in tipos_lista:
        tipos.append(item["type"]["name"])
    return tipos

#Obtener tipo especial
def obtenerTipoEspecial(pok_nombre):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pok_nombre}"
    datos_base = get_info(url)
    tipo_especial = []
    if datos_base['is_baby'] == True:
            tipo_especial.append('baby')
    elif datos_base['is_legendary'] == True:
            tipo_especial.append('legendary')
    elif datos_base['is_mythical'] == True:
            tipo_especial.append('mythical')
    return tipo_especial


#Obtener caracteristicas type
def procesa_tipos(lista_tipos, caracteristica):
    tipos_total = []
    for type in lista_tipos:
        url = f"https://pokeapi.co/api/v2/type/{type}"
        datos_type = get_info(url)
        lista_sec = datos_type["damage_relations"][caracteristica]
        
        for item in lista_sec:
            tipos_total.append(item["name"])
    
    tipos_total_filtrado = set(tipos_total) #elimina los datos repetidos
    tipos_total = list(tipos_total_filtrado) #enlista los datos ya filtrados
    tipos_total.sort()
    return tipos_total


#Obtencion de la descripcion
def obtenerDescripcion(pok_nombre):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pok_nombre}"
    datos_base = get_info(url)
    comentarios = datos_base["flavor_text_entries"]

    comentarios_es = []
    for item in comentarios:
        if item["language"]["name"] == "es":
            comentarios_es.append(item["flavor_text"].replace("\n"," "))
    pok_comentario = random.choice(comentarios_es)
    return pok_comentario








if __name__ == '__main__':
    #Obtener Id
        pok_nombre = "charizard"
        poke_id = obtenerId(pok_nombre)
        print(poke_id)
        
    #Obtener Imagen
        pok_nombre = "charizard"
        pok_img = obtenerImg(pok_nombre)
        print(pok_img)

    #Obtener pre evolucion
        pok_nombre = "charizard"
        pok_etapa = obtenerPreEvol(pok_nombre)
        print(pok_etapa)

    #Obtener stats
        pok_nombre = "charizard"
        stats = obtenerStats(pok_nombre)
        pok_hp, pok_atk, pok_def, pok_psa, pok_psd, pok_vel = stats
        print(stats)
        print(pok_hp)
           
    #Obtener type
        pok_nombre = "charizard"
        tipos = obtenerTipo(pok_nombre)
        print(tipos)

   #Obtener type special
        pok_nombre = "articuno"
        tipos = obtenerTipoEspecial(pok_nombre)
        print(tipos)

    #Obtener comentarios
        pok_nombre = "charizard"
        comentarios = obtenerDescripcion(pok_nombre)
        print(comentarios)

    #Obtener caracteristicas type
        pok_nombre = "charizard"
        tipos = obtenerTipo(pok_nombre)
        pok_sac = procesa_tipos(tipos,"double_damage_to")
        print(pok_sac)

    