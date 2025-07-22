import mariadb

credenciales = {
    "user": "uuetioutxhsauocl",
    "password": "Uvqln2sXjxz81w1ksiiz",
    "host": "bmmx6n7wvjqwe0gjlvug-mysql.services.clever-cloud.com",
    "port": 3306,
    "database": "bmmx6n7wvjqwe0gjlvug"
}

def conectar():
    try:
        conexion = mariadb.connect(**credenciales)
        return conexion
    except mariadb.Error as error:
        raise error

def ejecutar_consulta(sql, parametros=None):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(sql, parametros or ())
        resultados = cursor.fetchall()
        conexion.close()
        return resultados
    except mariadb.Error as error:
        return [("Error", str(error))]

def ejecutar_modificacion(sql, parametros=None):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(sql, parametros or ())
        conexion.commit()
        conexion.close()
        return True
    except mariadb.Error as error:
        print("Error:", error)
        return False
