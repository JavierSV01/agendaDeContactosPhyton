import pickle
import  tkinter
from tkinter import ttk, messagebox


class Contacto:

    def __init__(self, nombre, tlf):
        self.nombre = nombre
        self.tlf = tlf

if __name__ == '__main__':
    listaContactos = []


    ventana = tkinter.Tk()
    ventana.geometry("415x400")

    lbInicio = tkinter.Label(ventana, text = "Agenda de contactos")
    lbInicio.grid(row = 0, column = 1)

    lbNombre = tkinter.Label(ventana, text = "Nombre")
    lbNombre.grid(row = 1, column = 0)

    txNombre = tkinter.Entry(ventana)
    txNombre.grid(row = 1, column = 1)

    lbTelefono = tkinter.Label(ventana, text="Telefono")
    lbTelefono.grid(row = 2, column = 0)

    txTelefono = tkinter.Entry(ventana)
    txTelefono.grid(row = 2, column = 1)

    tabla = ttk.Treeview()
    tabla.grid(row=4, column=0, columnspan=3, ipadx=100)

    tabla["columns"] = ("1", "2")

    tabla.column("#0", width = 0)
    tabla.column("1", width=100, minwidth=100)
    tabla.column("2", width=100, minwidth=100)
    tabla.heading("1", text = "Nombre")
    tabla.heading("2", text = "Telefono")


    #fichero = open("ficheroContactos", "wb")
    #pickle.dump(listaContactos, fichero)
    #fichero.close()
    fichero1 = open("ficheroContactos", "ab+")
    fichero1.seek(0)
    try:
        listaContactos = pickle.load(fichero1)
    except:
        print("El fichero est vacio")
    finally:
        fichero1.close()
    for i in range(0, len(listaContactos)):
        a: Contacto = listaContactos[i]
        tabla.insert("", i, i, text="", values=(a.nombre, a.tlf))


    def añadir():
        nombre = txNombre.get()
        telefono = txTelefono.get()
        a:Contacto = Contacto(nombre, telefono)
        aux:Contacto = Contacto("null", "null")

        if (nombre != "" and telefono != ""):

            for i in range (0, len(listaContactos)):
                if(listaContactos[i].nombre == nombre):
                    aux:Contacto = listaContactos[i]


            if (aux.nombre != nombre or len(listaContactos) == 0):

                for i in tabla.get_children():
                    tabla.delete(i)

                listaContactos.append(a)

                for i in range (0, len(listaContactos)):
                    a:Contacto = listaContactos[i]
                    tabla.insert("", i, i, text = "", values = (a.nombre, a.tlf))
            else:
                messagebox.showinfo(title="Informacion", message="Ya existe ese contacto")

        else:
            messagebox.showinfo(title="Informacion", message="Introduce todos los datos")

    btAñadir = tkinter.Button(ventana, text = "Añadir", command = añadir)
    btAñadir.grid(row = 3, column = 0)

    def modificar():
        nombre = txNombre.get()
        telefono = txTelefono.get()
        a: Contacto = Contacto(nombre, telefono)
        aux: Contacto = Contacto("null", "null")

        if (nombre != "" and telefono != ""):

            for i in range(0, len(listaContactos)):
                if (listaContactos[i].nombre == nombre):
                    listaContactos[i].tlf = telefono
                    listaContactos[i].nombre = nombre
                    aux: Contacto = listaContactos[i]

            if (aux.nombre == nombre):

                for i in tabla.get_children():
                    tabla.delete(i)



                for i in range(0, len(listaContactos)):
                    a: Contacto = listaContactos[i]
                    tabla.insert("", i, i, text="", values=(a.nombre, a.tlf))
            else:
                messagebox.showinfo(title="Informacion", message="No existe ese contacto")

        else:
            messagebox.showinfo(title="Informacion", message="Introduce todos los datos")


    btModificar = tkinter.Button(ventana, text="Modificar", command = modificar)
    btModificar.grid(row = 3, column = 1)

    def borrar():
        try:
            item = tabla.selection()[0]
            nombre = tabla.item(item, option="values")[0]

            for i in range(len(listaContactos) - 1, -1, -1):
                a: Contacto = listaContactos[i]
                if (a.nombre == nombre):
                    listaContactos.remove(a)

            tabla.delete(item)
        except:
            messagebox.showinfo("Informacion", "Selecciona la fila a borrar")


    btBorrar = tkinter.Button(ventana, text = "Borrar", command = borrar)
    btBorrar.grid(row = 3, column = 2)


    def on_closing():
        fichero = open("ficheroContactos", "wb")
        pickle.dump(listaContactos, fichero)
        fichero.close()
        ventana.destroy()

    ventana.protocol("WM_DELETE_WINDOW", on_closing)
    ventana.mainloop()