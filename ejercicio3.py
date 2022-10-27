class Producto():
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        print(f"el producto {self.nombre} se ha creado correctamente")
    def __str__(self):
        return(f"el producto {self.nombre} con codigo {self.codigo} tiene un precio de {self.precio} y es del tipo {self.tipo}")
    
comida1 = Producto(12, "manzana", 20, "fruta")
comida2 = Producto(54, "chocolate", 10, "dulce")
comida3 = Producto(30, "jamon", 8, "embutido")

print(comida1)
print(comida2)
print(comida3)

