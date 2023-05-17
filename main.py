from PyQt5 import  QtWidgets, uic
from PyQt5.QtWidgets import *
from vendedores import controlVendedor, Vendedor
from producto import controlProductos, Producto
from usuario import controlUsuario, Usuario
from datetime import datetime

app = QtWidgets.QApplication([])
ppal = uic.loadUi("AppMain.ui")
wvend = uic.loadUi("VendorsGUI.ui")
wprod = uic.loadUi("ProductosGUI.ui")
wus = uic.loadUi("UsuariosGUI.ui")
wlog = uic.loadUi("LoginUsuario.ui")
wuslog = uic.loadUi("UsuarioLog.ui")
ctrlus = controlUsuario()
ctrlven = controlVendedor()
ctrlpro = controlProductos()
'''
CONTROL INTERFAZ DE VENDEDORES
'''

def openVendedores():
    # Configurar la tabla en la ventana de vendedores
    wvend.tableWidgetVends.setRowCount(len(ctrlven.listVendedor()))
    wvend.tableWidgetVends.setColumnCount(7)
    wvend.tableWidgetVends.setHorizontalHeaderLabels(["id","nombre","fe inicio","cant.ventas","ubicacion", "telefono","contrasena"])
    lstVens = ctrlven.listVendedor()
    wvend.tableWidgetVends.setRowCount(0)
    wvend.tableWidgetVends.setRowCount(len(lstVens))
    for i, v in enumerate(lstVens):
        wvend.tableWidgetVends.setItem(i, 0, QTableWidgetItem(v.idvend))
        wvend.tableWidgetVends.setItem(i, 1, QTableWidgetItem(v.nombre))
        wvend.tableWidgetVends.setItem(i, 2, QTableWidgetItem(v.feincrip.strftime('%Y/%m/%d')))
        wvend.tableWidgetVends.setItem(i, 3, QTableWidgetItem(str(v.cantVent)))
        wvend.tableWidgetVends.setItem(i, 4, QTableWidgetItem(v.ubi))
        wvend.tableWidgetVends.setItem(i, 5, QTableWidgetItem(v.tel))
        wvend.tableWidgetVends.setItem(i, 6, QTableWidgetItem(v.cont))
    # Mostrar la ventana de vendedores
    wvend.show()
  
def insertarVendedor():
    # Obtener los datos del vendedor desde los lineEdits
    idv = wvend.lineEditIdVend.text()
    nom = wvend.lineEditNomVend.text()
    fei = datetime.strptime(wvend.lineEditFeIniVend.text(), '%Y/%m/%d')
    ubi = wvend.lineEditUbicVend.text()
    tel = wvend.lineEditTelVend.text()
    cont = wvend.lineEditContVend.text()

    # Crear una instancia de Vendedor y agregarla al controlador de vendedores
    v = Vendedor(idv,cont, fei, ubi, tel, nom)
    if ctrlven.insertar(v):
        QMessageBox.information(wvend, "Éxito", f"El vendedor con ID {idv} ha sido insertado.")
        # Actualizar la tabla en la ventana de vendedores con los nuevos datos
        lstVens = ctrlven.listVendedor()
        wvend.tableWidgetVends.setRowCount(len(lstVens))
        for i, v in enumerate(lstVens):
            wvend.tableWidgetVends.setItem(i, 0, QTableWidgetItem(v.idvend))
            wvend.tableWidgetVends.setItem(i, 1, QTableWidgetItem(v.nombre))
            wvend.tableWidgetVends.setItem(i, 2, QTableWidgetItem(v.feincrip.strftime('%Y/%m/%d')))
            wvend.tableWidgetVends.setItem(i, 3, QTableWidgetItem(str(v.cantVent)))
            wvend.tableWidgetVends.setItem(i, 4, QTableWidgetItem(v.ubi))
            wvend.tableWidgetVends.setItem(i, 5, QTableWidgetItem(v.tel))
            wvend.tableWidgetVends.setItem(i, 6, QTableWidgetItem(v.cont))
    else:
        QMessageBox.information(wvend, "Error", f"El vendedor con ID {idv} ya existe, porfavor ingrese otro ID.")


def eliminarVendedor():
    idvend = wvend.lineEditIdVend.text()
    vendedor = ctrlven.getVendedor(idvend)
    if vendedor is not None:
        if ctrlven.eliminar(vendedor):
            # Vendedor eliminado correctamente
            QMessageBox.information(wvend, "Éxito", f"El vendedor con ID {idvend} ha sido eliminado.")
            # Actualizar la tabla de vendedores
            lstVens = ctrlven.listVendedor()
            wvend.tableWidgetVends.setRowCount(len(lstVens))
            for i,v in enumerate(lstVens):
                wvend.tableWidgetVends.setItem(i, 0, QTableWidgetItem(v.idvend))
                wvend.tableWidgetVends.setItem(i, 1, QTableWidgetItem(v.nombre))
                wvend.tableWidgetVends.setItem(i, 2, QTableWidgetItem(str(v.cantVent)))
                wvend.tableWidgetVends.setItem(i, 3, QTableWidgetItem(v.feincrip.strftime('%Y/%m/%d')))
                wvend.tableWidgetVends.setItem(i, 4, QTableWidgetItem(v.ubi))
                wvend.tableWidgetVends.setItem(i, 5, QTableWidgetItem(v.tel))
                wvend.tableWidgetVends.setItem(i, 6, QTableWidgetItem(v.cont))
        else:
            QMessageBox.information(wvend, "Error", f"El vendedor con ID {idvend} No ha sido eliminado.")
    else:
        # No se encontró el vendedor con el ID especificado
        QMessageBox.warning(wvend, "Error", f"No se encontró un vendedor con el ID {idvend}.")

