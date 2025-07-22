import tkinter as tk 
from services.gb import ejecutar_consulta
from views.productos import cargar_accesorios

def cargar_login(ventana):
    login_panel = tk.Frame(
        ventana,
        bg="green",
        padx=0,
        pady=0,
        width=100,
        height=100
    )
    
    titulo = tk.Label(login_panel, text="Login")
    titulo.pack()
    
    txt_correo = tk.Label(login_panel, text="Correo")
    txt_correo.pack()

    entrada_correo = tk.Entry(login_panel)
    entrada_correo.pack()

    txt_contra = tk.Label(login_panel, text="Contraseña")
    txt_contra.pack()

    entrada_contrasenha = tk.Entry(login_panel, show="*")  # Oculta la contraseña
    entrada_contrasenha.pack()

    def funcion_boton():
        usuario_login = entrada_correo.get()
        contrasenha_login = entrada_contrasenha.get()

        sql = "SELECT * FROM usuarios WHERE correo = ? AND contrasena = ?"
        parametros = (usuario_login, contrasenha_login)
        resultado = ejecutar_consulta(sql, parametros)

        if resultado and resultado[0][0] != "Error":
            print("Usuario:", usuario_login)
            print("Contraseña:", contrasenha_login)
            login_panel.destroy()
            cargar_accesorios(ventana)
        else:
            print("Datos incorrectos")

    boton = tk.Button(login_panel, text="Continuar", command=funcion_boton)
    boton.pack()

    login_panel.pack()
    print("Panel login cargado")
