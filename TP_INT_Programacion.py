# Función para crear un nodo nuevo con valor, lista de hijos y referencia al padre
def crearNodo(valores):
    return {
        "valor": valores,
        "hijos": [],
        "padre": None
    }

# Función para agregar un nodo al árbol
def agregar_nodo(arbol, valores, padre=None):
    # Verifica si el nodo ya existe
    if valores in arbol["nodos"]:
        print(f"El nodo '{valores}' ya existe.")
        return

    # Crea el nuevo nodo y lo guarda en el diccionario de nodos
    nuevoNodo = crearNodo(valores)
    arbol["nodos"][valores] = nuevoNodo

    # Si se especificó un padre
    if padre:
        # Verifica si el nodo padre existe
        if padre in arbol["nodos"]:
            nodoPadre = arbol["nodos"][padre]
            nuevoNodo["padre"] = nodoPadre  # Asigna el padre
            nodoPadre["hijos"].append(nuevoNodo)  # Agrega como hijo del padre
            print(f"El nodo '{valores}' fue añadido y sera hijo de '{padre}'.")
        else:
            print(f"El nodo padre no existe '{padre}', vuelve a intentarlo con un nodo existente.")
    else:
        # Si no se especifica padre, se intenta agregar como raíz
        if arbol["raiz"]:
            print(f"Ya existe una raíz: '{arbol['raiz']['valor']}'.")
        else:
            arbol["raiz"] = nuevoNodo  # Asigna como raíz
            print(f"La raíz '{valores}' fue creada.")

# Función para mostrar el árbol de forma recursiva e indentada
def mostrar_arbol(nodo, nivel=0):
    print("  " * nivel + nodo["valor"])  # Muestra el nodo con indentación
    for hijo in nodo["hijos"]:
        mostrar_arbol(hijo, nivel + 1)  # Llama recursivamente a los hijos

# Estructura del árbol: contiene todos los nodos y una referencia a la raíz
arbol = {
    "nodos": {},
    "raiz": None
}

while True:
    print("--- Menú ---")
    print("1. Agregar nodo al arbol")
    print("2. Mostrar árbol")
    print("3. Salir")

    opcion = input("Elegí una opción de 1 a 3: ")

    if opcion == "1":
        nombre = input("Nombre del nodo: ")
        padre = input("Nombre del nodo padre: ")
        padre = padre if padre != "" else None
        agregar_nodo(arbol, nombre, padre)

    elif opcion == "2":
        # Muestra el árbol si existe una raíz
        if arbol["raiz"]:
            print("El arbol actualmente esta compuesto por:")
            mostrar_arbol(arbol["raiz"])
        else:
            print("Esa raiz no existe.")

    elif opcion == "3":
        # Programa finalizado
        print("Hasta la próxima.")
        break

    else:
        #  opción inválida
        print("Ingrese un numero que este dentro de (1-3).")