def actualizarVendedor():
    # Obtener el ID del vendedor a actualizar
    idvend = wvend.lineEditIdVend.text()

    # Obtener el vendedor con ese ID
    vendedor = ctrlven.getVendedor(idvend)
    if vendedor is not None:
        # Actualizar los datos del vendedor con los valores de los QLineEdit correspondientes
        vendedor.nombre = wvend.lineEditNomVend.text()
        vendedor.feincrip = datetime.strptime(wvend.lineEditFeIniVend.text(), '%Y/%m/%d')
        vendedor.ubi = wvend.lineEditUbicVend.text()
        vendedor.tel = wvend.lineEditTelVend.text()
        vendedor.cont = wvend.lineEditContVend.text()

        # Modificar el vendedor en el diccionario de vendedores
        if ctrlven.modificar(vendedor):
            # Vendedor modificado correctamente
            QMessageBox.information(wvend, "Éxito", f"El vendedor con ID {idvend} ha sido actualizado.")
            # Actualizar la tabla de vendedores
            lstVens = ctrlven.listVendedor()
            wvend.tableWidgetVends.setRowCount(len(lstVens))
            for i,v in enumerate(lstVens):
                wvend.tableWidgetVends.setItem(i, 0, QTableWidgetItem(v.idvend))
                wvend.tableWidgetVends.setItem(i, 1, QTableWidgetItem(v.nombre))
                wvend.tableWidgetVends.setItem(i, 2, QTableWidgetItem(v.feincrip.strftime('%Y/%m/%d')))
                wvend.tableWidgetVends.setItem(i, 3, QTableWidgetItem(str(v.cantVent)))
                wvend.tableWidgetVends.setItem(i, 4, QTableWidgetItem(v.ubi))
                wvend.tableWidgetVends.setItem(i, 5, QTableWidgetItem(v.tel))
                wvend.tableWidgetVends.setItem(i, 6, QTableWidgetItem(v.cont))
        else:
            QMessageBox.information(wvend, "Error", f"El vendedor con ID {idvend} No ha sido actualizado.")
    else:
        # No se encontró el vendedor con el ID especificado
        QMessageBox.warning(wvend, "Error", f"No se encontró un vendedor con el ID {idvend}.")

def GuardarVendedores():
    ruta_archivo = 'vendedores.txt'
    try:
        with open(ruta_archivo, 'w') as archivo:
            num_filas = wvend.tableWidgetVends.rowCount()
            num_columnas = wvend.tableWidgetVends.columnCount()
            # Escribir encabezados
            #headers = [wvend.tableWidgetVends.horizontalHeaderItem(i).text() for i in range(num_columnas)]
            #archivo.write('\t'.join(headers) + '\n')
            # Escribir datos de productos
            for i in range(num_filas):
                datos_fila = []
                for j in range(num_columnas):
                    datos_fila.append(wvend.tableWidgetVends.item(i, j).text())
                archivo.write('\t'.join(datos_fila) + '\n')
        QMessageBox.information(wvend, 'Guardado', 'Los vendedores han sido guardados en el archivo.')
    except IOError:
        QMessageBox.warning(wvend, 'Error', 'No se pudo guardar los vendedores en el archivo.')


def CargarVendedores():
    ruta_archivo = 'vendedores.txt'
    try:
        with open(ruta_archivo, 'r') as archivo:
            # Leer datos línea por línea
            lineas = archivo.readlines()
            for linea in lineas:
                # Separar datos por el separador
                datos = linea.strip().split('\t')
                # Crear objeto Producto y agregarlo al controlador de productos
                v = Vendedor(datos[0], datos[1], datetime.strptime(datos[2], '%Y/%m/%d'),datos[4],datos[5],datos[6])
                ctrlven.insertar(v)
            # Obtener lista actualizada de usuarios y establecer el número de filas del tableWidgetUsu
            lstven = ctrlven.listVendedor()
            wvend.tableWidgetVends.setRowCount(len(lstven))
            # Establecer datos de usuarios en el tableWidgetUsu
            for i, v in enumerate(lstven):
                wvend.tableWidgetVends.setItem(i, 0, QTableWidgetItem(v.idvend))
                wvend.tableWidgetVends.setItem(i, 1, QTableWidgetItem(v.nombre))
                wvend.tableWidgetVends.setItem(i, 2, QTableWidgetItem(v.feincrip.strftime('%Y/%m/%d')))
                wvend.tableWidgetVends.setItem(i, 3, QTableWidgetItem(str(v.cantVent)))
                wvend.tableWidgetVends.setItem(i, 4, QTableWidgetItem(v.ubi))
                wvend.tableWidgetVends.setItem(i, 5, QTableWidgetItem(v.tel))
                wvend.tableWidgetVends.setItem(i, 6, QTableWidgetItem(v.cont))
        QMessageBox.information(wvend, 'Cargado', 'Los vendedores han sido cargados del archivo.')
    except FileNotFoundError:
        QMessageBox.warning(wvend, 'Error', 'No hay vendedores guardados.')



'''
CONTROL INTERFAZ DE PRODUCTO
'''


