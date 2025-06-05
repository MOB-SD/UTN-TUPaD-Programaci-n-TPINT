class Nodos:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []
        self.padre = None

    def agregarHijo(self, hijo):
        hijo.padre = self
        self.hijos.append(hijo)

class Arboles:
    def __init__(self):
        self.nodos = {}
        self.raiz = None

    def agregarNodo(self, valor, padre=None):
        if valor in self.nodos:
            print(f"El nodo '{valor}' ya existe.")
            return

        nuevoNodo = Nodos(valor)
        self.nodos[valor] = nuevoNodo

        if padre:
            if padre in self.nodos:
                self.nodos[padre].agregarHijo(nuevoNodo)
                print(f"El nodo '{valor}' fue añadido como hijo de '{padre}'.")
            else:
                print(f"El nodo padre no existe '{padre}'.")
        else:
            if self.raiz:
                print(f"Ya existe una raíz: '{self.raiz.valor}'.")
            else:
                self.raiz = nuevoNodo
                print(f"La raíz '{valor}' fue creada.")

    def mostrarArbol(self, nivel = 0, nodo=None):
        if nodo is None:
            nodo = self.raiz
        print("  " * nivel + nodo.valor)
        for hijo in nodo.hijos:
            self.mostrarArbol(hijo, nivel + 1)


if __name__ == "__main__":
    arbol = Arboles()

    while True:
        print("\n--- Menú ---")
        print("1. Agregar nodo")
        print("2. Mostrar árbol")
        print("3. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            nombre = input("Nombre del nodo: ")
            padre = input("Nombre del nodo padre: ")
            padre = padre.strip() if padre.strip() != "" else None
            arbol.agregarNodo(nombre, padre)

        elif opcion == "2":
            if arbol.raiz:
                print("\nÁrbol actual:")
                arbol.mostrarArbol()
            else:
                print("No existe esa raiz.")

        elif opcion == "3":
            print("Hasta la proxima.")
            break

        else:
            print("Opción inválida.")
