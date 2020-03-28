
import os #para llamar el método de limpiar pantalla
from colorama import init, Fore, Back, Style #Importar colores
productos=[ {"ID":"1","Producto":"Helado","Cantidad":2,"Precio":2.3},
            {"ID":"2","Producto":"RedBull","Cantidad":2,"Precio":2.3},
            {"ID":"3","Producto":"Inca Kola","Cantidad":2,"Precio":2.3},
            {"ID":"4","Producto":"Coca Cola","Cantidad":2,"Precio":2.3},
            {"ID":"5","Producto":"Cerveza Cuzqueña","Cantidad":2,"Precio":2.3},
            {"ID":"6","Producto":"Cerveza Pilsen","Cantidad":2,"Precio":2.3},
            {"ID":"7","Producto":"Gaseosa","Cantidad":2,"Precio":2.3},
            {"ID":"8","Producto":"Gaseosa","Cantidad":2,"Precio":2.3},
            {"ID":"9","Producto":"Gaseosa","Cantidad":2,"Precio":2.3},
            {"ID":"10","Producto":"Gaseosa","Cantidad":2,"Precio":2.3}]

def titles_menus(opc):
    titleAdding='''\
    +--------------------+
    | ADDING NEW PRODUCT |
    +--------------------+\
    '''
    titleSearching='''\
    +-------------------+
    | SEARCHING PRODUCT |
    +-------------------+\
    '''
    titleModifying='''\
    +-------------------+
    | MODIFYING PRODUCT |
    +-------------------+\
    '''
    titleDeleting='''\
    +-------------------+
    | DELETING PRODUCT  |
    +-------------------+\
    '''
    if opc == 0:
        print(Fore.GREEN+Style.BRIGHT+titleAdding)
    if opc == 1:
        print(Fore.GREEN+Style.BRIGHT+titleModifying)
    if opc == 2:
        print(Fore.GREEN+Style.BRIGHT+titleDeleting)
    if opc == 3:
        print(Fore.GREEN+Style.BRIGHT+titleSearching)

def search_product(product):
    if len(productos)==0:
        print(Fore.RED+Style.BRIGHT+"*"*5+"List is empty"+"*"*5)
    else:
        for dic in productos: #Recorre la cada elemento(dicc) que está dentro de                              productos
            try: #Que me intente realizar estas lineas de código dentro del for loop
                if dic['ID'] == product: #Busca si el parámetro es igual al elemento                             del diccionario
                    print(Fore.GREEN+Style.BRIGHT+"*"*5+"Code found"+"*"*5)
                    for key,items in dic.items(): #Muestra el key y items
                        print(Fore.WHITE+f"{key}:"+Fore.WHITE+Style.BRIGHT+f"{items}")
                    print("")
                # else:
                #     print(Fore.RED+"*"*5+f"Code not found"+"*"*5)
            except:
                pass

def del_product(productId):

    for dic in productos: #Hace un recorrido a cada elemento de la lista                         que son los diccionarios
        try:
            if dic['ID'] == productId:
                print(Fore.RED+Style.BRIGHT+"-"*25)
                print(Fore.RED+Style.BRIGHT+"Eliminando..")
                print(f"\tID: {dic['ID']}")
                print(f"\tProducto: {dic['Producto']}")
                print(f"\tCantidad: {dic['Cantidad']}")
                print(f"\tPrecio: {dic['Precio']}")
                print(Fore.RED+Style.BRIGHT+"-"*25)
                dic.clear() #Eliminar el diccionario entero
                return dic
            # else:
            #     print(f"Producto no está en la lista")
        except:
            pass

def mod_product(cod):

    for dic in productos:
        for elem in dic.keys():
            if dic['ID'] == cod:
                while True:
                    newProduct=input("Nuevo producto: ").lower().capitalize()
                    if len(newProduct) == 0 or newProduct.startswith(" "):
                        print(Fore.RED+Style.BRIGHT+"Por favor, digite un producto")
                        os.system("pause")
                        os.system("cls")
                        titles_menus(1)
                        print(f"ID: {dic['ID']}")
                    else:
                        break
                while True:
                    try:
                        newQuantity=int(input("Nueva cantidad: "))
                        break
                    except ValueError:
                        print(Fore.RED+Style.BRIGHT+"Digite correctamente..")
                        os.system("pause")
                        os.system("cls")
                        titles_menus(1)
                        print(f"ID: {dic['ID']}")
                        print(f"Nuevo Producto: {newProduct}")
                while True:
                    try:
                        newPrice=float(input("Nuevo precio: "))
                        break
                    except:
                        print(Fore.RED+Style.BRIGHT+"Digite correctamente..")
                        os.system("pause")
                        os.system("cls")
                        titles_menus(1)
                        print(f"ID: {dic['ID']}")
                        print(f"Nuevo Producto: {newProduct}")
                        print(f"Nueva Cantidad: {newQuantity}")

                dic['Producto']=newProduct
                dic['Cantidad']=newQuantity
                dic['Precio']=newPrice
                print(Fore.GREEN+Style.BRIGHT+"Product modified successfully")
                break