def openProductos():
    # Configurar la tabla en la ventana de productos
    wprod.tableWidgetProd.setRowCount(len(ctrlpro.listProducto()))
    wprod.tableWidgetProd.setColumnCount(10)
    wprod.tableWidgetProd.setHorizontalHeaderLabels(["id","nombre","descripcion","precio","descuento", "precio con descuento","disponoble","etiqueta","vendidos","ID vendedor"])
    lstProd = ctrlpro.listProducto()
    wprod.tableWidgetProd.setRowCount(0)
    wprod.tableWidgetProd.setRowCount(len(lstProd))
    for i, p in enumerate(lstProd):
        wprod.tableWidgetProd.setItem(i, 0, QTableWidgetItem(p.idprod))
        wprod.tableWidgetProd.setItem(i, 1, QTableWidgetItem(p.nombrep))
        wprod.tableWidgetProd.setItem(i, 2, QTableWidgetItem(p.descripcion))
        wprod.tableWidgetProd.setItem(i, 3, QTableWidgetItem(str(p.prcio)))
        wprod.tableWidgetProd.setItem(i, 4, QTableWidgetItem(p.descuento))
        wprod.tableWidgetProd.setItem(i, 5, QTableWidgetItem(str(p.preciodescu)))
        wprod.tableWidgetProd.setItem(i, 6, QTableWidgetItem(str(p.cantdisponible)))
        wprod.tableWidgetProd.setItem(i, 7, QTableWidgetItem(p.etiqueta))
        wprod.tableWidgetProd.setItem(i, 8, QTableWidgetItem(str(p.cantvendida)))
        wprod.tableWidgetProd.setItem(i, 9, QTableWidgetItem(str(p.idv)))


    # Mostrar la ventana de Productos
    wprod.show()
def insertarProducto():
    # Obtener los datos del producto desde los lineEdits
    idp = wprod.lineEditIdp.text()
    nomp = wprod.lineEditNomp.text()
    descrip = wprod.lineEditDescp.text()
    prec = float(wprod.lineEditPrecp.text())
    desc = wprod.lineEditdescup.text()
    precdesc = wprod.lineEditdescu2p.text()
    cantdisp = int(wprod.lineEditDispop.text())
    eti = wprod.lineEditEtip.text()
    cantven= int(wprod.lineEditVendp.text())
    idvend = wprod.lineEditVendedor.text()
    if ctrlven.getVendedor(idvend) is not None:
        v = ctrlven.getVendedor(idvend)
        if int(cantdisp) and int(prec) > 0:
            # Crear una variable de producto y agregarla al controlador de productos
            p = Producto(idp, nomp, descrip, prec, desc, precdesc, cantdisp,eti,cantven,idvend)
            # agregar el producto a la lista de productos del vendedor
            v.prod.append(p)
            if ctrlpro.insertarp(p):
                QMessageBox.information(wus, "Éxito", f"El producto con ID {idp} ha sido insertado correctamente.")
                # Actualizar la tabla en la ventana de productos con los nuevos datos
                lstProd = ctrlpro.listProducto()
                wprod.tableWidgetProd.setRowCount(len(lstProd))
                for i, p in enumerate(lstProd):
                    wprod.tableWidgetProd.setItem(i, 0, QTableWidgetItem(p.idprod))
                    wprod.tableWidgetProd.setItem(i, 1, QTableWidgetItem(p.nombrep))
                    wprod.tableWidgetProd.setItem(i, 2, QTableWidgetItem(p.descripcion))
                    wprod.tableWidgetProd.setItem(i, 3, QTableWidgetItem(str(p.prcio)))
                    wprod.tableWidgetProd.setItem(i, 4, QTableWidgetItem(p.descuento))
                    wprod.tableWidgetProd.setItem(i, 5, QTableWidgetItem(str(p.preciodescu)))
                    wprod.tableWidgetProd.setItem(i, 6, QTableWidgetItem(p.cantdisponible))
                    wprod.tableWidgetProd.setItem(i, 7, QTableWidgetItem(p.etiqueta))
                    wprod.tableWidgetProd.setItem(i, 8, QTableWidgetItem(str(p.cantvendida)))
                    wprod.tableWidgetProd.setItem(i, 9, QTableWidgetItem(str(p.idv)))

            else:
                QMessageBox.information(wprod, "Error", f"El producto con ID {idp} ya existe, porfavor ingrese otro ID.")

        else:
            QMessageBox.information(wprod, "Error", f"La cantidad del producto y el precio deben ser mayor que 0.")
    else:
        QMessageBox.information(wprod, "Error", f"El vendedor con ID {idvend} no existe, porfavor ingrese otro ID de vendedor.")

