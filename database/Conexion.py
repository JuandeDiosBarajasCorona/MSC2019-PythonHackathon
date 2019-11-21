import pymysql

# Se abre la conexión con el servidor de BD
db = pymysql.connect("localhost", "root", "", "msc2019")

# Creamos un objeto tipo cursor
cursor = db.cursor()

#Cadena SQL para recuperar los datos del servidor
sql = "SELECT * FROM test WHERE id > {0}".format(0)

# Ejectuamos la cadena sql
cursor.execute(sql)

# Se almacena la respuesta del servidor
results = cursor.fetchall()

# Se imprime el resultado
for row in results:
    id = row[0]
    name = row[1]
    email = row[2]

    print("id = {0}, nombre = {1}, email = {2}".format(id, name, email))
