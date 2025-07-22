import os
os.system("clear")
import tkinter as tk
from views.header import cargar_header
from views.productos import cargar_accesorios
from views.login import cargar_login

ventana = tk.Tk()
ventana.title("La forja del abismo")
ventana.geometry("1000x600")

cargar_login(ventana)
# cargar_accesorios(ventana)
ventana. mainloop()

# Individuo para pruebas
# vacío@silencio.com
# enigma

# Parámetro para inicar mariadb
# mariadb -h bmmx6n7wvjqwe0gjlvug-mysql.services.clever-cloud.com -P 3306 -u uuetioutxhsauocl -p --skip-ssl
# "password": "Uvqln2sXjxz81w1ksiiz",
# "database": "bmmx6n7wvjqwe0gjlvug",