def eliminarProducto():
    idprod = wprod.lineEditIdp.text()
    idvend = wprod.lineEditVendedor.text()
    producto = ctrlpro.getProducto(idprod)
    pvend = ctrlven.getVendedor(idvend)
    if producto is not None and pvend is not None:
        if ctrlpro.eliminarp(producto):
            # producto eliminado correctamente
            QMessageBox.information(wprod, "Éxito", f"El producto con ID {idprod} ha sido eliminado.")
            # Actualizar la tabla de productos
            lstProd = ctrlpro.listProducto()
            wprod.tableWidgetProd.setRowCount(len(lstProd))
            for i, p in enumerate(lstProd):
                wprod.tableWidgetProd.setItem(i, 0, QTableWidgetItem(p.idprod))
                wprod.tableWidgetProd.setItem(i, 1, QTableWidgetItem(p.nombrep))
                wprod.tableWidgetProd.setItem(i, 2, QTableWidgetItem(p.descripcion))
                wprod.tableWidgetProd.setItem(i, 3, QTableWidgetItem(str(p.prcio)))
                wprod.tableWidgetProd.setItem(i, 4, QTableWidgetItem(p.descuento))
                wprod.tableWidgetProd.setItem(i, 5, QTableWidgetItem(str(p.preciodescu)))
                wprod.tableWidgetProd.setItem(i, 6, QTableWidgetItem(p.cantdisponible))
                wprod.tableWidgetProd.setItem(i, 7, QTableWidgetItem(p.etiqueta))
                wprod.tableWidgetProd.setItem(i, 8, QTableWidgetItem(str(p.cantvendida)))
                wprod.tableWidgetProd.setItem(i, 9, QTableWidgetItem(str(p.idv)))
            # Eliminar producto de la lista de producto de el vendedor
            ctrlven.eliminarProducto(idvend,idprod)
        else:
            QMessageBox.information(wprod, "Error", f"El producto con ID {idprod} No ha sido eliminado.")
    else:
        # No se encontró el producto con el ID especificado
        QMessageBox.warning(wprod, "Error", f"No se encontró un producto con el ID {idprod}.")

def actualizarProducto():
    # Obtener el ID del producto a actualizar
    idprod = wprod.lineEditIdp.text()

    # Obtener el producto con ese ID
    producto = ctrlpro.getProducto(idprod)
    if producto is not None:
        # Actualizar los datos del producto con los valores de los QLineEdit correspondientes
        producto.nombrep = wprod.lineEditNomp.text()
        producto.descripcion = wprod.lineEditDescp.text()
        producto.prcio = wprod.lineEditPrecp.text()
        producto.descuento = wprod.lineEditdescup.text()
        producto.preciodescu = wprod.lineEditdescu2p.text()
        producto.cantdisponible = wprod.lineEditDispop.text()
        producto.etiqueta = wprod.lineEditEtip.text()
        producto.cantvendida = wprod.lineEditVendp.text()
        if int(producto.cantdisponible) and int(producto.prcio) > 0:
            # Modificar el producto en el diccionario de productos
            if ctrlpro.modificarp(producto):
                # producto modificado correctamente
                QMessageBox.information(wprod, "Éxito", f"El producto con ID {idprod} ha sido actualizado.")
                # Actualizar la tabla de productos
                lstProd = ctrlpro.listProducto()
                wprod.tableWidgetProd.setRowCount(len(lstProd))
                for i, p in enumerate(lstProd):
                    wprod.tableWidgetProd.setItem(i, 0, QTableWidgetItem(p.idprod))
                    wprod.tableWidgetProd.setItem(i, 1, QTableWidgetItem(p.nombrep))
                    wprod.tableWidgetProd.setItem(i, 2, QTableWidgetItem(p.descripcion))
                    wprod.tableWidgetProd.setItem(i, 3, QTableWidgetItem(str(p.prcio)))
                    wprod.tableWidgetProd.setItem(i, 4, QTableWidgetItem(p.descuento))
                    wprod.tableWidgetProd.setItem(i, 5, QTableWidgetItem(str(p.preciodescu)))
                    wprod.tableWidgetProd.setItem(i, 6, QTableWidgetItem(p.cantdisponible))
                    wprod.tableWidgetProd.setItem(i, 7, QTableWidgetItem(p.etiqueta))
                    wprod.tableWidgetProd.setItem(i, 8, QTableWidgetItem(str(p.cantvendida)))
            else:
                QMessageBox.information(wprod, "Error", f"El producto con ID {idprod} No ha sido actualizado.")
        else:
            QMessageBox.information(wprod, "Error", f"La cantidad del producto y el precio deben ser mayor que 0.")

    else:
        # No se encontró el producto con el ID especificado
        QMessageBox.warning(wprod, "Error", f"No se encontró un producto con el ID {idprod}.")

def GuardarProductos():
    ruta_archivo = 'productos.txt'
    try:
        with open(ruta_archivo, 'w') as archivo:
            num_filas = wprod.tableWidgetProd.rowCount()
            num_columnas = wprod.tableWidgetProd.columnCount()
            # Escribir encabezados
            #headers = [wprod.tableWidgetProd.horizontalHeaderItem(i).text() for i in range(num_columnas)]
            #archivo.write('\t'.join(headers) + '\n')
            # Escribir datos de productos
            for i in range(num_filas):
                datos_fila = []
                for j in range(num_columnas):
                    datos_fila.append(wprod.tableWidgetProd.item(i, j).text())
                archivo.write('\t'.join(datos_fila) + '\n')
        QMessageBox.information(wprod, 'Guardado', 'Los productos han sido guardados en el archivo.')
    except IOError:
        QMessageBox.warning(wprod, 'Error', 'No se pudo guardar los productos en el archivo.')


