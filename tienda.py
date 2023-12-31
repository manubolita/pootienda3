from leer import *
from producto import *
from venta import *
from factura import *
class Tienda:
    dinero_en_caja=0
    numero_factura=0
    def __init__(self,productos,facturas):
        self.productos=productos
        self.facturas=facturas
    def adicionar_productos(self):
        #y=1
        #while y==1:
        #    nombre=input('digite el nombre del producto--->')
        #    tipo=int(input('digite el tipo del producto--->'))
        #    valor_unitario=int(input('digite el valor unitario del producto--->'))
        #    cantidad_bodega=int(input('digite la cantidad en bodega del producto--->'))
        #    cantidad_minima=int(input('digite la cantidad minima para vender el producto--->'))
        #    self.productos.append(Producto(nombre,tipo,valor_unitario,cantidad_bodega,cantidad_minima))
        #    y=int(input('ahora esta digitando los productos, para salir pesione una tecla y 1 para continuar'))
        self.productos.append(Producto('lapiz',1,2000,50,10))
        self.productos.append(Producto('cuaderno',1,3000,50,10))
        self.productos.append(Producto('aspirina',2,1000,50,5))
        self.productos.append(Producto('arroz',3,3000,50,5))
        self.productos.append(Producto('papa',3,3000,50,5))
        print('se ha creado una lista  con 5 productos')
    def mostrar_productos(self):
        if len(self.productos)>0:
            print('productos de la tienda xx')
            for producto in self.productos:
                print(producto)
        else:
            print('no hay productos')
    def consultar_producto(self,producto):
        for prod in self.productos:
            if prod.nombre==producto:
                return prod
        if prod not in self.productos:
            return None
    def realizar_venta(self):
        numero_factura=Tienda.numero_factura+1
        factura=Factura(numero_factura)
        while True:
            self.mostrar_productos()
            producto=input('digitar producto--->')
            producto_ob=self.consultar_producto(producto)
            
            if producto_ob!=None:
                if factura.consultar_venta(producto):
                    if venta.producto.nombre==producto:
                        print('el producto ya esta en la factura, por tanto se le sumara a la cantidad anterior')
                        producto_ob_factura=venta.cantidad
                        cantidad_nueva=int(input('cantidad a sumar--->'))
                        if producto_ob.cantidad_bodega>cantidad_nueva:
                            cantidadv=cantidad_nueva
                        elif producto_ob.cantidad_bodega>0:
                            cantidadv=producto_ob.cantidad_bodega
                        else:
                            print('no hay productos a la venta')
                            break
                    
                        producto_ob_factura+=cantidadv
                        factura.ventas[numero_factura-1]=(producto_ob.nombre,producto_ob_factura)
                        valor_venta_individual=producto_ob.valor_unitario*cantidad_nueva
                        valor_venta=producto_ob.valor_unitario*producto_ob_factura
                        print(f'detalle venta \n producto--->{producto_ob.nombre} \n cantidad--->{producto_ob_factura}')
                        Tienda.dinero_en_caja=Tienda.dinero_en_caja+valor_venta_individual
                        factura.valor_factura+=valor_venta_individual
                        producto_ob.cantidad_bodega-=cantidad_nueva
                        resp=input('adicionar mas productos (s/n)--->')
                        if resp=='n' or resp=='N':
                            self.facturas.append(factura)
                            factura.mostrar_factura_detalle()
                            Tienda.numero_factura+=1
                            break
                else:
                    print(producto_ob)
                    cantidad=int(input('cantidad a vender--->'))
                    if producto_ob.cantidad_bodega>cantidad:
                        cantidadv=cantidad
                    elif producto_ob.cantidad_bodega>0:
                        cantidadv=producto_ob.cantidad_bodega
                    else:
                        print('no hay productos a la venta')
                        continue
                    valor_venta=producto_ob.valor_unitario*cantidadv
                    nombre=producto_ob.nombre
                    print(f'detalle venta \n producto--->{nombre} \n cantidad--->{cantidadv}')
                    Tienda.dinero_en_caja=Tienda.dinero_en_caja+valor_venta
                    venta=Venta(producto_ob,cantidadv)
                    factura.ventas.append(venta)
                    factura.valor_factura+=valor_venta
                    producto_ob.cantidad_bodega-=cantidadv
                    resp=input('adicionar mas productos (s/n)--->')
                    if resp=='n' or resp=='N':
                        self.facturas.append(factura)
                        factura.mostrar_factura_detalle()
                        Tienda.numero_factura+=1
                        break
            else:
                print('producto no valido digitelo nuevamente---')
