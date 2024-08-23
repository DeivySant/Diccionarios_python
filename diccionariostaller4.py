usuarios = {
    "123456789": {
        "Nombre" : "John",
        "Apellido" : "Ascuntar",
        "Direccion": "Catambuco",
        "Telefono" : "3187024676",
        "Placas" : ["ABC123" ,"ACB432", "ACC443"]
        },

    "987654321": {
        "Nombre" : "Maria",
        "Apellido" : "Daza",
        "Direccion": "La merced",
        "Telefono " : "3162887010",
        "Placas" : ["LMN789","OPQ012"]
        },

    "123456798": {
        "Nombre" :"Santiago",
        "Apellido" : "Ascuntar",
        "Direccion":"La merced",
        "Telefono" : "3007536544",
        "Placas" : ["PSA223","HJJ173","ACC443"]
    }
}
#------------------------------------------------------------------------------------------------------------------------
#Verifique si una placa esta asociada a mas de un usuario, a un único usuario o a 
#ningún usuario
def verificarplaca (placaverificar,usuarios):
    contador = 0
    for key,datosusuarios in usuarios.items():
        if placaverificar in datosusuarios["Placas"]:
            contador +=1
    print(f"La placa {placaverificar} se asocia a {contador} usuarios.")
    return

#------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------
#Permita hacer un cambio de placa de un usuario a otro, debe verificar que ambos 
#usuarios existen y que además la placa esta asociada al usuario propietario
def cambiarplaca(codigopro,codigorec,placacambio,usuarios):
    if (codigopro and codigorec) in usuarios:
        propietario = usuarios[codigopro]
        if placacambio in propietario["Placas"]:
            receptor = usuarios[codigorec]
            receptor["Placas"].append(placacambio)
            propietario["Placas"].remove(placacambio)
            print(f"Se realizo un cambio del placa {placacambio} del propietario con codigo {codigopro} a el usuario con codigo{codigorec}.")
            print(f"Las nuevas placas para el usuario receptor son : {receptor.get('Placas')}")
        else:
            print(f"La placa {placacambio} no existe para el codigo {codigopro}")

#------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------
#Actualice la dirección y teléfono de un usuario
def actualizar(codigo4,usuarios):
    if codigo4 in usuarios:
        usuario = usuarios[codigo4]
        print(f"Se tiene ; Nombre : {usuario.get('Nombre')} y direccion : {usuario.get('Direccion')}")
        usuario["Nombre"] = "Dievy Ascuntar"
        usuario["Direccion"] = "Catambuco la merced"
    else:
        print(f"El codigo {codigo4} no se encontro en el almacenamiento")
    print(f"Se actualizo la informacion ; Nombre : {usuario.get('Nombre')} y direccion : {usuario.get('Direccion')}")
#------------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------------
#Elimine una placa de un vehículo, en caso de que esta no esté asociada a ese 
#usuario, envíe un mensaje informando la situación
def eliminarplaca(placa2,codigo3,usuarios):
    if codigo3 in usuarios:
        usuario = usuarios[codigo3]
        if placa2 in usuario["Placas"]:
            usuario["Placas"].remove(placa2)
            print(f"La placas que quedan para el usuario {codigo3} son : {usuario.get('Placas')}")
        else:
            print(f"La placa : {placa2} no pertenece a este usuario")
#------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------
#Adicione una placa a un usuario determinado y al final muestre la lista de vehículos
#de ese usuario
def adicionarplaca(placa,codigo2,usuarios):
    if codigo2 in usuarios:
        usuario = usuarios[codigo2]
        usuario["Placas"].append(placa)
        print(f"Las placas que contiene el usuario {codigo2} son : {usuario.get('Placas')}")
#------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------
#Dada una placa revise en el diccionario si existe un propietario para la misma, y 
#muestre en pantalla la información de ese propietario
def buscarplaca(placa0,usuarios):
    for key,datosusuarios in usuarios.items():
        if placa0 in datosusuarios["Placas"]:
            print(f"La placa {placa0} pertenece a : {key} El nombre del propiertario es {datosusuarios.get('Nombre')} ")
            return
#------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------
#Dado un numero de documento muestre cuantos vehículos están asociados a ese 
#usuario, junto con sus placas
def placasusuario(codigo1,usuarios):
    if codigo1 in usuarios:
        usuario = usuarios[codigo1]
        contadorplaca = len(usuario["Placas"])
        print(f"El usuario {codigo1} tiene {contadorplaca} placas que son : {usuario['Placas']}")
    else:
        print(f"No se encotro el documento {codigo1}")
    return
#------------------------------------------------------------------------------------------------------------------------

placa1 = "HHH666" #Placa que sera adicionada
codigo2 = "987654321" #Codigo al cual se le adicionara la placa

placa0 = "PSA223" #Placa que sera buscada

codigo1 = "123456798" #Codigo para ver placas asociadas

codigo3 = "987654321" #Codigo de usuario que se eliminara una placa
placa2 = "OPQ012"#Placa a eliminar del usuario codigo3

codigo4 = "123456798" #Codigo de quien se actualizara los datos

placacambio = "ABC123" #Placa que sera cambiada de usuario
codigopro = "123456789" # Codigo del propietario de la placa
codigorec = "987654321" #Codigo del receptor de la placa

placaverificar = "ACC443" #Esta es la placa que se verificara cuantas veces esta en los usuarios

verificarplaca(placaverificar,usuarios)
cambiarplaca(codigopro,codigorec,placacambio,usuarios)
actualizar(codigo4,usuarios)
eliminarplaca(placa2,codigo3,usuarios)
adicionarplaca(placa1,codigo2,usuarios)
placasusuario(codigo1,usuarios)
buscarplaca(placa0,usuarios)