import sqlite3#para conectar con la base de datos sqlite
import os #para llamar el método de limpiar pantalla

from colorama import init, Fore, Back, Style #Importar colores 

con=sqlite3.connect("Store.db")
cursor=con.cursor()

nombre=input("Nombre: ")
precio=float(input("Precio: "))
cantidad=int(input("Cantidad: "))

tupla=(nombre,cantidad,precio)

sql="insert into product (descripcion,cantidad,precio) values (?,?,?)"

try:
    cursor.execute(sql,tupla)
    con.commit()
except:
    print("Ocurrio un error")

cursor.execute("select * from product")
data = cursor.fetchall()
#print(c.execute("select * from product"))
for x in data:
    for y in x:
        print(y,end=" ")
    print("\n")
c.close()
