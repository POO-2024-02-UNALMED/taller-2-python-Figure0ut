class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, nuevo_color):
        colores_permitidos = {"rojo", "verde", "amarillo", "negro", "blanco"}
        if nuevo_color in colores_permitidos:
            self.color = nuevo_color


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, nuevo_registro):
        self.registro = nuevo_registro

    def asignarTipo(self, nuevo_tipo):
        tipos_permitidos = {"electrico", "gasolina"}
        if nuevo_tipo in tipos_permitidos:
            self.tipo = nuevo_tipo


class Auto:
    cantidadCreados = ""

    def __init__(self, modelo, precio, marca, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = []
        self.marca = marca
        self.motor = None
        self.registro = registro
        Auto.cantidadCreados = str(int(Auto.cantidadCreados) + 1)

    def cantidadAsientos(self):
        return sum(1 for asiento in self.asientos if isinstance(asiento, Asiento))

    def verificarIntegridad(self):
        registros = [self.registro]
        
        if self.motor:
            registros.append(self.motor.registro)
        
        registros.extend(asiento.registro for asiento in self.asientos)
        
        if all(reg == registros[0] for reg in registros):
            return "Auto original"
        return "Las piezas no son originales"
