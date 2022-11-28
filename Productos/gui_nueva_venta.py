import tkinter as tk
from tkinter import ttk, messagebox
from Model.productos_dao import crear_tabla, borrar_tabla
from Model.productos_dao import Producto, guardar, listar,eliminar,nuevaVenta





class FrameNuevaVenta(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.pack()
        # self.config(bg='green')
        self.campos_Venta()



    def campos_Venta(self):
        self.label_codigo = tk.Label(self, text='REGISTRAR VENTAS: ')
        self.label_codigo.config(font=('Segoe UI Light', 14))
        self.label_codigo.grid(row=0, column=0, padx=10, pady=10)



        self.label_Cliente = tk.Label(self, text='Datos Cliente: ')
        self.label_Cliente.config(font=('Segoe UI Light', 12))
        self.label_Cliente.grid(row=1, column=0, padx=10, pady=10)


        self.label_nombreCliente = tk.Label(self, text='Nombres: ')
        self.label_nombreCliente.config(font=('Segoe UI Light', 10))
        self.label_nombreCliente.grid(row=2, column=0, padx=10, pady=10)


        self.label_producto = tk.Label(self, text='Datos Producto: ')
        self.label_producto.config(font=('Segoe UI Light', 12))
        self.label_producto.grid(row=3, column=0, padx=10, pady=10)

        self.label_codigo = tk.Label(self, text='Codigo: ')
        self.label_codigo.config(font=('Segoe UI Light', 10))
        self.label_codigo.grid(row=4, column=0, padx=10, pady=10)


        self.label_cantidad = tk.Label(self, text='Cantidad: ')
        self.label_cantidad .config(font=('Segoe UI Light', 10))
        self.label_cantidad .grid(row=5, column=0, padx=10, pady=10)




        self.mi_nombreCliente = tk.StringVar()
        self.entry_nombreCliente  = tk.Entry(self, textvariable=self.mi_nombreCliente)
        self.entry_nombreCliente .config(
            width=50, state='disabled', font=('Segoe UI Light', 10))
        self.entry_nombreCliente .grid(row=2, column=1, padx=10, pady=10, columnspan=2)


        self.mi_codigo = tk.StringVar()
        self.entry_codigo = tk.Entry(self, textvariable=self.mi_codigo)
        self.entry_codigo.config(
            width=50, state='disabled', font=('Segoe UI Light', 10))
        self.entry_codigo.grid(row=4, column=1, padx=10, pady=10, columnspan=2)


        self.mi_cantidad = tk.StringVar()
        self.entry_cantidad = tk.Entry(self, textvariable=self.mi_cantidad)
        self.entry_cantidad.config(
            width=50, state='disabled', font=('Segoe UI Light', 10))
        self.entry_cantidad.grid(row=5, column=1, padx=10, pady=10, columnspan=2)

        self.entry_nombreCliente.config(state='normal')
        self.entry_codigo.config(state='normal')
        self.entry_cantidad.config(state='normal')


        self.boton_nuevo = tk.Button(self, text="Registrar Venta",command=self.generarVenta)
        self.boton_nuevo.config(width=20, font=('Segoe UI Light', 10), fg="white", bg="#07439A", cursor='hand2',
                                activebackground='#07439A')
        self.boton_nuevo.grid(row=7, column=0, padx=10, pady=10)


    def generarVenta(self):
        nuevaVenta(self.entry_nombreCliente.get(),self.entry_codigo.get(),self.entry_cantidad.get())




