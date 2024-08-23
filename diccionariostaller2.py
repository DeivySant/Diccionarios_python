frutas = {
    "platano" : 1.35,
    "manzana" : 0.80,
    "pera" : 0.85,
    "naranja": 0.70
    }

def calcular_precio(precio,cantidad):
    total = cantidad * precio
    return total

fruta = input("Dame una fruta : ").lower()
cantidad = float(input("Cuantos kilos son los de tu compra :"))
precio = frutas.get(fruta)

print(f"El valor de tu compra es {calcular_precio(precio,cantidad)}")