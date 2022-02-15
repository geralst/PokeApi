from poke_validation import validate
import data
#Validacion del nombre
def validacion(nombre):
    nombre = validate(nombre)
    return nombre.capitalize()

if __name__ == '__main__':
    pok_nombre = validacion()
    print(pok_nombre)