import sqlite3#para conectar con la base de datos sqlite
import os #para llamar el método de limpiar pantalla
from colorama import init, Fore, Back, Style #Importar colores 

con=sqlite3.connect("Store.db")
c=con.cursor()

nombre=input("Nombre: ")
precio=float(input("Precio: "))
cantidad=int(input("Cantidad: "))

tupla=(nombre,cantidad,precio)

sql="insert into product (descripcion,cantidad,precio) values (?,?,?)"

try:
    c.execute(sql,tupla)
    con.commit()
except:
    print("Ocurrio un error")

for i in c.execute("Select * from product"):
    print(i)

c.close()

