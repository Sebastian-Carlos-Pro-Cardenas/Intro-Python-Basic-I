"""
--------------------------- CICLOS Y ESTRUCTURAS DE CONTROL ---------------------------
En este taller aprenderás usar los métodos más típicos para dirigir el flujo de ejecuón y la lógica de un algoritmo
"""

"""
--- Ejercicio 1 condicionales  ---
Escribe un programa que pida al usuario una letra y luego imprima un mensaje indicando si es una vocal o una consonante.
"""

input_char: str = input("Ingresa una letra: ").strip().lower()

if len(input_char) == 1 and input_char.isalpha():
    vowels: str = "aeiouáéíóú"
    if input_char in vowels:
        print(f"La letra '{input_char}' es una vocal.")
    else:
        print(f"La letra '{input_char}' es una consonante.")
else:
    print("Entrada no válida. Por favor, ingresa una sola letra del alfabeto.")

"""
--- Ejercicio 2  condicionales anidados  ---
Escribe un programa que pida al usuario una nota (entre 0 y 100) y determine si 
es una calificación de "A", "B", "C", "D" o "F".
"""

raw_score_input: str = input("\nIngresa tu nota (0 - 100): ")

if raw_score_input.isdigit():
    numeric_score: int = int(raw_score_input)
    if 0 <= numeric_score <= 100:
        if numeric_score >= 90:
            letter_grade: str = "A"
        elif numeric_score >= 80:
            letter_grade: str = "B"
        elif numeric_score >= 70:
            letter_grade: str = "C"
        elif numeric_score >= 60:
            letter_grade: str = "D"
        else:
            letter_grade: str = "F"
        print(f"Calificación numérica: {numeric_score} -> Nota: {letter_grade}")
    else:
        print("Error: La nota debe estar en el rango de 0 a 100.")
else:
    print("Error: Ingresa un número entero válido.")

"""
--- Ejercicio 3  bucle while  ---
Escribe un programa que pida al usuario un número entero positivo y 
luego imprima la cuenta regresiva desde ese número hasta 1.
"""

countdown_start: int = int(input("\nIngresa un número entero positivo para la cuenta regresiva: "))

if countdown_start > 0:
    current_counter: int = countdown_start
    print(f"Iniciando cuenta regresiva desde {countdown_start}:")
    while current_counter >= 1:
        print(current_counter, end=" " if current_counter > 1 else "\n")
        current_counter -= 1
else:
    print("Por favor, ingresa un número mayor a 0.")

"""
--- Ejercicio 4  bucle for  ---
Escribe un programa que imprima todos los caracteres de una cadena de texto ingresada por el usuario.
"""

user_text_input: str = input("\nIngresa una cadena de texto: ")

print("Desglosando caracteres:")
for single_character in user_text_input:
    print(f"  Character: '{single_character}'")

"""
--- Ejercicio 5  bucle for con range ---
Escribe un programa que imprima la tabla de multiplicar del 5 (del 1 al 10).
"""

multiplier_base: int = 5
print(f"\nTabla de multiplicar del {multiplier_base}:")

for factor_step in range(1, 11):
    product_result: int = multiplier_base * factor_step
    print(f"  {multiplier_base} x {factor_step:2d} = {product_result}")

"""
--- Ejercicio 6  bucle for con listas ---
Escribe un programa que pida al usuario 5 palabras, las guarde en una lista y 
luego en una nueva lista guarde todas las palabras en mayúsculas.
"""

raw_word_list: list[str] = []
print("\nPor favor ingresa 5 palabras:")

for index_step in range(1, 6):
    word_entry: str = input(f"  Palabra {index_step}: ").strip()
    raw_word_list.append(word_entry)

# Transforming words into uppercase using list iteration
uppercase_word_list: list[str] = []
for word_item in raw_word_list:
    uppercase_word_list.append(word_item.upper())

print(f"Lista de palabras en mayúsculas: {uppercase_word_list}")

"""
--- Ejercicio 7  break and continue ---
Escribe un programa que le pida al usuario una mascota y 
si es un perro, que imprima en la consola "Tengo un perro", 
si es un gato, que imprima en la consola "Tengo un gato", 
si es un pájaro, que imprima en la consola "Tengo un pájaro" y 
si no es ninguno de los 3 que imprima "No tengo una mascota convencional"
"""

known_pets: list[str] = ["perro", "gato", "pájaro"]

while True:
    pet_input: str = input("\nIngresa el tipo de mascota que tienes: ").strip().lower()

    if not pet_input:
        print("Entrada vacía. Intenta de nuevo.")
        continue  # Skip iteration on invalid empty input

    if pet_input == "perro":
        print("Tengo un perro")
        break
    elif pet_input == "gato":
        print("Tengo un gato")
        break
    elif pet_input in ["pájaro", "pajaro"]:
        print("Tengo un pájaro")
        break
    else:
        print("No tengo una mascota convencional")
        break
