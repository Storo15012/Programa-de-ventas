from datetime import datetime
# estructura de datos
d_vendors = {}

# plain data object
class Vendedor:
    def __init__(self, idv:str, cont:str,fei:datetime, ubi:str, tel:str, nom:str,prod:list=[]):
        """

        :param idv: Crea el objeto para el  id de vendedor
        :param cont: Crea el objeto para la contrasena de el vendedor
        :param fei: Crea el objeto para la fecha de inscripcion de el vendedor
        :param ubi: Crea el objeto para la ubicacion de el vendedor
        :param tel: Crea el objeto para el  numero de telefono de el vendedor
        :param nom: Crea el objeto para el  nombre de el vendedor
        :param prod: Crea el objeto para la lista de productos de el vendedor
        """

        self.idvend = idv
        self.cont = cont
        self.feincrip =fei
        self.cantVent = 0
        self.ubi = ubi
        self.tel = tel
        self.nombre = nom
        self.prod = prod
# clase de control de datas
class controlVendedor:


    def insertar(self, vendor:Vendedor) -> bool:

        if vendor.idvend not in d_vendors:
            d_vendors.update({vendor.idvend:vendor})
            return True
        else:
            return False

    def eliminar(self, vendor) -> bool:
        if vendor.idvend in d_vendors:
            del d_vendors[vendor.idvend]
            return True
        else:
            return False

    def modificar(self, vendor) -> bool:
        if vendor.idvend in d_vendors:
            d_vendors[vendor.idvend] = vendor
            return True
        else:
            return False

    def getVendedor(self,idvend) -> Vendedor:
        if idvend in d_vendors:
            return d_vendors[idvend]
        else:
            return None

    def listVendedor(self) -> list:
        return [ven for ven in d_vendors.values()]

    def verificarVendedor(self, idvend, cont):
        if idvend in d_vendors and d_vendors[idvend].cont == cont:
            return True
        else:
            return None

    def eliminarProducto(self, idvend, idprod) -> bool:
        if idvend in d_vendors:
            vendedor = d_vendors[idvend]
            if idprod in vendedor.prod:
                vendedor.prod.remove(idprod)
                d_vendors[idvend] = vendedor
                return True
        else:
            return False
