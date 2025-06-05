# Clase que representa un nodo en el árbol
class Nodos:
    def __init__(self, valor):
        self.valor = valor  # Valor que contiene el nodo
        self.hijos = []     # Lista de nodos hijos
        self.padre = None   # Referencia al nodo padre (inicialmente None)

    # Método para agregar un hijo al nodo actual
    def agregarHijo(self, hijo):
        hijo.padre = self          # Se establece el nodo actual como padre del hijo
        self.hijos.append(hijo)    # Se agrega el hijo a la lista de hijos

# Clase que representa el árbol completo
class Arboles:
    def __init__(self):
        self.nodos = {}    # Diccionario para almacenar los nodos por su valor
        self.raiz = None   # Referencia al nodo raíz del árbol

    # Método para agregar un nodo al árbol
    def agregarNodo(self, valor, padre=None):
        if valor in self.nodos:
            # Si el nodo ya existe, no se agrega de nuevo
            print(f"El nodo '{valor}' ya existe.")
            return

        nuevoNodo = Nodos(valor)      # Se crea un nuevo nodo con el valor dado
        self.nodos[valor] = nuevoNodo # Se agrega al diccionario de nodos

        if padre:
            if padre in self.nodos:
                # Si se especifica un padre y existe, se agrega como hijo de ese padre
                self.nodos[padre].agregarHijo(nuevoNodo)
                print(f"El nodo '{valor}' fue añadido como hijo de '{padre}'.")
            else:
                # Si el padre no existe, se muestra un mensaje de error
                print(f"El nodo padre no existe '{padre}'.")
        else:
            if self.raiz:
                # Si ya hay una raíz y se intenta agregar otra, se muestra un mensaje
                print(f"Ya existe una raíz: '{self.raiz.valor}'.")
            else:
                # Si no hay raíz, este nodo se convierte en la raíz del árbol
                self.raiz = nuevoNodo
                print(f"La raíz '{valor}' fue creada.")

    # Método para mostrar el árbol recursivamente desde un nodo dado
    def mostrarArbol(self, nodo=None, nivel=0):
        if nodo is None:
            nodo = self.raiz  # Si no se especifica un nodo, se usa la raíz
        print("  " * nivel + nodo.valor)  # Imprime el nodo con sangría según el nivel
        for hijo in nodo.hijos:
            self.mostrarArbol(hijo, nivel + 1)  # Llamada recursiva para mostrar los hijos

# Bloque principal que se ejecuta si este archivo es el programa principal
if __name__ == "__main__":
    arbol = Arboles()  # Se crea una instancia del árbol

    # Bucle principal del menú
    while True:
        print("\n--- Menú ---")
        print("1. Agregar nodo")
        print("2. Mostrar árbol")
        print("3. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            # Solicita el nombre del nuevo nodo y el nombre del padre
            nombre = input("Nombre del nodo: ")
            padre = input("Nombre del nodo padre: ")
            padre = padre.strip() if padre.strip() != "" else None  # Convierte texto vacío en None
            arbol.agregarNodo(nombre, padre)  # Agrega el nodo al árbol

        elif opcion == "2":
            # Muestra el árbol si existe una raíz
            if arbol.raiz:
                print("\nÁrbol actual:")
                arbol.mostrarArbol()
            else:
                print("No existe esa raiz.")

        elif opcion == "3":
            # Finaliza el programa
            print("Hasta la proxima.")
            break

        else:
            # Opción inválida del menú
            print("Opción inválida.")
