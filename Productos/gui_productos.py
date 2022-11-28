import tkinter as tk
from tkinter import ttk, messagebox
from Model.productos_dao import crear_tabla, borrar_tabla,crear_tablaCompra,crear_tablaVenta
from Model.productos_dao import Producto, guardar, listar, eliminar

from Productos.gui_inventario import FrameInventario
from Productos.gui_agregarStock import FrameStock
from Productos.gui_compras import FrameCompras
from Productos.gui_nueva_venta import FrameNuevaVenta
from Productos.gui_ventas import FrameVenta


def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)
    menu_inicio.add_command(label="Registrar Productos")
    menu_inicio.add_command(label="Ver stock productos", command=inventario)
    menu_inicio.add_command(label="Agregar stock ", command=agregarStock)
    menu_inicio.add_command(label="Salir", command=root.destroy)

    menu_Venta = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Venta', menu=menu_Venta)
    menu_Venta.add_command(label="Registar Venta",command=nuevaVenta)
    menu_Venta.add_command(label="Ver Ventas", command=venta)

    menu_Inventario = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inventario', menu=menu_Inventario)
    menu_Inventario.add_command(label="Ver compras",command=compras)

    menu_configuracion = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Configuracion', menu=menu_configuracion)
    menu_configuracion.add_command(label="Crear tabla producto", command=crear_tabla)
    menu_configuracion.add_command(label="Crear tabla compra", command=crear_tablaCompra)
    menu_configuracion.add_command(label="Crear tabla venta", command=crear_tablaVenta)
    menu_configuracion.add_command(label="Eliminar tablas", command=borrar_tabla)


