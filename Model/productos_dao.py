from tkinter import messagebox

from .conexion_db import ConexionDB


def crear_tabla():
    conexion = ConexionDB()

    sql = '''
    CREATE TABLE productos(
        id INTEGER,
        modelo VARCHAR(100),
        talla VARCHAR(20),
        cantidad INTEGER,
        color VARCHAR(20),
        presentacion varchar(60),
        costo DECIMAL(4,2),
        precio DECIMAL(4,2),
        PRIMARY KEY(id AUTOINCREMENT)
        )
        '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Crear Registro'
        mensaje = 'Se creo en la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'La tabla ya esta creada'
        messagebox.showinfo(titulo, mensaje)


def crear_tablaCompra():
    conexion = ConexionDB()

    sql = '''
    CREATE TABLE compra(
        id INTEGER,
        nombre_proveedor VARCHAR(100),
        id_producto INTEGER,
        cantidad INTEGER,
        fecha TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY(id AUTOINCREMENT)
        FOREIGN KEY (id_producto) REFERENCES producto(id)
        )
        '''

    conexion.cursor.execute(sql)
    conexion.cerrar()


def crear_tablaVenta():
    conexion = ConexionDB()

    sql = '''
    CREATE TABLE venta(
        id INTEGER,
        nombre_cliente VARCHAR(100),
        id_producto INTEGER,
        cantidad INTEGER,
        total DECIMAL(5,2),
        fecha TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY(id AUTOINCREMENT)
        FOREIGN KEY (id_producto) REFERENCES producto(id)
        )
        '''

    conexion.cursor.execute(sql)
    conexion.cerrar()


def borrar_tabla():
    conexion = ConexionDB()
    sql = 'DROP TABLE IF EXISTS productos,compra,venta'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar Tabla'
        mensaje = 'La tabla de base de datos se borro con exito'
        messagebox.showinfo(titulo, mensaje)

    except:

        titulo = 'Borrar Tabla'
        mensaje = 'No hay tabla para borrar'
        messagebox.showwarning(titulo, mensaje)


class Producto:
    def __init__(self, modelo, talla, cantidad, color, presentacion, costo, precio):
        self.codigo = None
        self.modelo = modelo
        self.talla = talla
        self.cantidad = cantidad
        self.color = color
        self.presentacion = presentacion
        self.costo = costo
        self.precio = precio

    def __str__(self):
        return f'Producto[{self.modelo},{self.talla},{self.cantidad},{self.color},{self.presentacion},{self.costo},{self.precio}]'


def guardar(producto):
    conexion = ConexionDB()

    sql = f'''INSERT INTO productos(modelo,talla,cantidad,color,presentacion,costo,precio) VALUES 
            ('{producto.modelo}','{producto.talla}',{producto.cantidad},'{producto.color}','{producto.presentacion}',{producto.costo},{producto.precio})
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Conexion registro'
        mensaje = 'Tabla producto no creada'
        messagebox.showerror(titulo, mensaje)


def listar():
    conexion = ConexionDB()
    lista_productos = []
    sql = 'SELECT * FROM productos order by id desc'

    try:
        conexion.cursor.execute(sql)
        lista_productos = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion registro'
        mensaje = 'No se listo'
        messagebox.showwarning(titulo, mensaje)

    return lista_productos


def eliminar(id_producto):
    conexion = ConexionDB()

    sql = f'DELETE FROM productos WHERE id={id_producto}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Eliminar datos'
        mensaje = 'Eliminado correctamente'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Eliminar datos'
        mensaje = 'No se puedo eliminar el registro'
        messagebox.showwarning(titulo, mensaje)


def actualizarCantidad(id_producto, cantidad, nombre_proveedor):
    conexion = ConexionDB()

    sql = f'UPDATE productos set cantidad=cantidad+{cantidad} WHERE id={id_producto}'
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Actualizar Stock'
        mensaje = 'Exito'

        # messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Actualizar Stock'
        mensaje = 'No se puedo aumentar el stock'
        # messagebox.showwarning(titulo, mensaje)

    conexion = ConexionDB()
    sql2 = f'''INSERT INTO compra(nombre_proveedor,id_producto,cantidad)VALUES
        ('{nombre_proveedor}', '{id_producto}', '{cantidad}')'''
    try:
        conexion.cursor.execute(sql2)
        conexion.cerrar()
        titulo = 'Actualizar Stock'
        mensaje = 'Exito'
    except:
        titulo = 'Actualizar Stock'
        mensaje = 'No se puedo aumentar el stock'


def listarCompras():
    conexion = ConexionDB()
    lista_productos = []
    sql = 'SELECT compra.id, compra.nombre_proveedor, productos.modelo, compra.cantidad,compra.fecha from compra inner join productos on productos.id=compra.id_producto order by compra.id desc'

    try:
        conexion.cursor.execute(sql)
        lista_productos = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion registro'
        mensaje = 'No se listo'
        messagebox.showwarning(titulo, mensaje)

    return lista_productos


def nuevaVenta(nombre_Cliente, id_producto, cantidad):
    conexion = ConexionDB()
    total = 0
    sql = f'SELECT productos.precio  FROM productos  WHERE id={id_producto}'

    try:
        conexion.cursor.execute(sql)
        precio = conexion.cursor.fetchone()
        for p in precio:
            total = p * int(cantidad)
        conexion.cerrar()
        titulo = 'Consulta producto'
        mensaje = 'Exito'
    except:
        titulo = 'Consulta producto'
        mensaje = 'Error'

    conexion = ConexionDB()
    sql = f'''INSERT INTO venta(nombre_cliente,id_producto,cantidad,total) VALUES
                ('{nombre_Cliente}','{id_producto}','{cantidad}','{total}')
        '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Nueva venta'
        mensaje = 'Exito'

        # messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Nueva venta'
        mensaje = 'Error venta'
        # messagebox.showwarning(titulo, mensaje)

    conexion = ConexionDB()

    sql = f'UPDATE productos set cantidad=cantidad-{cantidad} WHERE id={id_producto}'
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Nueva venta'
        mensaje = 'Exito'

        # messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Nueva venta'
        mensaje = 'Error venta'
        # messagebox.showwarning(titulo, mensaje)


def listarVentas():
    conexion = ConexionDB()
    lista_ventas = []
    sql = 'SELECT venta.id, venta.nombre_cliente, productos.modelo, venta.cantidad,venta.total,venta.fecha from venta inner join productos on productos.id= venta.id_producto order by venta.id desc'

    try:
        conexion.cursor.execute(sql)
        lista_ventas = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion registro'
        mensaje = 'No se listo'
        messagebox.showwarning(titulo, mensaje)

    return lista_ventas
