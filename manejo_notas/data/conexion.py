import mysql.connector

conexion = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    database='locopepe_gestion_notas'
)

cursor = conexion.cursor()

cursor.execute('SELECT * FROM docentes')
resultado = cursor.fetchall()
print(resultado)