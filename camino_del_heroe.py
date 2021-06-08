from random import randint
import sys 
cantidad_oro = randint(0,100)
inventario = []
vida_heroe = randint(50,100)
guantes_daño = 1
daga_daño = 5
espada_daño = 10

precio_guantes = randint(1,20)
precio_daga = randint(30,40)
precio_espada = randint(70,90)
def camino1(nombre):
    print(nombre + " decidiste tomar el Camino 1... Sabia eleccion. Aunque lamentablemente la última")
    print("Te come una manada de lobos salvajes.")

def camino2(nombre, cantidad_oro):
    oro_recibido = randint(1,50)
    print(nombre + " decidiste tomar el Camino 2... Sabia eleccion. Te encuentras " + str(oro_recibido) + " monedas de oro en el piso.")
    cantidad_oro = cantidad_oro + oro_recibido
    print("Ahora tenés " + str(cantidad_oro) + " de oro.")
    return cantidad_oro

def tienda(nombre, cantidad_oro, inventario):
    print("Bienvenido a la tienda " + nombre +  "! Tenemos los siguientes objetos:")
    print("Guantes:" + str(precio_guantes))
    print("Daga:" + str(precio_daga))
    print("Espada:" + str(precio_espada))
    print("Que quieres llevar?")
    compra = input()
    if compra == "Guantes":
        if cantidad_oro - precio_guantes < 0:
            print("No te alcanza!")
            print("El tipo de la tienda te mata por intentar comprar algo que no te alcanza.")
            sys.exit()
        print("Muy buena eleccion.")
        cantidad_oro = cantidad_oro - precio_guantes
        print("Ahora tienes " + str(cantidad_oro) + " monedas de oro.")
        inventario.append("Guantes")
        print("Tienes los siguientes objetos en el inventario:")
        print(inventario)
        arma_heroe = 1
        return arma_heroe
    elif compra == "Daga":
        if cantidad_oro - precio_daga < 0:
            print("No te alcanza")
            print("El tipo de la tienda te mata por intentar comprar algo que no te alcanza.")
            sys.exit()
        print("Muy buena eleccion.")
        cantidad_oro = cantidad_oro - precio_daga
        print("Ahora tienes " + str(cantidad_oro) + " monedas de oro.")
        inventario.append("Daga")
        print("Tienes los siguientes objetos en el inventario:")
        print(inventario)
        arma_heroe = 5
        return arma_heroe
    if compra == "Espada":
        if cantidad_oro - precio_espada < 0:
            print("No te alcanza")
            print("El tipo de la tienda te mata por intentar comprar algo que no te alcanza.")
            print("Game over.")
            sys.exit()
        print("Muy buena eleccion.")
        cantidad_oro = cantidad_oro - precio_espada
        print("Ahora tienes " + str(cantidad_oro) + " monedas de oro.")
        inventario.append("Espada")
        print("Tienes los siguientes objetos en el inventario:")
        print(inventario)
        arma_heroe = espada_daño
        return arma_heroe

def orco(nombre, cantidad_oro, inventario, arma_heroe, vida_heroe):
    print("Te encontraste con un orco, que desafortunado, " + nombre + ".")
    daño_orco = randint(1,10)
    vida_orco = randint(30,50)
    print("Cada golpe de este orco hace " + str(daño_orco) + " de daño. Además, tiene " + str(vida_orco) + " puntos de vida." )
    print("Afortunadamente, traes contigo tu " + str(inventario) + " y tienes " + str(vida_heroe) + " puntos de vida.")
    while vida_heroe > 0 and vida_orco > 0:
        print("Quieres golpear al orco o huir? (Pelear/Huir)")
        respuesta_orco = input()
        if respuesta_orco == "Pelear":
            vida_orco = vida_orco - arma_heroe
            vida_heroe = vida_heroe - daño_orco
            print("Sos más rápido que el orco, asi que pegas primero, causandole " + str(arma_heroe)+ " de daño, dejandalo con " + str(vida_orco) + " de vida.")
            print("El orco te pega con sus puños, causandote " + str(daño_orco) + " de daño, y dejandote con " + str(vida_heroe) + " de vida.")
    if vida_heroe < 0:
        print("Te mató el orco, fallaste")
        sys.exit()
    elif vida_orco < 0:
        print("Mataste al orco, bien ahí")
        monedas_orco = randint(1,50)
        print("El orco tenía " + str(monedas_orco) + " monedas, las cuales te llevas")
        cantidad_oro += monedas_orco
        print("Ahora tenes " + str(cantidad_oro) + " monedas.")


def cura(nombre, vida_heroe, cantidad_oro):
    cantidad_vida_cura = randint(15,50)
    print("Te encontraste con un amigable cura")
    print("Te ofrece curarte " +  str(cantidad_vida_cura) + " puntos de vida por " + str(cantidad_vida_cura) + " monedas de oro." )
    print("Tienes " + str(vida_heroe) + " puntos de vida y " + str(cantidad_oro) + " monedas de oro. Quieres curarte? (si/no)")
    respuesta_cura = input()
    if respuesta_cura == "si":
        print("El cura, utilizando sus poderes arcanos, te cura")
        cantidad_oro = cantidad_oro - cantidad_vida_cura
        vida_heroe += cantidad_vida_cura
        print("Ahora tenés " + str(cantidad_oro) +" monedas de oro y " + str(vida_heroe) + " puntos de vida.")
    else:
        print("El cura es bastante caprichoso, y no va a aceptar un no como respuesta.")
        print("El cura te roba 10 monedas usando su magia, y te saca la lengua (no literalmente) :P")
        cantidad_oro = cantidad_oro - 10
        print("Ahora tenés " + str(cantidad_oro) + " monedas de oro.")

while True:
    while True:
        jugar_o_no = input("Querés jugar al camino del heroe? si/no ")
        if jugar_o_no == "si":
            print("Excelente. Empiezas con " + str(cantidad_oro) + " de oro y " + str(vida_heroe) + " puntos de vida.")
            if cantidad_oro > 50:
                print("Naciste adinerado, aparentemente. Felicidades")
            elif cantidad_oro < 50:
                print("Aparentemente naciste en latinoamerica.")
            print("Ahora tienes que tomar un camino, mi joven, pero primero, como te llamas?")
            nombre = str(input())
            print("Oh, hermoso nombre " + nombre + ". Ahora, quieres ir por el primer camino o por el segundo? 1/2")
            eleccioncamino = input()
            if eleccioncamino == str(1):
                camino1(nombre)
                print("F")
            elif eleccioncamino == str(2):
                cantidad_oro = camino2(nombre, cantidad_oro)
                print("Con el dinero que ahora posees podés visitar a la tienda")
                arma_heroe = tienda(nombre, cantidad_oro, inventario)
                print("Luego de comprar tu arma en la tienda, sigues por tu camino, determinado.")
                orco(nombre, cantidad_oro, inventario, arma_heroe, vida_heroe)
                print("Luego de semejante batalla, te encuentras agotado.")
                cura(nombre, vida_heroe, cantidad_oro)
        elif jugar_o_no == "no":
            print("Por las barbas de Merlin, que maleducad@!")
            break
        break
    break

# by chancho
# test
