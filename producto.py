class Producto:
    def __init__(self,nombre,tipo,valor_unitario,cantidad_bodega,cantidad_minima):
        self.nombre=nombre
        self.tipo=tipo
        self.valor_unitario=valor_unitario
        self.cantidad_bodega=cantidad_bodega
        self.cantidad_minima=cantidad_minima
    def __str__(self):
        return(f'nombre: {self.nombre},tipo: {self.tipo}, Valor unitario: {self.valor_unitario},cantidad en la bodega: {self.cantidad_bodega}')