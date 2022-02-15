from xml.dom.minidom import Document
from string import Template
from entrada import validacion
from solicitudes import obtenerId, obtenerImg, obtenerPreEvol, obtenerStats, obtenerTipo, obtenerDescripcion, obtenerTipoEspecial, procesa_tipos
from generarSpan import genera_span

#Validacion del nombre
nombre = input('Introduzca el nombre del Pokémon a procesar, si el pokémon tiene espacios reemplace por "-" : ')
pok_nombre = validacion(nombre) #El nombre lo entrega en mayuscula!!! no usarlo como parametro

#Obtener los datos del pokemon atraves del nombre
pok_id = obtenerId(nombre)

#Obtener imagen del pokemon por id
pok_img = obtenerImg(nombre)

#Obtencion de las pre evoluciones
pok_preEtapa = obtenerPreEvol(nombre)

#Obtencion de los stats
pok_stats = obtenerStats(nombre)
pok_hp, pok_atk, pok_def, pok_psa, pok_psd, pok_vel = pok_stats #asigna cada variable en obtenida del recorrido de la lista en el siguiente orden.

#Obtener tipo de pokemon
pok_tipos = genera_span(obtenerTipo(nombre))
pok_tipo_esp = genera_span(obtenerTipoEspecial(nombre))
#Obtener descripcion de pokemon
pok_comentario = obtenerDescripcion(nombre)

#Obtener caracterisitacas de tipo
lista_tipos = obtenerTipo(nombre)

# 1. Generar lista super efectivo contra ==> double_damage_to
    # lista_sec = datos_type["damage_relations"]["double_damage_to"]
    # recorrer lista sub name 
tipos_sec = genera_span(procesa_tipos(lista_tipos,"double_damage_to"))

# 2. generar lista debil contra ==> double_damage_from
tipos_dc = genera_span(procesa_tipos(lista_tipos,"double_damage_from"))

# 3. generar lista resistente contra ==> half_damage_from
tipos_rc = genera_span(procesa_tipos(lista_tipos,"double_damage_from"))

# 4. generar lista poco eficaz contra ==> half_damage_to
tipos_pec = genera_span(procesa_tipos(lista_tipos,"half_damage_to"))

# 5. generar lista inmune contra ==> no_damage_from
tipos_inmune = genera_span(procesa_tipos(lista_tipos,"no_damage_from"))

# 6. generar lista ineficaz contra ==> no_damage_to
tipos_ineficaz = genera_span(procesa_tipos(lista_tipos,"no_damage_to"))

# luego enviar cada una de las litas anteriores a la funcion genera span
# asignar el resultado respectivo a la variable correspondiente e n el archivo base.html
# Ejm: para super efectivo contra, la variable correspondiente es $span_sup_ef


#Generar el html con los datos obtenidos de la api

#llamado al html base para ser sobrescrito
with open('base.html','r') as infile:
    entrada = infile.read()

#creo objeto template con las variables recibidas de la api
base_html = Template(entrada)

#reemplazo los valores de este template con substitute
#orden variable html = variable python
salida_html = base_html.substitute(
    pok_id = pok_id, pok_nombre = pok_nombre, pok_img = pok_img,
    pok_preEtapa = pok_preEtapa, pok_hp = pok_hp, pok_atk = pok_atk,
    pok_def = pok_def, pok_psa = pok_psa, pok_psd = pok_psd,
    pok_vel = pok_vel, pok_tipos = pok_tipos, pok_tipo_esp = pok_tipo_esp, pok_comentario = pok_comentario,
    tipos_sec = tipos_sec, tipos_dc = tipos_dc, tipos_rc = tipos_rc,
    tipos_pec = tipos_pec, tipos_inmune = tipos_inmune, tipos_ineficaz = tipos_ineficaz)

with open('salida.html', 'w') as outfile:
     outfile.write(salida_html)
