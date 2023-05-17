# estructura de datos
d_productos = {}

# plain data object
class Producto:
    def __init__(self, idp:str, nomp:str, descrip:str, prec:float, desc:str, precdesc:float, cantdisp:int, eti:str, cantven:int,idv:str,comen:list=[]):

        '''
        
        :param idp: Crea el objeto para el  id de los productos
        :param nom: Crea el objeto para el nombre de los productos
        :param descrip: Crea el objeto para la descripcion de los productos
        :param foto: Crea el objeto para la foto de los productos
        :param prec: Crea el objeto para el precio de los productos
        :param desc: Crea el objeto para el descuento de los productos
        :param precdesc: Crea el objeto para el precio con el descuento de los productos 
        :param cantdisp: crea el objeto para la cantidad de productos disponibles
        :param eti: crea el objeto para las etiquetas de un producto
        :param cantven: crea el objeto para la cantidad de productos vendidos
        '''
        self.idprod = idp
        self.nombrep =nomp
        self.descripcion = descrip
        self.prcio= prec
        self.descuento = desc
        self.preciodescu = precdesc
        self.cantdisponible = cantdisp
        self.etiqueta = eti
        self.cantvendida = 0
        self.idv = idv
        self.comen = comen


# clase de control de datas
class controlProductos:


    def insertarp(self, producto:Producto) -> bool:
        """
        Inserta un nuevproducto a la estructura de datos
        :param producto: un objeto de la clase Producto
        :return: True si solo si el objeto fue almacenado correctamente False en caso contrario
        """
        if producto.idprod not in d_productos:
            d_productos.update({producto.idprod:producto})
            return True
        else:
            return False

    def eliminarp(self, producto) -> bool:
        if producto.idprod in d_productos:
            del d_productos[producto.idprod]
            return True
        else:
            return False

    def modificarp(self, producto) -> bool:
        if producto.idprod in d_productos:
            d_productos[producto.idprod] = producto
            return True
        else:
            return False

    def getProducto(self,idprod) -> Producto:
        if idprod in d_productos:
            return d_productos[idprod]
        else:
            return None
    def listProducto(self) -> list:
        return [prod for prod in d_productos.values()]

    def buscarp(self, nombrep):
        productos = []
        for producto in d_productos.values():
            if producto.nombrep == nombrep:
                productos.append(producto)
        if productos is not None:
            return productos
        else:
            return None
