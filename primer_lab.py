# Solicita al usuario que ingrese su peso en kilogramos
peso = float(input("Ingresa tu peso en kilogramos: "))

# Solicita al usuario que ingrese su altura en metros
altura = float(input("Ingresa tu altura en metros: "))

# Calcula el IMC
imc = peso / (altura ** 2)

# Determina la categoría basada en el IMC calculado
if imc < 18.5:
    categoria = "Bajo peso"
elif imc < 25:
    categoria = "Peso normal"
elif imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

# Imprime el resultado
print(f"Tu IMC es {imc:.2f}, lo que corresponde a la categoría de '{categoria}'.")
