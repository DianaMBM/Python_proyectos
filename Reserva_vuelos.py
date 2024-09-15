class Destino:
    def __init__(self, tipo_vuelo, nombre):
        self.tipo_vuelo = tipo_vuelo
        self.nombre = nombre

    def Mostrarinfo(self):
        raise NotImplementedError


class Vuelo(Destino):
    def __init__(self, tipo_vuelo, nombre, aerolinea, hora, precio, impuesto):
        super().__init__(tipo_vuelo, nombre)
        self.aerolinea = aerolinea
        self.hora = hora
        self.precio = precio
        self.impuesto = impuesto

    def Mostrarinfo(self):
        print(" ")
        print(f"Información del vuelo a {self.nombre}")
        print(f"Tipo de vuelo: {self.tipo_vuelo}")
        print(f"Impuesto: {self.impuesto}")
        print(f"Aerolínea: {self.aerolinea}")
        print(f"Hora: {self.hora}")
        print(f"Precio: {self.precio}")
        print(" ")


def main():
    vuelos = []
    while True:
        tipo_vuelo = input("Ingrese el tipo de vuelo: Internacional, Nacional o Salir "
        ).lower()
        if tipo_vuelo == "salir":
            break
        elif tipo_vuelo == "internacional":
            impuesto = 500
            print(
                "El impuesto del vuelo internacional es de Q500.00, este incluye el impuesto de la entrada, salida, llegada, iva, tasas aeroportuarias y de seguridad."
            )
        elif tipo_vuelo == "nacional":
            impuesto = 100
            print("El impuesto del vuelo nacional es de Q100.00")
        else:
            print("Inválido. Las únicas opciones son: Internacional, Nacional o Salir")
            continue

        nombre = input("Ingrese el nombre del destino: ").lower()
        aerolinea = input("Ingrese la aerolínea: ").lower()
        hora = input("Ingrese la hora del vuelo: ")
        precio_vuelo = int(input("Ingrese el precio del vuelo: "))
        precio = precio_vuelo + impuesto
        vuelo = Vuelo(tipo_vuelo, nombre, aerolinea, hora, precio, impuesto)
        vuelos.append(vuelo)

    print("")
    print("Información de los vuelos")
    for vuelo in vuelos:
        vuelo.Mostrarinfo()


if __name__ == "__main__":
    main()