def create_product(product):
    for dic in productos:
        if product['ID'] in dic['ID']:
            print(Fore.RED+Style.BRIGHT+"Code is already in the list")
            os.system("pause")
            break
    else:
        productos.insert(0,product) #Insertar en la primera posición
        print(Fore.GREEN+Style.BRIGHT+"Product Added successfully")
        # opc=input("Desea seguir registrando productos?"+Fore.YELLOW+Style.BRIGHT+"(s/n): ").lower()
        keepContinue=True
        while True: #Ambos tienen que cumplirse
            #print(Fore.RED+Style.BRIGHT+"Digite la opcion correcta")
            opc=input("Desea seguir registrando productos?"+Fore.YELLOW+Style.BRIGHT+"(s/n): ").lower()
            if opc=='n': #Si es 'n' se rompe el bucle
                break    #Si no lo es, vuelve a recorre el bucle desde arriba                evaluando
            elif opc=='s':
                add_Product()
            else:
                print(Fore.RED+Style.BRIGHT+"Digite la opcion correcta")

def add_Product():
    #opc='0'
    suma_cantidad=0
    #while opc!='n':
    os.system("cls")
    titles_menus(0)
    while True:
        productId=input("Digite ID: ").upper()
        if len(productId)==0 or " " in productId:
            print(Fore.RED+Style.BRIGHT+"Error: Digite ID..")
            os.system("pause")
            os.system("cls")
            titles_menus(0)
        else:
            break
    while True:
        productName=input("Digite producto: ")
        if len(productName)==0:
            print(Fore.RED+Style.BRIGHT+"Error: Digite Producto..")
            os.system("pause")
            os.system("cls")
            titles_menus(0)
            print(f"ID: {productId}")
        else:
            break

    keepGoing=True
    keepGoing2=True
    while keepGoing: #Bucle Infinito
        try:
            productCantidad=int(input(f"Digite cantidad de {productName}: "))
            keepGoing=False #Se rompe el bucle
        except ValueError:
            print(Fore.RED+Style.BRIGHT+"Error: Digite la cantidad correctamente..")
            os.system("pause")
            os.system("cls")
            titles_menus(0) #Después de limpiar pantalla que muestre el menu
            print(f"ID: {productId}")# Y mostrar los input ya ingresados
            print(f"Producto: {productName}")# ...
    while keepGoing2:
        try:
            productPrecio=float(input(f"Digite precio de {productName}: "))
            keepGoing2=False
        except ValueError:
            print(Fore.RED+Style.BRIGHT+"Error: Digite el precio correctamente..")
            os.system("pause")
            os.system("cls")
            titles_menus(0)#Después de limpiar pantalla que muestre el menu
            print(f"ID: {productId}")# Y mostrar los input ya ingresados
            print(f"Producto: {productName}")# ...
            print(f"Cantidad: {productCantidad}")# ...

    #Operation
    suma_cantidad+=productCantidad
    #Registering new dictionary to the list
    products = {
                'ID':productId,
                'Producto':productName,
                'Cantidad':productCantidad,
                'Precio':productPrecio
                }
    create_product(products) #Applying the dict to the List

    #Cálculo
    importe_total=productPrecio*suma_cantidad
    print(f"Importe Total: {importe_total:.2f}")
    if suma_cantidad<5:
        descuento=importe_total*0.10
        print(f"Descuento 10%: {descuento:.2f}")
    elif suma_cantidad>=5 and suma_cantidad<10:
        descuento=importe_total*0.20
        print(f"Descuento 20%: {descuento:.2f}")
    elif suma_cantidad>=10:
        descuento=importe_total*0.40
        print(f"Descuento 40%: {descuento:.2f}")
    importe_pagar=importe_total-descuento
    #Output
    print(f"Total a pagar es: {importe_pagar:,}") #Añadir comas al output

