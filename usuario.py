# estructura de datos
d_us = {}

# plain data object
class Usuario:
    def __init__(self, idu:str, nomu:str, login:str, contra:str):
        """

        :param idu: Crea el objeto para el  id de el usuario
        :param nomu: Crea el objeto para el  nombre de el usuario
        :param login: Crea el objeto para el  login de los usuarios
        :param contra: Crea el objeto para la contrasena de los usuarios
        """

        self.idu = idu
        self.nombreu = nomu
        self.login = login
        self.contra = contra


# clase de control de datos
class controlUsuario:


    def insertaru(self, usuario:Usuario) -> bool:

        if usuario.idu not in d_us:
            d_us.update({usuario.idu:usuario})
            return True
        else:
            return False

    def eliminaru(self, usuario) -> bool:
        if usuario.idu in d_us:
            del d_us[usuario.idu]
            return True
        else:
            return False

    def modificaru(self, usuario) -> bool:
        if usuario.idu in d_us:
            d_us[usuario.idu] = usuario
            return True
        else:
            return False

    def getUsuario(self,idu) -> Usuario:
        if idu in d_us:
            return d_us[idu]
        else:
            return None


    def listUsuarios(self) -> list:
        return [us for us in d_us.values()]

    def verificarUsuario(self, idu, contra):
        if idu in d_us and d_us[idu].contra == contra:
            return True
        else:
            return None