def CargarProductos():
    ruta_archivo = 'productos.txt'
    try:
        with open(ruta_archivo, 'r') as archivo:
            # Leer datos línea por línea
            lineas = archivo.readlines()
            for linea in lineas:
                # Separar datos por el separador
                datos = linea.strip().split('\t')
                # Crear objeto Producto y agregarlo al controlador de productos
                p = Producto(datos[0], datos[1], datos[2], float(datos[3]),datos[4],float(datos[5]),int(datos[6]),datos[7],int(datos[8]),(datos[9]))
                ctrlpro.insertarp(p)
            # Obtener lista actualizada de productos y establecer el número de filas del tableWidgetProd
            lstProd = ctrlpro.listProducto()
            wprod.tableWidgetProd.setRowCount(len(lstProd))
            # Establecer datos de productos en el tableWidgetProd
            for i, p in enumerate(lstProd):
                wprod.tableWidgetProd.setItem(i, 0, QTableWidgetItem(p.idprod))
                wprod.tableWidgetProd.setItem(i, 1, QTableWidgetItem(p.nombrep))
                wprod.tableWidgetProd.setItem(i, 2, QTableWidgetItem(p.descripcion))
                wprod.tableWidgetProd.setItem(i, 3, QTableWidgetItem(str(p.prcio)))
                wprod.tableWidgetProd.setItem(i, 4, QTableWidgetItem(p.descuento))
                wprod.tableWidgetProd.setItem(i, 5, QTableWidgetItem(str(p.preciodescu)))
                wprod.tableWidgetProd.setItem(i, 6, QTableWidgetItem(str(p.cantdisponible)))
                wprod.tableWidgetProd.setItem(i, 7, QTableWidgetItem(p.etiqueta))
                wprod.tableWidgetProd.setItem(i, 8, QTableWidgetItem(str(p.cantvendida)))
                wprod.tableWidgetProd.setItem(i, 9, QTableWidgetItem(str(p.idv)))
        QMessageBox.information(wprod, 'Cargado', 'Los productos han sido cargados del archivo.')
    except FileNotFoundError:
        QMessageBox.warning(wprod, 'Error', 'No hay productos guardados.')

'''
CONTROL INTERFAZ DE USUARIOS
'''
def openUsuarios():
    # Configurar la tabla en la ventana de usuarios
    wus.tableWidgetUsu.setRowCount(len(ctrlus.listUsuarios()))
    wus.tableWidgetUsu.setColumnCount(4)
    wus.tableWidgetUsu.setHorizontalHeaderLabels(["id","nombre","login","contrasena"])

    # Mostrar la ventana de usuarios
    wus.show()
def insertarUsuario():
    # Obtener los datos del usuario desde los lineEdits
    idu = wus.lineEditIdu.text()
    nomu = wus.lineEditNomu.text()
    login = wus.lineEditLogin.text()
    contra = wus.lineEditContra.text()
    # Crea una variable de usuario y la agrega al controlador de usuarios
    u = Usuario(idu, nomu, login, contra)
    if ctrlus.insertaru(u):
        QMessageBox.information(wus, "Éxito", f"El usuario con ID {idu} ha sido insertado correctamente.")
        # Actualizar la tabla en la ventana de usuarios con los nuevos datos
        lstUs = ctrlus.listUsuarios()
        wus.tableWidgetUsu.setRowCount(len(lstUs))
        for i, u in enumerate(lstUs):
            wus.tableWidgetUsu.setItem(i, 0, QTableWidgetItem(u.idu))
            wus.tableWidgetUsu.setItem(i, 1, QTableWidgetItem(u.nombreu))
            wus.tableWidgetUsu.setItem(i, 2, QTableWidgetItem(u.login))
            wus.tableWidgetUsu.setItem(i, 3, QTableWidgetItem(u.contra))
    else:
        QMessageBox.information(wus, "Error", f"El usuario con ID {idu} ya existe, porfavor ingrese otro ID.")

def eliminarUsuario():
    idu = wus.lineEditIdu.text()
    usuario = ctrlus.getUsuario(idu)
    if usuario is not None:
        if ctrlus.eliminaru(usuario):
            # usuario eliminado correctamente
            QMessageBox.information(wus, "Éxito", f"El usuario con ID {idu} ha sido eliminado.")
            # Actualizar la tabla de usuarios
            lstUs = ctrlus.listUsuarios()
            wus.tableWidgetUsu.setRowCount(len(lstUs))
            for i, u in enumerate(lstUs):
                wus.tableWidgetUsu.setItem(i, 0, QTableWidgetItem(u.idu))
                wus.tableWidgetUsu.setItem(i, 1, QTableWidgetItem(u.nombreu))
                wus.tableWidgetUsu.setItem(i, 2, QTableWidgetItem(u.login))
                wus.tableWidgetUsu.setItem(i, 3, QTableWidgetItem(u.contra))
        else:
            # No se encontró el usuario con el ID especificado
            QMessageBox.warning(wus, "Error", f"No se elimino el usuario con el ID {idu}.")
    else:
        # No se encontró el usuario con el ID especificado
        QMessageBox.warning(wus, "Error", f"No se encontró un usuario con el ID {idu}.")

def actualizarUsuario():
    # Obtener el ID del usuario a actualizar
    idu = wus.lineEditIdu.text()
    # Obtener el usuario con ese ID
    usuario = ctrlus.getUsuario(idu)
    if usuario is not None:
        # Actualizar los datos del usuario con los valores de los QLineEdit correspondientes
        usuario.nombreu = wus.lineEditNomu.text()
        usuario.login = wus.lineEditLogin.text()
        usuario.contra = wus.lineEditContra.text()
        # Modificar el usuario en el diccionario de usuarios
        if ctrlus.modificaru(usuario):
            # usuario modificado correctamente
            QMessageBox.information(wus, "Éxito", f"El usaurio con ID {idu} ha sido actualizado.")
            # Actualizar la tabla de usuarios
            lstUs = ctrlus.listUsuarios()
            wus.tableWidgetUsu.setRowCount(len(lstUs))
            for i, u in enumerate(lstUs):
                wus.tableWidgetUsu.setItem(i, 0, QTableWidgetItem(u.idu))
                wus.tableWidgetUsu.setItem(i, 1, QTableWidgetItem(u.nombreu))
                wus.tableWidgetUsu.setItem(i, 2, QTableWidgetItem(u.login))
                wus.tableWidgetUsu.setItem(i, 3, QTableWidgetItem(u.contra))
        else:
            QMessageBox.information(wus, "Error", f"El usaurio con ID {idu} no ha sido actualizado.")
    else:
        # No se encontró el usuario con el ID especificado
        QMessageBox.warning(wus, "Error", f"No se encontró un usuario con el ID {idu}.")

