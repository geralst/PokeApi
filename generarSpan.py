def genera_span(lista): #lista que recibira de 2,3 o 5
    diccionario_es = {
                    'normal':'Normal', 'fighting':'Lucha', 'flying':'Volador', 'poison':'Veneno',
                    'ground':'Tierra', 'rock':'Roca', 'bug':'Bicho', 'ghost':'Fantasma',
                    'steel':'Acero', 'fire':'Fuego', 'water':'Agua', 'grass':'Planta', 
                    'electric':'Eléctrico', 'psychic':'Psíquico', 'ice':'Hielo', 'dragon':'Dragón',
                    'dark':'Siniestro', 'fairy':'Hada', 'baby':'Bebé', 'legendary':'Legendario',
                    'mythical':'Mítico'}
    
    span_str = ""
    for item in lista:
        item_es = diccionario_es[item]
        span_str = span_str + f'<span class="label {item}">{item_es}</span>'

    return span_str