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


#Funcion actualizar
try:
    id=int(input("Id: "))
    sql="""select id from product where id=?"""
    c.execute(sql,(id,))
    row=c.fetchall()
    rowlen=len(row)
    if rowlen == 0:
        print("El producto no existe")
    else:
        nombre=input("Nombre: ")
        precio=float(input("Precio: "))
        cantidad=int(input("Cantidad: ")) 
        tupla=(nombre,precio,cantidad,id)   
        sql="""update product set descripcion=?, precio=?, cantidad=? where id=?"""
        c.execute(sql,tupla)
        con.commit()
    for i in c.execute("Select * from product"):
        print(i)

    c.close()        
except:
    print("Ocurrio un error")