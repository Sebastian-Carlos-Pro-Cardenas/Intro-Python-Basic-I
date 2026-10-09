"""
--------------------------- COLECCIONES ---------------------------
En este taller aprenderás a manipular coleccciones de datos: Listas, diccionarios, tuplas y sets.
"""

"""
 --- LISTAS ---
Las listas son ordenadas y mutables.
Pueden contener elementos duplicados.
Puedes modificar, añadir y eliminar elementos.
"""
"""
--- Ejercicio 1 Listas ---
Crea una variable "mascotas" que almacene una lista con los siguientes elementos: 'perro', 'gato', 'loro'
Imprime por consola el valor almacenado
Despues haz los pasos pedidos
"""

# Escribe tu código aquí
pet_list: list[str] = ['perro', 'gato', 'loro']
print(f"Lista de mascotas inicial: {pet_list}")

# Escribe el código para saber la cantidad de elementos que tiene la lista, imprimir por consola
list_length: int = len(pet_list)
print(f"Cantidad de elementos en la lista: {list_length}")

# Escribe el código para acceder al valor de la posición 2, imprimir por consola
element_at_index_two: str = pet_list[2]
print(f"Elemento en la posición 2: {element_at_index_two}")

# Escribe el código para agregar una elemento a la lista, imprimir por consola la lista
pet_list.append('hámster')
print(f"Lista tras agregar elemento: {pet_list}")

# Escribe el código para modificar un elemento de la lista, imprimir por consola la lista
pet_list[0] = 'hurón'
print(f"Lista tras modificar elemento en índice 0: {pet_list}")

# Escribe el código para eliminar un elemento de la lista, imprimir por consola la lista
pet_list.remove('gato')
print(f"Lista tras eliminar 'gato': {pet_list}\n")

"""
 --- TUPLAS ---
Las tuplas son ordenadas e inmutables.
Pueden contener elementos duplicados.
No puedes modificar, añadir o eliminar elementos después de la creación.
"""

"""
--- Ejercicio 2 Tuplas ---
Crea una variable "plantas" que almacene una tupla con los siguientes elementos: 'cactus', 'orquidea', 'rosas'
Imprime por consola el valor almacenado
Despues haz los pasos pedidos
"""
# Escribe tu código aquí
plant_tuple: tuple[str, ...] = ('cactus', 'orquidea', 'rosas')
print(f"Tupla de plantas inicial: {plant_tuple}")

# Escribe el código para saber la cantidad de elementos que tiene la tupla, imprimir por consola
tuple_length: int = len(plant_tuple)
print(f"Cantidad de elementos en la tupla: {tuple_length}")

# Escribe el código para acceder al valor de la posición 2, imprimir por consola
tuple_element_at_index_two: str = plant_tuple[2]
print(f"Elemento en la posición 2 de la tupla: {tuple_element_at_index_two}")

# Intentar modificar una tupla
# plantas[1] = 'hoja rota'  # Descomenta esta línea para ver qué sucede

# Análisis del intento de modificación:
# Al intentar modificar un ítem de la tupla se genera un error 'TypeError: 'tuple' object does not support item assignment'.
# Esto sucede porque las tuplas son estructuras de datos inmutables; sus elementos no se pueden reasignar, añadir ni eliminar tras crearse.


"""
 --- SETS ---
Los sets son desordenados y mutables.
No pueden contener elementos duplicados.
Puedes añadir y eliminar elementos, pero no puedes modificar los elementos existentes.
"""

"""
--- Ejercicio 3 Sets ---
Crea una variable "nombres" que almacene un set con los siguientes elementos: 'María', 'Cris', 'Cris', 'Alex'
Imprime por la terminal dicha variable
Haz los pasos pedidos
"""

# Escribe el código aqui
name_set: set[str] = {'María', 'Cris', 'Cris', 'Alex'}
print(f"\nSet de nombres: {name_set}")

# Explica qué sucede cuándo imprimes el valor que almacena "nombres"

# Explicación de qué sucede al imprimir "nombres":
# El set descarta automáticamente el duplicado 'Cris', almacenando solo elementos únicos.
# Además, la secuencia al imprimirse no garantiza un orden fijo, dado que los conjuntos (sets) no son ordenados en Python.

# Escribe el código para saber la cantidad de elementos que tiene el set, imprimir por consola
set_length: int = len(name_set)
print(f"Cantidad de elementos únicos en el set: {set_length}")

# Escribe el código para acceder al valor de la posición 3, imprimir por consola
accessible_set_list: list[str] = list(name_set)
print(f"Acceso a posición 2/3 tras conversión a lista: {accessible_set_list[2] if len(accessible_set_list) > 2 else 'N/A'}")

# Escribe el código para agregar una elemento al set, imprimir por consola el set
name_set.add('Sofia')
print(f"Set tras agregar elemento: {name_set}")

# Escribe el código para eliminar un elemento del set, imprimir por consola el set
name_set.remove('María')
print(f"Set tras eliminar 'María': {name_set}\n")

"""
 --- DICCIONARIOS ---
Los diccionarios son desordenados y mutables.
Contienen pares clave-valor.
Puedes añadir, modificar y eliminar pares clave-valor.
"""

"""
--- Ejercicio 4 Diccionarios ---
Crea un diccionario llamado "ciudad" con las claves 'nombre' y 'pais' y los valores 'Barcelona' y 'España' respectivamente.
Imprime el diccionario 
"""
city_profile: dict[str, str] = {
    'nombre': 'Barcelona',
    'pais': 'España'
}
print(f"Diccionario inicial: {city_profile}")

city_name: str = city_profile['nombre']
print(f"Valor de la clave 'nombre': {city_name}")

city_profile['poblacion'] = '1.6 millones'
print(f"Diccionario tras añadir 'poblacion': {city_profile}")

city_profile['nombre'] = 'Barcelona Capital'
print(f"Diccionario tras modificar 'nombre': {city_profile}")

del city_profile['pais']
print(f"Diccionario tras eliminar la clave 'pais': {city_profile}")