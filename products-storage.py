import sqlite3#para conectar con la base de datos sqlite
import os #para llamar el método de limpiar pantalla
from colorama import init, Fore, Back, Style #Importar colores

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

def print_welcome():
    title= '''
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

con=sqlite3.connect("Store.db")
c=con.cursor()

for i in c.execute("Select * from product"):
    print(i)

init(autoreset=True)  #Para la librería colorama que los colores se apliquen correctamente 
print_welcome()
