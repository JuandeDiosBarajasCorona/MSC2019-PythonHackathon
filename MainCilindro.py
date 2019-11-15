from tkinter import *
from tkinter import ttk, font
from Cilindro import Cilindro
#import getpass


# Gestor de geometría (grid). Ventana no dimensionable

class Aplicacion():
    # Declara una variable de clase para contar ventanas

    ventana = 0

    # Declara una variable de clase para usar en el
    # cálculo de la posición de una ventana

    posx_y = 0
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Cilindro")
        #self.raiz.geometry("640x480")
        #self.raiz.resizable(width=False, height=False)

        # Establece que no se pueda modificar el tamaño de la
        # ventana. El método resizable(0,0) es la forma abreviada
        # de resizable(width=False,height=False).

        self.raiz.resizable(0, 0)
        fuente = font.Font(weight='bold')

        # Define un widget de tipo 'Frame' (marco) que será el
        # contenedor del resto de widgets. El marco se situará
        # en la ventana 'self.raiz' ocupando toda su extensión.
        # El marco se define con un borde de 2 píxeles y la
        # opción 'relief' con el valor 'raised' (elevado) añade
        # un efecto 3D a su borde.
        # La opción 'relief' permite los siguientes valores:
        # FLAT (llano), RAISED (elevado), SUNKEN (hundido),
        # GROOVE (hendidura) y RIDGE (borde elevado).
        # La opción 'padding' añade espacio extra interior para
        # que los widgets no queden pegados al borde del marco.

        self.marco = ttk.Frame(self.raiz, borderwidth=2,
                               relief="raised", padding=(10, 10))

        # Define el resto de widgets pero en este caso el primer
        # paràmetro indica que se situarán en el widget del
        # marco anterior 'self.marco'.

        self.etiq1 = ttk.Label(self.marco, text="X:",
                               font=fuente, padding=(5, 5))
        self.etiq2 = ttk.Label(self.marco, text="Y:",
                               font=fuente, padding=(5, 5))
        self.etiq3 = ttk.Label(self.marco, text="Radio:",
                               font=fuente, padding=(5, 5))
        self.etiq4 = ttk.Label(self.marco, text="Altura:",
                               font=fuente, padding=(5, 5))

        # Define variables para las opciones 'textvariable' de
        # cada caja de entrada 'ttk.Entry()'.

        self.valorX = StringVar()
        self.valorY = StringVar()
        self.vradio = StringVar()
        self.valtura = StringVar()
        #self.usuario.set(getpass.getuser())
        self.ctext1 = ttk.Entry(self.marco, textvariable=self.valorX,
                                width=30)
        self.ctext2 = ttk.Entry(self.marco, textvariable=self.valorY,
                                width=30)
        self.ctext3 = ttk.Entry(self.marco, textvariable=self.vradio,
                                width=30)
        self.ctext4 = ttk.Entry(self.marco, textvariable=self.valtura,
                                width=30)
        self.separ1 = ttk.Separator(self.marco, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.marco, text="Crear",
                                 padding=(5, 5), command=self.crear)
        self.boton2 = ttk.Button(self.marco, text="Imprimir",
                                 padding=(5, 5), command=self.imprimir)
        self.boton3 = ttk.Button(self.marco, text="Salir",
                                 padding=(5, 5), command=quit)

        # Define la ubicación de cada widget en el grid.
        # En este ejemplo en realidad hay dos grid (cuadrículas):
        # Una cuadrícula de 1fx1c que se encuentra en la ventana
        # que ocupará el Frame; y otra en el Frame de 5fx3c para
        # el resto de controles.
        # La primera fila y primera columna serán la número 0.
        # La opción 'column' indica el número de columna y la
        # opción 'row' indica el número de fila donde hay que
        # colocar un widget.
        # La opción 'columnspan' indica al gestor que el
        # widget ocupará en total un número determinado de
        # columnas. Las cajas para entradas 'self.ctext1' y
        # 'self.ctext2' ocuparán dos columnas y la barra
        # de separación 'self.separ1' tres.

        self.marco.grid(column=0, row=0)
        self.etiq1.grid(column=0, row=0)
        self.ctext1.grid(column=1, row=0, columnspan=2)
        self.etiq2.grid(column=0, row=1)
        self.ctext2.grid(column=1, row=1, columnspan=2)
        self.etiq3.grid(column=0, row=2)
        self.ctext3.grid(column=1, row=2, columnspan=2)
        self.etiq4.grid(column=0, row=3)
        self.ctext4.grid(column=1, row=3, columnspan=2)
        self.separ1.grid(column=0, row=4, columnspan=3)
        self.boton1.grid(column=0, row=5)
        self.boton2.grid(column=1, row=5)
        self.boton3.grid(column=2, row=5)

        # Establece el foco en la caja de entrada de la
        # contraseña.

        self.ctext1.focus_set()
        self.raiz.mainloop()

        """
        if self.clave.get() == 'tkinter':
            print("Acceso permitido")
            print("Usuario:   ", self.ctext1.get())
            print("Contraseña:", self.ctext2.get())
        else:
            print("Acceso denegado")
            self.clave.set("")
            self.ctext1.focus_set()
         """

    def crear(self):
        valorX = int(self.ctext1.get())
        valorY = int(self.ctext2.get())
        vradio = int(self.ctext3.get())
        valtura = int(self.ctext4.get())

        Cilindro.__init__(self, valorX, valorY, vradio, valtura)

        Cilindro.setX(self, valorX)
        Cilindro.setY(self, valorY)
        Cilindro.setRadio(self, vradio)
        Cilindro.setAltura(self, valtura)

        ''' Construye una ventana de diálogo '''

        # Define una nueva ventana de diálogo

        self.dialogo = Toplevel()

        # Incrementa en 1 el contador de ventanas

        Aplicacion.ventana += 1

        # Recalcula posición de la ventana

        Aplicacion.posx_y += 50
        tamypos = '200x100+' + str(Aplicacion.posx_y) + \
                  '+' + str(Aplicacion.posx_y)
        self.dialogo.geometry(tamypos)
        self.dialogo.resizable(0, 0)

        # Obtiene identicador de la nueva ventana

        ident = self.dialogo.winfo_id()

        # Construye mensaje de la barra de título

        #titulo = str(Aplicacion.ventana) + ": " + str(ident)
        self.dialogo.title("Alerta")

        # Define el botón 'Cerrar' que cuando sea
        # presionado cerrará (destruirá) la ventana
        # 'self.dialogo' llamando al método
        # 'self.dialogo.destroy'
        texto = ttk.Label(self.dialogo, text="¡El objeto ha sido creado con éxito!")
        boton = ttk.Button(self.dialogo, text='Aceptar',
                           command=self.dialogo.destroy)
        texto.pack(side=TOP, padx=20, pady=5)
        boton.pack(side=BOTTOM, padx=20, pady=20)

        # Cuando la ejecución del programa llega a este
        # punto se utiliza el método wait_window() para
        # esperar que la ventana 'self.dialogo' sea
        # destruida.
        # Mientras tanto se atiende a los eventos locales
        # que se produzcan, por lo que otras partes de la
        # aplicación seguirán funcionando con normalidad.
        # Si hay código después de esta línea se ejecutará
        # cuando la ventana 'self.dialogo' sea cerrada.

        self.raiz.wait_window(self.dialogo)

    def imprimir(self):
        ''' Construye una ventana de diálogo '''

        # Define una nueva ventana de diálogo

        self.dialogo = Toplevel()

        # Incrementa en 1 el contador de ventanas

        Aplicacion.ventana += 1

        # Recalcula posición de la ventana

        Aplicacion.posx_y += 50
        tamypos = '220x280+' + str(Aplicacion.posx_y) + \
                  '+' + str(Aplicacion.posx_y)
        self.dialogo.geometry(tamypos)
        self.dialogo.resizable(0, 0)

        # Obtiene identicador de la nueva ventana

        ident = self.dialogo.winfo_id()

        # Construye mensaje de la barra de título

        # titulo = str(Aplicacion.ventana) + ": " + str(ident)
        self.dialogo.title("Alerta")

        # Define el botón 'Cerrar' que cuando sea
        # presionado cerrará (destruirá) la ventana
        # 'self.dialogo' llamando al método
        # 'self.dialogo.destroy'

        textX = "El valor de X es: "+str(Cilindro.getX(self))
        textY = "El valor de Y es: "+str(Cilindro.getY(self))
        textradio = "El valor del radio es: "+str(Cilindro.getRadio(self))
        textaltura = "El valor de la altura es: "+str(Cilindro.getAltura(self))
        textvolumen = "El valor del volumen es: "+str(Cilindro.getVolumen(self))

        texto = ttk.Label(self.dialogo, text="Valores del cilindro: ")

        valor1 = ttk.Label(self.dialogo, text=textX)
        valor2 = ttk.Label(self.dialogo, text=textY)
        valor3 = ttk.Label(self.dialogo, text=textradio)
        valor4 = ttk.Label(self.dialogo, text=textaltura)
        valor5 = ttk.Label(self.dialogo, text=textvolumen)

        boton = ttk.Button(self.dialogo, text='Aceptar',
                           command=self.dialogo.destroy)

        texto.pack(side=TOP, padx=20, pady=5)
        valor1.pack(side=TOP, padx=20, pady=5)
        valor2.pack(side=TOP, padx=20, pady=5)
        valor3.pack(side=TOP, padx=20, pady=5)
        valor4.pack(side=TOP, padx=20, pady=5)
        valor5.pack(side=TOP, padx=20, pady=5)

        boton.pack(side=BOTTOM, padx=20, pady=20)

        # Cuando la ejecución del programa llega a este
        # punto se utiliza el método wait_window() para
        # esperar que la ventana 'self.dialogo' sea
        # destruida.
        # Mientras tanto se atiende a los eventos locales
        # que se produzcan, por lo que otras partes de la
        # aplicación seguirán funcionando con normalidad.
        # Si hay código después de esta línea se ejecutará
        # cuando la ventana 'self.dialogo' sea cerrada.

        self.raiz.wait_window(self.dialogo)

def main():
    mi_app = Aplicacion()
    return 0


if __name__ == '__main__':
    main()