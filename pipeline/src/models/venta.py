class Venta:
    def __init__(self):
        """
        Inicializa el modelo de venta
        """
        self.id = None
        self.producto = None
        self.cantidad = 0
        self.precio_unitario = 0.0
        self.total = 0.0
        self.fecha = None
        self.vendedor = None
    
    def calcular_total(self):
        """
        Calcula el total de la venta
        """
        self.total = self.cantidad * self.precio_unitario
    
    def to_dict(self):
        """
        Convierte la venta a un diccionario
        Returns:
            dict: Representación de la venta en formato diccionario
        """
        return {
            'id': self.id,
            'producto': self.producto,
            'cantidad': self.cantidad,
            'precio_unitario': self.precio_unitario,
            'total': self.total,
            'fecha': self.fecha,
            'vendedor': self.vendedor
        }
    
    @staticmethod
    def from_dict(data):
        """
        Crea una instancia de Venta desde un diccionario
        Args:
            data (dict): Datos de la venta
        Returns:
            Venta: Nueva instancia de Venta
        """
        venta = Venta()
        venta.id = data.get('id')
        venta.producto = data.get('producto')
        venta.cantidad = data.get('cantidad', 0)
        venta.precio_unitario = data.get('precio_unitario', 0.0)
        venta.fecha = data.get('fecha')
        venta.vendedor = data.get('vendedor')
        venta.calcular_total()
        return venta