def list_product():

    tabla='''\
    +--------------------------------------------------+
    | Codigo    Producto        Cantidad        Precio |
    |--------------------------------------------------|\
    '''
    # print("\nid | product | quantity | price")
    # print("*"*50)
    print(Fore.WHITE+Style.BRIGHT+tabla)
    for products in productos: #recorre la lista que está conformada por diccionarios
        #for elem in products.keys():
        try:
            print(Fore.GREEN+Style.BRIGHT+"    | {:<9} {:<18} {:<12} S/ {:<3} |".format(
                    products['ID'],
                    products['Producto'],
                    products['Cantidad'],
                    products['Precio']))
        except:
            pass
    print(Fore.WHITE+Style.BRIGHT+"    +--------------------------------------------------+")

def print_welcome():
    # title='''\
    # +-------------------+
    # | WELCOME - D'Kelly |
    # +-------------------+\
    # '''
    title= '''\
        +-------------------+
        | WELCOME - D'Kelly |
        +-------------------+\
    '''
    print(Fore.YELLOW+Style.BRIGHT+title)
    print(Fore.WHITE+Style.BRIGHT+"    >>[A]","dd Product")
    print(Fore.WHITE+Style.BRIGHT+"    >>[S]","earch Product")
    print(Fore.WHITE+Style.BRIGHT+"    >>[L]","ist Products")
    print(Fore.WHITE+Style.BRIGHT+"    >>[M]","odify Product")
    print(Fore.WHITE+Style.BRIGHT+"    >>[D]","elete Product")
    print(Fore.RED+Style.BRIGHT+"    >>[E]","xit")

if __name__=='__main__':
    os.system("cls")
    init(autoreset=True)  #Para la librería colorama que los colores se apliquen correctamente
    opc='0'
    while opc!='E':
        print_welcome()
        opc=input(Fore.WHITE+Style.BRIGHT+'\n    Type your option: ').upper()
        if opc=='E': #Exit
            break
        elif opc=='A': #Add
            os.system("cls")
            add_Product()
            os.system("pause")
            os.system("cls") #Para limpiar pantalla
        elif opc=='S': #Search
            os.system("cls") #Limpiar pantalla cuando se seleccione la opcion
            keepGoing=True
            while keepGoing:
                try:
                    while True:

                        titles_menus(3)
                        productID=input("Digite ID a buscar: ").upper()
                        if len(productID) == 0 or " " in productID:
                            print(Fore.RED+Style.BRIGHT+"Digite correctamente..")
                            os.system("pause")
                            os.system("cls")
                        else:
                            break
                    search_product(productID)
                    keepGoing=False
                except ValueError:
                    print("Error: Digite correctamente el código..")
            tecla=input("Presione cualquier tecla para continuar...")
            os.system("cls") #Para limpiar pantalla
        elif opc=='M': #Modify
            keepGoing=True
            os.system("cls")
            titles_menus(1) #1 for Modifying title
            while keepGoing:
                try:
                    productID=input("Escriba el ID del producto a modificar: ").upper()
                    mod_product(productID)
                    keepGoing=False
                except ValueError:
                    print("Error: Digite correctamente el código..")
            tecla=input("Presione cualquier tecla para continuar...")
            os.system("cls") #Para limpiar pantalla
        elif opc=='D': #Delete
            keepGoing=True
            while keepGoing: #Bucle Infinito
                try:
                    os.system("cls")
                    while True:
                        titles_menus(2)
                        productId=input("Escriba ID del producto a eliminar: ").upper()
                        if len(productId) == 0 or " " in productId:
                            print(Fore.RED+Style.BRIGHT+"Digite correctamente..")
                            os.system("pause")
                            os.system("cls")
                        else:
                            break
                    del_product(productId)
                    keepGoing=False
                except ValueError: #Captura si se digita algún otro tipo de                            caracter
                    print("Error: Digite correctamente el código..")
            tecla=input("Presione cualquier tecla para continuar...")
            os.system("cls") #Para limpiar pantalla
        elif opc=='L': #List
            os.system("cls")
            try:
                list_product()
            except KeyError:
                pass
            tecla=input("Presione cualquier tecla para continuar...")
            os.system("cls")
        else:
            print(Fore.RED+Style.BRIGHT+"    Type the correct option..")
            os.system("pause")
            os.system("cls")