class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.pack()
        # self.config(bg='green')
        self.campos_Producto()
        self.desabilitar_campos()
        self.tabla_productos()

    def campos_Producto(self):
        self.label_codigo = tk.Label(self, text='Registro de Productos ')
        self.label_codigo.config(font=('Segoe UI Light', 13))
        self.label_codigo.grid(row=0, column=0, padx=10, pady=10)

        self.label_codigo = tk.Label(self, text='Codigo: ')
        self.label_codigo.config(font=('Segoe UI Light', 10))
        self.label_codigo.grid(row=1, column=0, padx=10, pady=10)

        self.label_modelo = tk.Label(self, text='Modelo: ')
        self.label_modelo.config(font=('Segoe UI Light', 10))
        self.label_modelo.grid(row=2, column=0, padx=10, pady=10)

        self.label_talla = tk.Label(self, text='Talla: ')
        self.label_talla.config(font=('Segoe UI Light', 10))
        self.label_talla.grid(row=3, column=0, padx=10, pady=10)

        self.label_cantidad = tk.Label(self, text='Cantidad: ')
        self.label_cantidad.config(font=('Segoe UI Light', 10))
        self.label_cantidad.grid(row=4, column=0, padx=10, pady=10)

        self.label_color = tk.Label(self, text='Color: ')
        self.label_color.config(font=('Segoe UI Light', 10))
        self.label_color.grid(row=5, column=0, padx=10, pady=10)

        self.label_presentacion = tk.Label(self, text='Presentacion: ')
        self.label_presentacion.config(font=('Segoe UI Light', 10))
        self.label_presentacion.grid(row=6, column=0, padx=10, pady=10)

        self.label_costo = tk.Label(self, text='Costo: ')
        self.label_costo.config(font=('Segoe UI Light', 10))
        self.label_costo.grid(row=7, column=0, padx=10, pady=10)

        self.label_precio = tk.Label(self, text='Precio: ')
        self.label_precio.config(font=('Segoe UI Light', 10))
        self.label_precio.grid(row=8, column=0, padx=10, pady=10)

        self.mi_codigo = tk.StringVar()
        self.entry_codigo = tk.Entry(self, textvariable=self.mi_codigo)
        self.entry_codigo.config(
            width=50, state='disabled', font=('Segoe UI Light', 10))
        self.entry_codigo.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        self.mi_modelo = tk.StringVar()
        self.entry_modelo = tk.Entry(self, textvariable=self.mi_modelo)
        self.entry_modelo.config(
            width=50, state='disabled', font=('Segoe UI Light', 10))
        self.entry_modelo.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        self.mi_talla = tk.StringVar()
        self.entry_talla = tk.Entry(self, textvariable=self.mi_talla)
        self.entry_talla.config(
            width=50, state='disabled', font=('Segoe UI Light', 10))
        self.entry_talla.grid(row=3, column=1, padx=10, pady=10, columnspan=2)

        self.mi_cantidad = tk.StringVar()
        self.entry_cantidad = tk.Entry(self, textvariable=self.mi_cantidad)
        self.entry_cantidad.config(
            width=50, state='disabled', font=('Segoe UI Light', 10))
        self.entry_cantidad.grid(row=4, column=1, padx=10, pady=10, columnspan=2)

        self.mi_color = tk.StringVar()
        self.entry_color = tk.Entry(self, textvariable=self.mi_color)
        self.entry_color.config(
            width=50, state='disabled', font=('Segoe UI Light', 10))
        self.entry_color.grid(row=5, column=1, padx=10, pady=10, columnspan=2)

        self.mi_presentacion = tk.StringVar()
        self.entry_presentacion = tk.Entry(self, textvariable=self.mi_presentacion)
        self.entry_presentacion.config(
            width=50, state='disabled', font=('Segoe UI Light', 10))
        self.entry_presentacion.grid(row=6, column=1, padx=10, pady=10, columnspan=2)

        self.mi_costo = tk.StringVar()
        self.entry_costo = tk.Entry(self, textvariable=self.mi_costo)
        self.entry_costo.config(
            width=50, state='disabled', font=('Segoe UI Light', 10))
        self.entry_costo.grid(row=7, column=1, padx=10, pady=10, columnspan=2)

        self.mi_precio = tk.StringVar()
        self.entry_precio = tk.Entry(self, textvariable=self.mi_precio)
        self.entry_precio.config(
            width=50, state='disabled', font=('Segoe UI Light', 10))
        self.entry_precio.grid(row=8, column=1, padx=10, pady=10, columnspan=2)

        self.boton_nuevo = tk.Button(self, text="Nuevo", command=self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Segoe UI Light', 10), fg="white", bg="#07439A", cursor='hand2',
                                activebackground='#07439A')
        self.boton_nuevo.grid(row=9, column=0, padx=10, pady=10)

        self.boton_guardar = tk.Button(self, text="Guardar", command=self.guardar_datos)
        self.boton_guardar.config(width=20, font=('Segoe UI Light', 10), fg="white", bg="#158645", cursor='hand2',
                                  activebackground='#158645')
        self.boton_guardar.grid(row=9, column=1, padx=10, pady=10)

        self.boton_candelar = tk.Button(self, text="Cancelar", command=self.desabilitar_campos)
        self.boton_candelar.config(width=20, font=('Segoe UI Light', 10), fg="white", bg="#767676", cursor='hand2',
                                   activebackground='#FF7C67')
        self.boton_candelar.grid(row=9, column=2, padx=10, pady=10)

    def habilitar_campos(self):
        self.entry_codigo.config(state='disable')
        self.entry_modelo.config(state='normal')
        self.entry_talla.config(state='normal')
        self.entry_cantidad.config(state='normal')
        self.entry_color.config(state='normal')
        self.entry_presentacion.config(state='normal')
        self.entry_costo.config(state='normal')
        self.entry_precio.config(state='normal')

        self.boton_guardar.config(state='normal')
        self.boton_candelar.config(state='normal')

    def desabilitar_campos(self):
        self.mi_codigo.set('')
        self.mi_modelo.set('')
        self.mi_talla.set('')
        self.mi_cantidad.set('')
        self.mi_color.set('')
        self.mi_presentacion.set('')
        self.mi_costo.set('')
        self.mi_precio.set('')

        self.entry_codigo.config(state='disabled')
        self.entry_modelo.config(state='disabled')
        self.entry_talla.config(state='disabled')
        self.entry_cantidad.config(state='disabled')
        self.entry_color.config(state='disabled')
        self.entry_presentacion.config(state='disabled')
        self.entry_costo.config(state='disabled')
        self.entry_precio.config(state='disabled')

        self.boton_guardar.config(state='disabled')
        self.boton_candelar.config(state='disabled')

    def guardar_datos(self):
        producto = Producto(
            self.mi_modelo.get(),
            self.mi_talla.get(),
            self.mi_cantidad.get(),
            self.mi_color.get(),
            self.mi_presentacion.get(),
            self.mi_costo.get(),
            self.mi_precio.get(),
        )

        guardar(producto)
        self.tabla_productos()

    def tabla_productos(self):
        # Recuperar productos
        self.lista_productos = listar()

        self.tabla = ttk.Treeview(self,
                                  column=('Modelo', 'Talla', 'Cantidad', 'Color', 'Presentacion', 'Costo', 'Precio'))
        self.tabla.grid(row=10, column=0, columnspan=3, sticky='nse')

        self.scroll = ttk.Scrollbar(self,
                                    orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=10, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='Codigo')
        self.tabla.heading('#1', text='Modelo')
        self.tabla.heading('#2', text='Talla')
        self.tabla.heading('#3', text='Cantidad')
        self.tabla.heading('#4', text='Color')
        self.tabla.heading('#5', text='Presentacion')
        self.tabla.heading('#6', text='Costo')
        self.tabla.heading('#7', text='Precio')

        self.tabla.column("#0", width=100)
        self.tabla.column("#1", width=100)
        self.tabla.column("#2", width=100)
        self.tabla.column("#3", width=100)
        self.tabla.column("#4", width=100)
        self.tabla.column("#5", width=100)
        self.tabla.column("#6", width=100)
        self.tabla.column("#7", width=100)

        # inserccion datos
        # self.tabla.insert('', 0, text='1', values=('Los vengadores', '22', 'accion'))

        # Iteracion de productos
        for p in self.lista_productos:
            self.tabla.insert('', 0, text=p[0],
                              values=(p[1], p[2], p[3], p[4], p[5], p[6], p[7])
                              )
        #
        # self.boton_buscar = tk.Button(self, text="Buscar")
        # self.boton_buscar.config(width=20, font=('Segoe UI Light', 10), fg="white", bg="#07439A", cursor='hand2',
        #                          activebackground='#07439A')
        # self.boton_buscar.grid(row=9, column=0, padx=10, pady=10)

        self.boton_eliminar = tk.Button(self, text="Eliminar", command=self.eliminar_datos)
        self.boton_eliminar.config(width=20, font=('Segoe UI Light', 10), fg="white", bg="#FF7C67", cursor='hand2',
                                   activebackground='#FF7C67')
        self.boton_eliminar.grid(row=11, column=1, padx=10, pady=10)

    def eliminar_datos(self):
        try:
            self.id_producto = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.id_producto)

            self.tabla_productos()

        except:
            titulo = 'Eliminar un registro'
            mensaje = 'No se han seleccionado ningun registro'
            messagebox.showwarning(titulo, mensaje)


def inventario():
    root = tk.Tk()
    root.title('Inventario')
    root.resizable(0, 0)
    app = FrameInventario(root=root)
    root.eval('tk::PlaceWindow . center')
    root.mainloop()


def venta():
    root = tk.Tk()
    root.title('Ventas')
    root.resizable(0, 0)
    app = FrameVenta(root=root)
    root.eval('tk::PlaceWindow . center')
    root.mainloop()


def nuevaVenta():
    root = tk.Tk()
    root.title('Nueva venta')
    root.resizable(0, 0)
    app = FrameNuevaVenta(root=root)
    root.eval('tk::PlaceWindow . center')
    root.mainloop()


def compras():
    root = tk.Tk()
    root.title('Compras')
    root.resizable(0, 0)
    app = FrameCompras(root=root)
    root.eval('tk::PlaceWindow . center')
    root.mainloop()


def agregarStock():
    root = tk.Tk()
    root.title('Ventas')

    root.resizable(0, 0)
    app = FrameStock(root=root)
    root.eval('tk::PlaceWindow . center')
    root.mainloop()



