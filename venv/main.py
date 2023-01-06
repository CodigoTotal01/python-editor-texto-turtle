import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfilename
class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('GlobalMentoring.com.mx - Editor de Texto')
        # Configuración tamaño mínimo de la venta
        self.rowconfigure(0, minsize=600, weight=1)
        # Configuración mínima de la segunda columna
        self.columnconfigure(1, minsize=600, weight=1)
        # Atributo de campo de texto -> usada en el commponente -< y recien se esta añadiendo
        self.campo_texto = tk.Text(self, wrap=tk.WORD)
        # Atributo de archivo
        self.archivo = None
        # Atributo para saber si ya se abrió un archivo anteriormente
        self.archivo_abierto = False
        # Creación de componentes
        self._crear_componentes()
        self._crear_menu()

    def _crear_componentes(self):
        frame_botones = tk.Frame(self, relief=tk.RAISED, bd=2)
        boton_abrir = tk.Button(frame_botones, text='Abrir')
        boton_guardar = tk.Button(frame_botones, text='Guardar')
        boton_guardar_como = tk.Button(frame_botones, text='Guardar como...')
        ##los elementos se ajustan segun elemeneto mas grande
        boton_abrir.grid(row=0, column=0, sticky='we', padx=5, pady=5)
        boton_guardar.grid(row=1, column=0, sticky='we', padx=5, pady=5)
        boton_guardar_como.grid(row=2, column=0, sticky='we', padx=5, pady=5)
        # Se coloca el frame de manera vertical
        frame_botones.grid(row=0, column=0, sticky='ns')
        # Agregamos el campo de texto, se expandirá por completo el espacio disponible
        self.campo_texto.grid(row=0, column=1, sticky='nswe')

    def _crear_menu(self):
        #creamdo el menu de la app
        menu_app = tk.Menu(self)
        self.config(menu=menu_app)
        menu_archivo = tk.Menu(menu_app, tearoff=False)
        menu_app.add_cascade(label="Archivo", menu= menu_archivo) #aqui recien le pasamos y se mostrara cdomo menu archivo
        #el menu en cascada contendra opcionares add_command
        menu_archivo.add_command(label="Abrir", command=self._abrir_archivo)  # aqui recien le pasamos y se mostrar
        menu_archivo.add_command(label="Guardar", command=self._guardar) #aqui recien le pasamos y se mostrara cdomo menu archivo
        menu_archivo.add_command(label="Guardar Como..",command=self._guardar_como) #aqui recien le pasamos y se mostrara cdomo menu archivo
        menu_archivo.add_separator()
        #metodo propio para salir
        menu_archivo.add_command(label="Quit", command=self.quit) #aqui recien le pasamos y se mostrara cdomo menu archivo

    def _abrir_archivo(self):
        #para abrir archivo para editar (lectura y escritura )
        self.archivo_abierto = askopenfile(mode="r+")
        #ELIMINAR TEXTO ANTERIO -> desde la propia caja de texto
        self.campo_texto.delete(1.0, tk.END)
        #si hay archivo
        #si n oexiste
        if not self.archivo_abierto:
            return  #no hacer nada salir nomas
        #pero si todo esta bien abriremos el archivo modo escritura y lectura
        #recursos
        #guarda la referenciua en nuestro valor de arhcivo que emoes generado antes
        with open(self.archivo_abierto.name, "r+") as self.archivo:
            #leemos el contenido del archivo
            texto =  self.archivo.readlines()
            #debemos indicar de donde debemos inicaiar a insirtar
            self.campo_texto.insert(tk.INSERT, texto)
            self.title(f'Escribiendo en: {self.archivo_abierto.name}')

    def _guardar(self):
        #si se guardo un archivo -> lo sobreescbimos -> solo escritura
        if self.archivo_abierto: #guardamos referencia
            with open(self.archivo_abierto.name, "w") as self.archivo:
                #leemos contenido de la caja de texto
                texto = self.campo_texto.get(1.0, tk.END) #leer de arriba hacia abajo
                self.archivo.write(texto) #sobreescbribiomos seria con append el otro coso
                self.title("Binario 01 -> editor de texto")
        else:
            self._guardar_como()

    def _guardar_como(self):
        #salvamos el archivo actual como un nuevo archivo
        self.archivo = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Archivos de texto", "*.txt"), ("todos los archivos", "*.*")]
        )
        #si no esta vacio
        if not self.archivo:
            return
        with open(self.archivo, "w") as self.archivo:
            # leemos contenido de la caja de texto
            texto = self.campo_texto.get(1.0, tk.END)  # leer de arriba hacia abajo
            self.archivo.write(texto)  # sobreescbribiomos seria con append el otro coso
            self.title("Binario 01 -> salvado 🤖")


if __name__ == "__main__":
    editor = Editor()
    editor.mainloop()