def GuardarUsuarios():
    ruta_archivo = 'usuarios.txt'
    try:
        with open(ruta_archivo, 'w') as archivo:
            num_filas = wus.tableWidgetUsu.rowCount()
            num_columnas = wus.tableWidgetUsu.columnCount()
            # Escribir encabezados
            #headers = [wus.tableWidgetUsu.horizontalHeaderItem(i).text() for i in range(num_columnas)]
            #archivo.write('\t'.join(headers) + '\n')
            # Escribir datos de usuarios
            for i in range(num_filas):
                datos_fila = []
                for j in range(num_columnas):
                    datos_fila.append(wus.tableWidgetUsu.item(i, j).text())
                archivo.write('\t'.join(datos_fila) + '\n')
        QMessageBox.information(wus, 'Guardado', 'Los usuarios han sido guardados en el archivo.')
    except IOError:
        QMessageBox.warning(wus, 'Error', 'No se pudo guardar los usuarios en el archivo.')


def CargarUsuarios():
    ruta_archivo = 'usuarios.txt'
    try:
        with open(ruta_archivo, 'r') as archivo:
            # Leer datos línea por línea
            lineas = archivo.readlines()
            for linea in lineas:
                # Separar datos por el separador
                datos = linea.strip().split('\t')
                # Crear objeto Usuario y agregarlo al controlador de usuarios
                u = Usuario(datos[0], datos[1], datos[2], datos[3])
                ctrlus.insertaru(u)
            # Obtener lista actualizada de usuarios y establecer el número de filas del tableWidgetUsu
            lstUs = ctrlus.listUsuarios()
            wus.tableWidgetUsu.setRowCount(len(lstUs))
            # Establecer datos de usuarios en el tableWidgetUsu
            for i, u in enumerate(lstUs):
                wus.tableWidgetUsu.setItem(i, 0, QTableWidgetItem(u.idu))
                wus.tableWidgetUsu.setItem(i, 1, QTableWidgetItem(u.nombreu))
                wus.tableWidgetUsu.setItem(i, 2, QTableWidgetItem(u.login))
                wus.tableWidgetUsu.setItem(i, 3, QTableWidgetItem(u.contra))
        QMessageBox.information(wus, 'Cargado', 'Los usuarios han sido cargados del archivo.')
    except FileNotFoundError:
        QMessageBox.warning(wus, 'Error', 'No hay usuarios guardados.')

"""
CONTROL DE USUARIOS LOGUEADOS
"""
def OpenloginUsuario():
    wlog.show()

def LoginUsuario():
    idu = wlog.lineEditIdu.text()
    contra = wlog.lineEditContra.text()
    usuario = ctrlus.getUsuario(idu)
    if usuario is not None :
        us=ctrlus.verificarUsuario(idu, contra)
        if us is not None:
            QMessageBox.information(wlog, "Exito", f"El usaurio con ID {idu} ha sido logueado.")
            wuslog.tableWidgetuslog.setRowCount(len(ctrlpro.listProducto()))
            wuslog.tableWidgetuslog.setColumnCount(10)
            wuslog.tableWidgetuslog.setHorizontalHeaderLabels(
                ["id", "nombre", "descripcion", "precio", "descuento", "precio con descuento", "disponoble", "etiqueta",
                 "vendidos","ID vendedor"])
            lstProd = ctrlpro.listProducto()
            wuslog.tableWidgetuslog.setRowCount(len(lstProd))
            for i, p in enumerate(lstProd):
                wuslog.tableWidgetuslog.setItem(i, 0, QTableWidgetItem(p.idprod))
                wuslog.tableWidgetuslog.setItem(i, 1, QTableWidgetItem(p.nombrep))
                wuslog.tableWidgetuslog.setItem(i, 2, QTableWidgetItem(p.descripcion))
                wuslog.tableWidgetuslog.setItem(i, 3, QTableWidgetItem(str(p.prcio)))
                wuslog.tableWidgetuslog.setItem(i, 4, QTableWidgetItem(p.descuento))
                wuslog.tableWidgetuslog.setItem(i, 5, QTableWidgetItem(str(p.preciodescu)))
                wuslog.tableWidgetuslog.setItem(i, 6, QTableWidgetItem(str(p.cantdisponible)))
                wuslog.tableWidgetuslog.setItem(i, 7, QTableWidgetItem(p.etiqueta))
                wuslog.tableWidgetuslog.setItem(i, 8, QTableWidgetItem(str(p.cantvendida)))
                wuslog.tableWidgetuslog.setItem(i, 9, QTableWidgetItem(str(p.idv)))
            wuslog.show()
        else:
            QMessageBox.information(wlog, "Error", f"El usaurio con ID {idu} no ha sido logueado, verifique su contrasena")
    else:
        QMessageBox.information(wlog, "Error", f"El usaurio con ID {idu} no existe.")

