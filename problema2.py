def agregar_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return
    if nombre in inventario:
        print("El producto ya existe en el inventario.")
        return
    try:
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio: "))
    except ValueError:
        print("Cantidad y precio deben ser números válidos.")
        return
    if cantidad <= 0:
        print("La cantidad debe ser un número positivo.")
        return
    if precio <= 0:
        print("El precio debe ser un número positivo.")
        return
    inventario[nombre] = {'cantidad': cantidad, 'precio': precio}
    print("Producto agregado exitosamente.")


def ver_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
        return
    print("\nInventario:")
    for nombre, datos in inventario.items():
        total = datos['cantidad'] * datos['precio']
        print(f"- {nombre}: cantidad={datos['cantidad']}, precio={datos['precio']:.2f}, total={total:.2f}")


def buscar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a buscar: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return
    datos = inventario.get(nombre)
    if not datos:
        print("Producto no encontrado.")
        return
    total = datos['cantidad'] * datos['precio']
    print(f"Producto encontrado: {nombre} - cantidad={datos['cantidad']}, precio={datos['precio']:.2f}, total={total:.2f}")


def actualizar_cantidad(inventario):
    nombre = input("Ingrese el nombre del producto a actualizar: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return
    if nombre not in inventario:
        print("Producto no encontrado.")
        return
    try:
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
    except ValueError:
        print("La cantidad debe ser un número válido.")
        return
    if nueva_cantidad <= 0:
        print("La cantidad debe ser un número positivo.")
        return
    inventario[nombre]['cantidad'] = nueva_cantidad
    print("Cantidad actualizada exitosamente.")


def eliminar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return
    if nombre in inventario:
        del inventario[nombre]
        print("Producto eliminado exitosamente.")
    else:
        print("Producto no encontrado.")


def menu():
    inventario = {}
    while True:
        print("\nMenú:")
        print("1. Agregar producto")
        print("2. Ver inventario")
        print("3. Buscar producto")
        print("4. Actualizar cantidad")
        print("5. Eliminar producto")
        print("6. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == '1':
            agregar_producto(inventario)
        elif opcion == '2':
            ver_inventario(inventario)
        elif opcion == '3':
            buscar_producto(inventario)
        elif opcion == '4':
            actualizar_cantidad(inventario)
        elif opcion == '5':
            eliminar_producto(inventario)
        elif opcion == '6':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
