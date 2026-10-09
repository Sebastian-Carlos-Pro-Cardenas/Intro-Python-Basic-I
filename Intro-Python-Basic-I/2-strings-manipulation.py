"""
--------------------------- MANIPULACIÓN DE STRINGS ---------------------------
En este taller aprenderás cómo crear manipular cadenas de texto y cómo manejar entradas de datos del usuario.
"""

"""
--- Ejercicio 1 ---
Crea una variable llamada "hobbie". 
Asígnale como valor una string con uno de tus hobbies". 
Crea otra variable llamada "name"
Asígnale como valor una string con tu nombre". 
Crea otra variable llamada "teammate"
Asígnale como valor una string con el nombre de una compañera". 
Crea una variable llamada "teammate-hobbie". 
Asígnale como valor una string con unos de sus hobbies". 
"""

user_hobby: str = "fotografía"
user_name: str = "Carlos"
teammate_name: str = "Elena"
teammate_hobby: str = "pintar"

"""
--- Ejercicio 2 Concatenación ---
Imprime por consola el siguiente mensaje concatenando las variales anteriormente declaradas:
"Soy [name] y en mis tiempos libres me gusta [hobbie]"
"""

concatenated_message: str = "Soy " + user_name + " y en mis tiempos libres me gusta " + user_hobby
print(concatenated_message)

"""
--- Ejercicio 3 f-strings ---
Imprime por consola el siguiente mensaje usando f-strings para unir las frases de las variales anteriormente declaradas:
"Ella es [teammate] y en sus tiempos libres le gusta [teammate-hobbie]"
"""

formatted_message: str = f"Ella es {teammate_name} y en sus tiempos libres le gusta {teammate_hobby}"
print(formatted_message)

"""
--- Ejercicio 4 separación por comas ---
Imprime por consola el siguiente mensaje usando separación por comas para unir las frases de las variales anteriormente declaradas:
"Ella se llama [teammate] y yo me llamo [name]"
"""

print("Ella se llama", teammate_name, "y yo me llamo", user_name)

"""
--- Ejercicio 5 separación con operador % ---
Imprime por consola el siguiente mensaje usando separación con el operador % para unir las frases de las variales anteriormente declaradas:
"Además de programar, nos gusta [hobbie] y [teammate-hobbie]"
"""

percent_formatted_message: str = "Además de programar, nos gusta %s y %s" % (user_hobby, teammate_hobby)
print(percent_formatted_message)

"""
--- Ejercicio 6 input data ---
Escribe dos variables que reciban por terminal un número cada una
"""

first_raw_input: str = input("Ingresa el primer número: ")
second_raw_input: str = input("Ingresa el segundo número: ")

"""
--- Ejercicio 7 ---
Imprime por consola el resultado de la suma de los dos número obtenidos anteriormente y 
en un comentario de línea escribe lo que sucede. ¡Recuerda que puedes usar type() para indagar mas!
"""

raw_sum_result = first_raw_input + second_raw_input
print(f"Resultado de la suma sin transformar: {raw_sum_result}")
print(f"Tipo de dato de 'first_raw_input': {type(first_raw_input)}")

# Análisis: La función input() siempre retorna valores de tipo string (str). Al usar el operador '+', Python no realiza una adición aritmética, sino una concatenación de cadenas de texto (ej. "5" + "3" resulta en "53").

"""
--- Ejercicio 8 conversión de strings ---
Transforma los valores recibidos en el ejercicio 6 a números
Imprime por consola el resultado de la suma de los dos número obtenidos anteriormente
"""

first_number: float = float(first_raw_input)
second_number: float = float(second_raw_input)

arithmetic_sum: float = first_number + second_number
print(f"Resultado real de la suma aritmética: {arithmetic_sum}")
