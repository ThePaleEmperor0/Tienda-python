import tkinter as tk

def cargar_usuario(ventana):
    panel = tk.Frame(ventana, bg="green", width=1000, height=600)
    
    tk.Label(panel, text="Correo").pack()
    entrada_correo = tk.Entry(panel)
    entrada_correo.pack()

    tk.Label(panel, text="Contraseña").pack()
    entrada_contrasenha = tk.Entry(panel, show="*")
    entrada_contrasenha.pack()

    def registrar_usuario():
        correo = entrada_correo.get()
        contrasena = entrada_contrasenha.get()
        if correo and contrasena:
            print("Usuario registrado:", correo)
        else:
            print("Faltan datos")

    tk.Button(panel, text="Continuar", command=registrar_usuario).pack()
    panel.pack()
    print("Panel usuario cargado")
