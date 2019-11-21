import pymysql

# Se abre la conexión con el servidor de BD
db = pymysql.connect("localhost", "root", "", "msc2019")

# Creamos un objeto tipo cursor
cursor = db.cursor()

name = "Isis Siomara"
salary = 293765.28

# Definir cadena SQL
sql = "INSERT INTO empelado(nombre, sueldo) VALUES ('{0}', {1})".format(name, salary)

print(sql)

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()