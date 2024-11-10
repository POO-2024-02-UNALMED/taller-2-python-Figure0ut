class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        colores_permitidos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in colores_permitidos:
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        tipos_permitidos = ["electrico", "gasolina"]
        if tipo in tipos_permitidos:
            self.tipo = tipo

class Auto:
    cantidadCreados = ""  

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados = str(int(Auto.cantidadCreados) + 1)

    def cantidadAsientos(self):
        return len([asiento for asiento in self.asientos if isinstance(asiento, Asiento)])

    def verificarIntegridad(self):
        if self.motor is None:
            return "Las piezas no son originales"

        registro_auto = self.registro
        registro_motor = self.motor.registro

        if registro_auto != registro_motor:
            return "Las piezas no son originales"

        for asiento in self.asientos:
            if isinstance(asiento, Asiento):
                if asiento.registro != registro_auto:
                    return "Las piezas no son originales"

        return "Auto original"