def BuscarProducto():
    # Obtener el nombre ingresado en el QLineEdit
    nombrep = wuslog.lineEditNomp.text()

    # Buscar los productos con ese nombre utilizando el método buscarp
    productos_encontrados = ctrlpro.buscarp(nombrep)

    # Si se encuentran productos, agregarlos a la tabla
    if productos_encontrados is not None:
        wuslog.tableWidgetuslog.setRowCount(0)
        # Configurar el número de filas de la tabla
        wuslog.tableWidgetuslog.setRowCount(len(productos_encontrados))

        # Agregar los productos a la tabla
        for i, producto in enumerate(productos_encontrados):
            wuslog.tableWidgetuslog.setItem(i, 0, QtWidgets.QTableWidgetItem(producto.idprod))
            wuslog.tableWidgetuslog.setItem(i, 1, QtWidgets.QTableWidgetItem(producto.nombrep))
            wuslog.tableWidgetuslog.setItem(i, 2, QtWidgets.QTableWidgetItem(producto.descripcion))
            wuslog.tableWidgetuslog.setItem(i, 3, QtWidgets.QTableWidgetItem(str(producto.prcio)))
            wuslog.tableWidgetuslog.setItem(i, 4, QtWidgets.QTableWidgetItem(producto.descuento))
            wuslog.tableWidgetuslog.setItem(i, 5, QtWidgets.QTableWidgetItem(str(producto.preciodescu)))
            wuslog.tableWidgetuslog.setItem(i, 6, QtWidgets.QTableWidgetItem(producto.cantdisponible))
            wuslog.tableWidgetuslog.setItem(i, 7, QtWidgets.QTableWidgetItem(producto.etiqueta))
            wuslog.tableWidgetuslog.setItem(i, 8, QtWidgets.QTableWidgetItem(str(producto.cantvendida)))
            wuslog.tableWidgetuslog.setItem(i, 9, QtWidgets.QTableWidgetItem(str(producto.idv)))

    else:
        QMessageBox.information(wuslog, "Error", f"El producto no existe ")

def comprar():
    idp = wuslog.lineEditIdp.text()
    idv = wuslog.lineEditIdv.text()
    p = ctrlpro.getProducto(idp)
    v = ctrlven.getVendedor(idv)

    if p is not None:
        if int(p.cantdisponible) >0:
            v.cantVent += 1
            p.cantvendida +=1
            p.cantdisponible -=1
            wuslog.tableWidgetuslog.setRowCount(0)
            lstProd = ctrlpro.listProducto()
            wuslog.tableWidgetuslog.setRowCount(len(lstProd))
            for i, p in enumerate(lstProd):
                wuslog.tableWidgetuslog.setItem(i, 0, QTableWidgetItem(p.idprod))
                wuslog.tableWidgetuslog.setItem(i, 1, QTableWidgetItem(p.nombrep))
                wuslog.tableWidgetuslog.setItem(i, 2, QTableWidgetItem(p.descripcion))
                wuslog.tableWidgetuslog.setItem(i, 3, QTableWidgetItem(str(p.prcio)))
                wuslog.tableWidgetuslog.setItem(i, 4, QTableWidgetItem(p.descuento))
                wuslog.tableWidgetuslog.setItem(i, 5, QTableWidgetItem(str(p.preciodescu)))
                wuslog.tableWidgetuslog.setItem(i, 6, QTableWidgetItem(str(p.cantdisponible)))
                wuslog.tableWidgetuslog.setItem(i, 7, QTableWidgetItem(p.etiqueta))
                wuslog.tableWidgetuslog.setItem(i, 8, QTableWidgetItem(str(p.cantvendida)))
                wuslog.tableWidgetuslog.setItem(i, 9, QTableWidgetItem(str(p.idv)))

            QMessageBox.information(wuslog, "Exito", f"has comprado {p.nombrep}")
        else:
            QMessageBox.information(wuslog, "Error", f"producto agotado ")

    else:
        QMessageBox.information(wuslog, "Error", f"El producto no existe ")
def Vervendedores():
    wuslog.tableWidgetuslog.setRowCount(0)
    wuslog.tableWidgetuslog.setHorizontalHeaderLabels(
        ["id", "nombre", "fe inicio", "cant.ventas", "ubicacion", "telefono", "contrasena"])
    lstVens = ctrlven.listVendedor()
    wuslog.tableWidgetuslog.setRowCount(len(lstVens))
    for i, v in enumerate(lstVens):
        wuslog.tableWidgetuslog.setItem(i, 0, QTableWidgetItem(v.idvend))
        wuslog.tableWidgetuslog.setItem(i, 1, QTableWidgetItem(v.nombre))
        wuslog.tableWidgetuslog.setItem(i, 2, QTableWidgetItem(v.feincrip.strftime('%Y/%m/%d')))
        wuslog.tableWidgetuslog.setItem(i, 3, QTableWidgetItem(str(v.cantVent)))
        wuslog.tableWidgetuslog.setItem(i, 4, QTableWidgetItem(v.ubi))
        wuslog.tableWidgetuslog.setItem(i, 5, QTableWidgetItem(v.tel))
        wuslog.tableWidgetuslog.setItem(i, 6, QTableWidgetItem(v.cont))
