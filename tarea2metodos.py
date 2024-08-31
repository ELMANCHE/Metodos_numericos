#importacion ope mat
import math

# Valor real de e^(0.7)
e_0_7_real = math.exp(0.7)

# Tolerancia
tol = 0.0001

# Inicializar variables
n = 0
e_0_7_aprox = 0
error_verdadero_relativo = 100
error_iterativo_relativo = 100

while abs(error_iterativo_relativo) >= tol:
    # Calcular el término actual de la serie
    termino = (0.7**n) / math.factorial(n)
    
    # Actualizar la aproximación
    e_0_7_aprox += termino
    
    # Calcular el error verdadero relativo
    error_verdadero_relativo = abs((e_0_7_aprox - e_0_7_real) / e_0_7_real) * 100
    
    # Calcular el error iterativo relativo
    if n > 0:
        error_iterativo_relativo = abs((e_0_7_aprox - e_0_7_aprox_anterior) / e_0_7_aprox) * 100
    else:
        error_iterativo_relativo = 100
    
    # Actualizar la aproximación anterior
    e_0_7_aprox_anterior = e_0_7_aprox
    
    # Incrementar el índice
    n += 1

# Redondear el resultado a 4 cifras significativas
e_0_7_aprox = round(e_0_7_aprox, 4)

#Para imprimir
print(f"Valor aproximado de e^(0.7) con 4 cifras significativas: {e_0_7_aprox}")
print(f"Error verdadero relativo porcentual: {error_verdadero_relativo:.4f}%")
print(f"Error iterativo relativo porcentual: {error_iterativo_relativo:.4f}%")