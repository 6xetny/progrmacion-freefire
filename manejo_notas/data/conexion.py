import mysql.connector

conexion = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    database='gestion_notas'
)

cursor = conexion.cursor()

def ejecutar_consulta(consulta):
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    return resultado

cursor.execute('SELECT numero_opcion,opcion_menu FROM opciones_menu')
resultado = cursor.fetchall()
print(resultado)