def Verproductos():
    wuslog.tableWidgetuslog.setRowCount(0)
    wuslog.tableWidgetuslog.setHorizontalHeaderLabels(
        ["id", "nombre", "descripcion", "precio", "descuento", "precio con descuento", "disponoble", "etiqueta",
         "vendidos","ID vendedor"])
    lstProd = ctrlpro.listProducto()
    wuslog.tableWidgetuslog.setRowCount(len(lstProd))
    for i, p in enumerate(lstProd):
        wuslog.tableWidgetuslog.setItem(i, 0, QTableWidgetItem(p.idprod))
        wuslog.tableWidgetuslog.setItem(i, 1, QTableWidgetItem(p.nombrep))
        wuslog.tableWidgetuslog.setItem(i, 2, QTableWidgetItem(p.descripcion))
        wuslog.tableWidgetuslog.setItem(i, 3, QTableWidgetItem(str(p.prcio)))
        wuslog.tableWidgetuslog.setItem(i, 4, QTableWidgetItem(p.descuento))
        wuslog.tableWidgetuslog.setItem(i, 5, QTableWidgetItem(str(p.preciodescu)))
        wuslog.tableWidgetuslog.setItem(i, 6, QTableWidgetItem(str(p.cantdisponible)))
        wuslog.tableWidgetuslog.setItem(i, 7, QTableWidgetItem(p.etiqueta))
        wuslog.tableWidgetuslog.setItem(i, 8, QTableWidgetItem(str(p.cantvendida)))
        wuslog.tableWidgetuslog.setItem(i, 9, QTableWidgetItem(str(p.idv)))

'''
CONTROL DE BOTONES VENDEDOR
'''
# Conecta el botón de actualización con el método actualizarVendedor
wvend.pushButtonActualizar.clicked.connect(actualizarVendedor)
# Conecta el botón de eliminación con el método eliminarVendedor
wvend.pushButtonEliminar.clicked.connect(eliminarVendedor)
# Conectar el botón "Insertar" en la ventana de vendedores a la función insertarVendedor
wvend.pushButtonInsertar.clicked.connect(insertarVendedor)
# Conecta el botón de guardado de vendedores  con el método GuardarVendedores
wvend.pushButtonGuardarV.clicked.connect(GuardarVendedores)
# Conecta el botón de carga de vendedores  con el método CargarVendedores
wvend.pushButtonCargarV.clicked.connect(CargarVendedores)
'''
CONTROL DE BOTONES PRODUCTOS
'''
# Conecta el botón de actualización con el método actualizarVendedor
wprod.pushButtonActualizarp.clicked.connect(actualizarProducto)
# Conecta el botón de eliminación con el método eliminarVendedor
wprod.pushButtonEliminarp.clicked.connect(eliminarProducto)
# Conecta el botón "Insertar" en la ventana de productos a la función insertarProducto
wprod.pushButtonInsertarp.clicked.connect(insertarProducto)
# Conecta el botón de guardado de productos  con el método GuardarPrductos
wprod.pushButtonGuardarP.clicked.connect(GuardarProductos)
# Conecta el botón de carga de productos  con el método CargarProductos
wprod.pushButtonCargarP.clicked.connect(CargarProductos)

'''
CONTROL DE BOTONES DE USUARIOS
'''
# Conecta el botón "Insertar" en la ventana de usuarios a la función insertarUsuario
wus.pushButtonInsertaru.clicked.connect(insertarUsuario)
# Conecta el botón de eliminación con el método eliminarUsuario
wus.pushButtonEliminaru.clicked.connect(eliminarUsuario)
# Conecta el botón de actualización con el método actualizarUsuario
wus.pushButtonActualizaru.clicked.connect(actualizarUsuario)
# Conecta el botón de guardado de usuarios  con el método GuardaUsuarios
wus.pushButtonGuardarU.clicked.connect(GuardarUsuarios)
# Conecta el botón de carga de usuarios  con el método CargarUsuarios
wus.pushButtonCargarU.clicked.connect(CargarUsuarios)
'''
CONTROL DE BOTONES USUARIOS LOGUEADOS
'''
#Conecta el botón "LOGIN" en la ventana LoginUsuario a la funcion LoginUsuario
wlog.pushButtonLog.clicked.connect(LoginUsuario)
#Conecta el botón de buscar  en la ventana LoginUsuario a la funcion BuscarProducto
wuslog.pushButtonBuscarp.clicked.connect(BuscarProducto)
#Conecta el botón de comprar  en la ventana LoginUsuario a la funcion Comprar
wuslog.pushButtonComp.clicked.connect(comprar)
#Conecta el botón de productos  en la ventana LoginUsuario a la funcion Vervendedores
wuslog.pushButtonVerv.clicked.connect(Vervendedores)
#Conecta el botón de vendedores  en la ventana LoginUsuario a la funcion Verproductos
wuslog.pushButtonVerp.clicked.connect(Verproductos)


'''
CONTROL DE BOTONES PAGINA PRINCIPAL
'''
# Conecta el botón "Vendedores" en la ventana principal a la función openVendedores
ppal.pushButtonVendors.clicked.connect(openVendedores)
# Conectar el botón "productos" en la ventana principal a la función openProductos
ppal.pushButtonProductos.clicked.connect(openProductos)
# Conectar el botón "usuarios" en la ventana principal a la función openUsuarios
ppal.pushButtonUsuarios.clicked.connect(openUsuarios)
# Conectar el botón "login usuario" en la ventana principal a la funcion OpenloginUsuairos
ppal.pushButtonLogU.clicked.connect(OpenloginUsuario)
# Mostrar la ventana principal
ppal.show()
app.exec()