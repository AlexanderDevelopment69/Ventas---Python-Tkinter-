import tkinter as tk
from Productos.gui_productos import Frame,barra_menu




def main():
    root=tk.Tk()

    root.title('Zapateria Rojas')
    root.resizable(0,0)
    barra_menu(root)
    app=Frame(root=root)
    root.eval('tk::PlaceWindow . center')
    root.mainloop()


if __name__=='__main__':
    main()


