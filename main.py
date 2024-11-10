class Asiento:
    def __init__(self):
        self.color = None
        self.precio = None
        self.registro = None

    def cambiarColor(self, nuevo_color):
        colores_permitidos = {"rojo", "verde", "amarillo", "negro", "blanco"}
        if nuevo_color in colores_permitidos:
            self.color = nuevo_color


class Motor:
    def __init__(self):
        self.numeroCilindros = None
        self.tipo = None
        self.registro = None

    def cambiarRegistro(self, nuevo_registro):
        self.registro = nuevo_registro

    def asignarTipo(self, nuevo_tipo):
        tipos_permitidos = {"electrico", "gasolina"}
        if nuevo_tipo in tipos_permitidos:
            self.tipo = nuevo_tipo


class Auto:
    cantidadCreados = ""

    def __init__(self):
        self.modelo = None
        self.precio = None
        self.asientos = []
        self.marca = None
        self.motor = None
        self.registro = None
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
