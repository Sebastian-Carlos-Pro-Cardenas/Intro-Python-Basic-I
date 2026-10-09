"""
--------------------------- OPERADORES ---------------------------
En este taller aprenderás usar los diferentes tipos de operadores
"""

"""
--- Ejercicio 1 operadores aritméticos  ---
Reemplaza el ? con el operador según sea el caso
"""
num1: int = 10
num2: int = 5

print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2}")

"""
--- Ejercicio 2 operadores lógicos  ---
Reemplaza el ? con el operador según sea el caso
Puedes investigar sobre las tablas de la verdad, recuerda "las amigas de mis amigas, son mis amigas"
"""

michi_4_patas: bool = True
michi_3_ojos: bool = False
michi_vuela: bool = False
michi_interesado: bool = True
michi_juega: bool = True
michi_pone_huevos: bool = False

print(f"AND: {michi_4_patas and michi_3_ojos}")
print(f"OR: {michi_interesado or michi_vuela}")
print(f"NOT bool1: {not michi_juega}")
print(f"NOT bool2: {not michi_pone_huevos}")

"""
--- Ejercicio 3 Comparadores  ---
Reemplaza el ? con el comparador según sea el caso
"""

a: int = 7
b: int = 3

print(f"¿a es igual a b?: {a == b}")
print(f"¿a es diferente de b?: {a != b}")
print(f"¿a es mayor que b?: {a > b}")
print(f"¿a es menor que b?: {a < b}")
print(f"¿a es mayor o igual que b?: {a >= b}")
print(f"¿a es menor o igual que b?: {a <= b}")
