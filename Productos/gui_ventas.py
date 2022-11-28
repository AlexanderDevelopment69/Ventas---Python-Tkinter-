import tkinter as tk
from tkinter import ttk, messagebox
from Model.productos_dao import crear_tabla, borrar_tabla
from Model.productos_dao import Producto, guardar, listar,eliminar,actualizarCantidad,listarVentas









class FrameVenta(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.pack()
        # self.config(bg='green')
        self.tabla_ventas()







    def tabla_ventas(self):
        # Recuperar productos
        self.lista_ventas = listarVentas()

        self.tabla = ttk.Treeview(self,
                                  column=(
                                       'Cliente', 'Producto', 'Cantidad', 'Total', 'Fecha'))
        self.tabla.grid(row=2, column=0, columnspan=3, sticky='nse')

        self.scroll = ttk.Scrollbar(self,
                                    orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=3, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='N venta')
        self.tabla.heading('#1', text='Cliente')
        self.tabla.heading('#2', text='Producto')
        self.tabla.heading('#3', text='Cantidad')
        self.tabla.heading('#4', text='Total')
        self.tabla.heading('#5', text='Fecha')


        self.tabla.column("#0", width=100)
        self.tabla.column("#1", width=100)
        self.tabla.column("#2", width=100)
        self.tabla.column("#3", width=100)
        self.tabla.column("#4", width=100)
        self.tabla.column("#5", width=100)


        # inserccion datos
        # self.tabla.insert('', 0, text='1', values=('Los vengadores', '22', 'accion'))

        # Iteracion de productos
        for p in self.lista_ventas:
            self.tabla.insert('', 0, text=p[0],
                              values=(p[1], p[2], p[3], p[4],p[5])
                              )
        #
        # self.boton_buscar = tk.Button(self, text="Buscar")
        # self.boton_buscar.config(width=20, font=('Segoe UI Light', 10), fg="white", bg="#07439A", cursor='hand2',
        #                          activebackground='#07439A')
        # self.boton_buscar.grid(row=9, column=0, padx=10, pady=10)


