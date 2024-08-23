dic_datos = {
    "Nombre" : input("Dame tu nombre : "),
    "Edad" : input("Introduce tu edad : "),
    "Direccion" : input("Dame tu direccion : "),
    "Telefono" : input ("Telfono : ")
    }

print(f"Tu nombre es {dic_datos.get('Nombre')} tienes {dic_datos.get('Edad')}, vives en {dic_datos.get('Direccion')} y tu numero de telefono es {dic_datos.get('Telefono')}")