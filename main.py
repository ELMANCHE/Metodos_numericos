import math

def obtener_cifras_significativas(numero):
    if numero == 0:
        return 0
    elif numero < 1 and numero > 0:
        expo = math.floor(math.log10(numero))
        ope = numero / (10 ** expo)
        ope = round(ope * 1000) / 1000  # Redondear a 3 cifras significativas
        numero = ope * (10 ** expo)
    elif numero >= 1:
        expo = math.floor(math.log10(numero)) - 2
        ope = numero / (10 ** expo)
        ope = round(ope) / 100  # Redondear a 3 cifras significativas
        numero = ope * (10 ** expo)
    return numero

#pidiendo los datos al usuario
def main():
    print("Bienvenido:")
    valor_verdadero = float(input("Ingrese el valor verdadero: "))
    valor_aproximado = float(input("Ingrese el valor aproximado: "))

    error_verdadero = abs(valor_verdadero - valor_aproximado)
    error_relativo = error_verdadero / valor_verdadero
    error_relativo_porcentual = error_relativo * 100

    print("\nCalculos normales:")
    print(f"Error verdadero: {error_verdadero}")
    print(f"Error relativo: {error_relativo}")
    print(f"Error relativo porcentual: {error_relativo_porcentual} %")

    print("\nCon 3 cifras significativas:")
    print(f"Error verdadero: {obtener_cifras_significativas(error_verdadero):.9f}")
    print(f"Error relativo: {obtener_cifras_significativas(error_relativo):.9f}")
    print(f"Error relativo porcentual: {obtener_cifras_significativas(error_relativo_porcentual):.9f} %")

if __name__ == "__main__":
    main()

