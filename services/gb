import mariadb

credenciales = {
    "user": "dxn",
    "password": "root",
    "host": "localhost",
    "database": "Korn"
}

def ejecutar_consulta(sql):
    try:
        conexion = mariadb.connect(**credenciales)
        cursor = conexion.cursor()
        cursor.execute(sql)
        resultados = cursor.fetchall()
        conexion.close()
        return resultados
    except mariadb.Error as error:
        return [("Error", str(error))]
