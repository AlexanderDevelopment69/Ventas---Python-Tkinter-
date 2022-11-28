import tkinter as tk
from tkinter import ttk, messagebox
from Model.productos_dao import crear_tabla, borrar_tabla
from Model.productos_dao import Producto, guardar, listar, eliminar, actualizarCantidad


class FrameStock(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.pack()
        # self.config(bg='green')
        self.campos_stock()
        self.tabla_productos()

    def campos_stock(self):
        self.label_codigo = tk.Label(self, text='AUMENTAR STOCK DE PRODUCTOS: ')
        self.label_codigo.config(font=('Segoe UI Light', 14))
        self.label_codigo.grid(row=0, column=0, padx=10, pady=10)

        self.label_Cliente = tk.Label(self, text='Datos Proveedor: ')
        self.label_Cliente.config(font=('Segoe UI Light', 12))
        self.label_Cliente.grid(row=1, column=0, padx=10, pady=10)

        self.label_nombreCliente = tk.Label(self, text='Nombre: ')
        self.label_nombreCliente.config(font=('Segoe UI Light', 10))
        self.label_nombreCliente.grid(row=2, column=0, padx=10, pady=10)

        self.label_producto = tk.Label(self, text='Datos Producto: ')
        self.label_producto.config(font=('Segoe UI Light', 12))
        self.label_producto.grid(row=3, column=0, padx=10, pady=10)

        self.label_codigo = tk.Label(self, text='Codigo: ')
        self.label_codigo.config(font=('Segoe UI Light', 10))
        self.label_codigo.grid(row=4, column=0, padx=10, pady=10)

        self.label_cantidad = tk.Label(self, text='Cantidad: ')
        self.label_cantidad.config(font=('Segoe UI Light', 10))
        self.label_cantidad.grid(row=5, column=0, padx=10, pady=10)

        self.mi_nombreProveedor = tk.StringVar()
        self.entry_nombreProveedor = tk.Entry(self, textvariable=self.mi_nombreProveedor)
        self.entry_nombreProveedor.config(
            width=50, state='normal', font=('Segoe UI Light', 10))
        self.entry_nombreProveedor.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        self.mi_codigo = tk.StringVar()
        self.entry_codigo = tk.Entry(self, textvariable=self.mi_codigo)
        self.entry_codigo.config(
            width=50, state='normal', font=('Segoe UI Light', 10))
        self.entry_codigo.grid(row=4, column=1, padx=10, pady=10, columnspan=2)

        self.mi_cantidad = tk.StringVar()
        self.entry_cantidad = tk.Entry(self, textvariable=self.mi_cantidad)
        self.entry_cantidad.config(
            width=50, state='normal', font=('Segoe UI Light', 10))
        self.entry_cantidad.grid(row=5, column=1, padx=10, pady=10, columnspan=2)

        self.boton_nuevo = tk.Button(self, text="Aumentar stock", command=self.aumentarStock)
        self.boton_nuevo.config(width=20, font=('Segoe UI Light', 10), fg="white", bg="#07439A", cursor='hand2',
                                activebackground='#07439A')
        self.boton_nuevo.grid(row=7, column=0, padx=10, pady=10)

    def tabla_productos(self):
        # Recuperar productos
        self.lista_productos = listar()

        self.tabla = ttk.Treeview(self,
                                  column=(
                                      'Modelo', 'Talla', 'Cantidad', 'Color', 'Presentacion', 'Costo', 'Precio'))
        self.tabla.grid(row=8, column=0, columnspan=3, sticky='nse')

        self.scroll = ttk.Scrollbar(self,
                                    orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=8, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)


        self.tabla.heading('#0', text='Codigo')
        self.tabla.heading('#1', text='Modelo')
        self.tabla.heading('#2', text='Talla')
        self.tabla.heading('#3', text='Color')
        self.tabla.heading('#4', text='Presentacion')
        self.tabla.heading('#5', text='Costo')
        self.tabla.heading('#6', text='Precio')
        self.tabla.heading('#7', text='stock')

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
                              values=(p[1], p[2], p[4], p[5], p[6], p[7], p[3])
                              )
        #
        # self.boton_buscar = tk.Button(self, text="Buscar")
        # self.boton_buscar.config(width=20, font=('Segoe UI Light', 10), fg="white", bg="#07439A", cursor='hand2',
        #                          activebackground='#07439A')
        # self.boton_buscar.grid(row=9, column=0, padx=10, pady=10)


    def aumentarStock(self):
        actualizarCantidad(self.entry_codigo.get(),self.entry_cantidad.get(),self.entry_nombreProveedor.get())
        self.tabla_productos()


