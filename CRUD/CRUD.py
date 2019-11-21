from tkinter import *
from tkinter import messagebox
import pymysql
import fpdf
from fpdf import FPDF

# abrir conexion a la base de datos msc2019 y la tabla trabajdores
db = pymysql.connect("juandebarco.com", "juandeba_admin", "time in london", "juandeba_crudmsc2019")
# Creamos ub objeto tipo cursor
cursor = db.cursor()


def insert():
    id = inp_clave.get()
    name = inp_nombre.get()
    salary = inp_sueldo.get()
    if (id == "" or name == "" or salary == ""):
        messagebox.showinfo(message="Status inser: Se requieren todos los campos", title="Advertencia")
    else:
        sql = "INSERT INTO empelado(clave,nombre,sueldo) values({0},'{1}',{2})".format(id, name, salary)
        cursor.execute(sql)
        db.commit()
        inp_clave.delete(0, 'end')
        inp_nombre.delete(0, 'end')
        inp_sueldo.delete(0, 'end')
        messagebox.showinfo(message="Dato insertado", title="Advertencia")
        show()


def delete():
    if (inp_clave.get() == ""):
        messagebox.showinfo(message="Campo clave requerido", title="Advertencia")
    else:
        sql = "DELETE FROM empelado WHERE clave ='" + inp_clave.get() + "'"
        cursor.execute(sql)
        db.commit()
        inp_clave.delete(0, 'end')
        inp_nombre.delete(0, 'end')
        inp_sueldo.delete(0, 'end')
        messagebox.showinfo(message="Dato eliminado", title="Advertencia")
        show()


def update():
    sql = "UPDATE empelado SET nombre='" + inp_nombre.get() + "',sueldo='" + inp_sueldo.get() + "' WHERE clave='" + inp_clave.get() + "'"
    cursor.execute(sql)
    db.commit()
    inp_clave.delete(0, 'end')
    inp_nombre.delete(0, 'end')
    inp_sueldo.delete(0, 'end')
    messagebox.showinfo(message="Dato Actualizado", title="Advertencia")
    show()


def show():
    sql = "SELECT * FROM empelado"
    cursor.execute(sql)
    db.commit()
    rows = cursor.fetchall()
    list.delete(0, list.size())

    for row in rows:
        insertData = str(row[0]) + '    ' + row[1] + '    ' + str(row[2])
        list.insert(list.size() + 1, insertData)


def reporte():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 20, )
    pdf.cell(180, 10, 'Reportes de empleados', 1, 1, 'C')
    pdf.set_font('Arial', 'B', 10, )
    pdf.cell(60, 10, 'Clave', 1, 0, 'C')
    pdf.cell(60, 10, 'Nombre', 1, 0, 'C')
    pdf.cell(60, 10, 'Sueldo', 1, 1, 'C')

    # conexion a mysql
    con = pymysql.connect(host="juandebarco.com", user="juandeba_admin", password="time in london", database="juandeba_crudmsc2019")
    cursor = con.cursor()
    cursor.execute("select * from empelado")
    rows = cursor.fetchall()
    # list.delete(0, list.size())
    pdf.set_font('Arial', '', 10)
    for row in rows:
        pdf.cell(60, 10, str(row[0]), 1, 0, 'C')
        pdf.cell(60, 10, str(row[1]), 1, 0, 'C')
        pdf.cell(60, 10, str(row[2]), 1, 1, 'C')

    con.close()
    pdf.output('reportes.pdf', 'F')


root = Tk()
root.config(bd=15)
clave = StringVar()
nombre = StringVar()
sueldo = StringVar()

root.geometry("650x250")
root.resizable(width=False, height=False)
root.title('CRUD PYTHON')

lbl_clave = Label(root, text="Clave:")
lbl_clave.place(x=20, y=30)
inp_clave = Entry(root, textvariable=clave)
inp_clave.place(x=150, y=30)

lbl_nombre = Label(root, text="Nombre:")
lbl_nombre.place(x=20, y=60)
inp_nombre = Entry(root, textvariable=nombre)
inp_nombre.place(x=150, y=60)

lbl_sueldo = Label(root, text="Sueldo:")
lbl_sueldo.place(x=20, y=90)
inp_sueldo = Entry(root, textvariable=sueldo)
inp_sueldo.place(x=150, y=90)

btn_insertar = Button(root, text="Insertar", command=insert)
btn_insertar.place(x=20, y=140)
btn_eliminar = Button(root, text="Eliminar", command=delete)
btn_eliminar.place(x=75, y=140)
btn_actualizar = Button(root, text="Actualizar", command=update)
btn_actualizar.place(x=135, y=140)
btn_reporte = Button(root, text="Reporte", command=reporte)
btn_reporte.place(x=205, y=140)

list = Listbox(root, width=50)
list.place(x=290, y=30)
show()
root.mainloop()