"""
--------------------------- VARIABLES / TIPOS DE DATOS ---------------------------
En este taller aprenderás cómo crear variables, trabajar con diferentes tipos de datos.
"""

"""
--- Ejercicio 1 Variables---
Crea una variable llamada "mensaje". 
Asígnale el valor "¡Hola, Mundo!". 
Imprime el valor de la variable en la consola.
"""

welcome_message: str = "¡Hola, Mundo!"
print(welcome_message)

"""
--- Ejercicio 2 Variables---
Invoca la variable anterior llamada "mensaje". 
Reasígnale el valor "Hello world!". 
Imprime el valor de la variable en la consola.
Escribe en un comentario de línea lo que sucede.
"""

welcome_message = "Hello world!"
print(welcome_message)

"""
--- Ejercicio 3 Tipos de datos---
Crea variables para cada uno de los siguientes tipos de datos y colecciones: string, int, float, 
bool, list, tuple, dicctionary and set. 
Imprime cada variable y el tipo de dato o colección que almacena en la consola.
"""

user_name: str = "Alice Vance"
user_age: int = 28
account_balance: float = 1450.75
is_active_account: bool = True

programming_skills: list[str] = ["Python", "SQL", "Git"]
geographic_coordinates: tuple[float, float] = (40.4168, -3.7038)
user_profile: dict[str, str | int] = {
    "id": 101,
    "role": "Developer",
    "city": "Cuenca"
}
unique_identifiers: set[int] = {1001, 1002, 1003}

print(f"Value: '{user_name}' | Type: {type(user_name).__name__}")
print(f"Value: {user_age} | Type: {type(user_age).__name__}")
print(f"Value: {account_balance} | Type: {type(account_balance).__name__}")
print(f"Value: {is_active_account} | Type: {type(is_active_account).__name__}")
print(f"Value: {programming_skills} | Type: {type(programming_skills).__name__}")
print(f"Value: {geographic_coordinates} | Type: {type(geographic_coordinates).__name__}")
print(f"Value: {user_profile} | Type: {type(user_profile).__name__}")
print(f"Value: {unique_identifiers} | Type: {type(unique_identifiers).__name__}")
