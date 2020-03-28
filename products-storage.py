import sqlite3#para conectar con la base de datos sqlite
import os #para llamar el método de limpiar pantalla
from colorama import init, Fore, Back, Style #Importar colores

con=sqlite3.connect("Store.db")
cursor=con.cursor()

def adding_function():
    nombre=input("Nombre: ")
    precio=float(input("Precio: "))
    cantidad=int(input("Cantidad: "))

    tupla=(nombre,cantidad,precio)
    sql="insert into product (descripcion,cantidad,precio) values (?,?,?)"

    try:
        cursor.execute(sql,tupla)
        con.commit()
        print('Product was added successfully!')
    except:
        print("Ocurrio un error")

#List function
def list_function():
    cursor.execute("select * from product")
    data = cursor.fetchall()
    #print(c.execute("select * from product"))
    for values in data:
        for y in values:
            print(y,end=" ")
        print("\n")
# Update function
def update_function():
    try:
        id=int(input("Id: "))
        sql="""select id from product where id=?"""
        cursor.execute(sql,(id,))
        row=cursor.fetchall()
        rowlen=len(row)
        if rowlen == 0:
            print("El producto no existe")
        else:
            nombre=input("Nombre: ")
            precio=float(input("Precio: "))
            cantidad=int(input("Cantidad: "))
            tupla=(nombre,precio,cantidad,id)
            sql="""update product set descripcion=?, precio=?, cantidad=? where id=?"""
            cursor.execute(sql,tupla)
            con.commit()
        for i in cursor.execute("Select * from product"):
            print(i)

    except:
        print("Ocurrio un error")

def delete_function():
    try:
        id = int(input("Digite ID: "))
        sql = "delete from product where id = ?"
        cursor.execute(sql,(id,))
        con.commit()
        print("Product deleted successfully")
    except:
        print("Product doesn't exist")

def menu():
    print(Fore.WHITE+Style.BRIGHT+"    >>[A]","dd Product")
    print(Fore.WHITE+Style.BRIGHT+"    >>[S]","earch Product")
    print(Fore.WHITE+Style.BRIGHT+"    >>[L]","ist Products")
    print(Fore.WHITE+Style.BRIGHT+"    >>[U]","pdate Product")
    print(Fore.WHITE+Style.BRIGHT+"    >>[D]","elete Product")
    print(Fore.RED+Style.BRIGHT+"    >>[E]","xit")

if __name__=="__main__":
    init(autoreset=True)  #Para la librería colorama que los colores se apliquen correctamente
    opc = '0'
    while opc!='E':
        menu()
        opc=input('Please, choose an option: ').upper()
        if opc=='E':
            break
        elif opc=='A':
            adding_function()
        elif opc=='L':
            list_function()
        elif opc=='M':
            update_function()
        elif opc=='D':
            delete_function()
        else:
            print('Type the correct option..')
            os.system('pause')
            os.system('cls')
    con.close()
