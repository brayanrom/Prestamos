from os import system
from Personas import Persona
from PrestamosNew import Articulo
from bd import MysqlDatabase
from bd import MongoDatabase
class Menu:
    def __init__(self):
        print("Seleccione la base de datos predeterminada")
        print("1.- Mysql")
        print("2.- MongoDB")
        self.dbActual=input("-> ")
        self.limpiar()

    def menuPR(self):
        while True:
                print("1.- Obtener material")
                print("2.- Devolver material")
                print("3.- Registro de prestamos")
                print("5.- Configuracion")
                print("0.- Salir")
                print("")
                print("Seleccione la opcion deseada")
                opcionint = int(input("-> "))
            #----------------------------------------------------------------------
                if opcionint==1:               #pedir objetos   Obtener material
                    self.limpiar()
                    print("1.- Balon de Futbol")
                    print("2.- Balon de Basquetball")
                    print("3.- Pelota de tenis")
                    print("0.- Salir")   
                    opc=int(input('Ingrese la opcion deseada-> ')) 
                    if opc==1:
                        matricula,cantidad=Persona.tMatricula()
                        articulo='Balon de Futbol'
                        self.RegistrarArticulo(matricula,articulo,cantidad)
                    elif opc==2:
                        self.limpiar()
                        matricula,cantidad=Persona.tMatricula()
                        articulo= 'Balon de Basquetball'
                        self.RegistrarArticulo(matricula,articulo,cantidad)
                    elif opc==3:
                        self.limpiar()
                        matricula,cantidad=Persona.tMatricula()
                        articulo='Pelota de tenis'
                        self.RegistrarArticulo(matricula,articulo,cantidad)
                    elif opc==0:
                        self.limpiar()  
                        True    
            #----------------------------------------------------------------------
                elif opcionint==2:                           #devolver objetos
                    Menu.limpiar()
                    print('Que deseas regresar')
                    print("1.- Balon de Futbol")
                    print("2.- Balon de Basquetball")
                    print("3.- Pelota de tenis")  
                    print("0.- Salir")  
                    opc=int(input('->'))
                    Menu.limpiar()
                    tmp=Articulo()
                    c=1
                    if opc==1:
                        print("------------------------------------------------------------------")
                        print("|N/Pres\t|Matricula\t|Articulo\t\t\t| C/Prestada\t |")
                        listaA= tmp.VerArticulos()
                        for articulo in listaA:
                            if articulo.articulo=="Balon de Futbol":
                                print("|#"+ str(c)+"\t|"+ articulo.matricula+"\t|"+
                                articulo.articulo+"\t\t|"+
                                str(articulo.cantidad)+"\t\t |")
                        print('')
                        Menu.eliminar()
                    elif opc==2:
                        print("------------------------------------------------------------------")
                        print("|N/Pres\t|Matricula\t|Articulo\t\t\t| C/Prestada\t |")
                        listaA= tmp.VerArticulos()
                        for articulo in listaA:
                            if articulo.articulo=="Balon de Basquetball":
                                print("|#"+ str(c)+"\t|"+ articulo.matricula+"\t|"+
                                articulo.articulo+"\t\t|"+
                                str(articulo.cantidad)+"\t\t |")
                        print('')
                        Menu.eliminar()
                    elif opc==3:
                        print("------------------------------------------------------------------")
                        print("|N/Pres\t|Matricula\t|Articulo\t\t\t| C/Prestada\t |")
                        listaA= tmp.VerArticulos()
                        for articulo in listaA:
                            if articulo.articulo=="Pelota de tenis":
                                print("|#"+ str(c)+"\t|"+ articulo.matricula+"\t|"+
                                articulo.articulo+"\t\t|"+
                                str(articulo.cantidad)+"\t\t |")
                        print('')
                        Menu.eliminar()        
                    elif opc==0:
                        Menu.limpiar()  
                        True      
            #----------------------------------------------------------------------
                elif opcionint==3:                 #registro prestamos  txt
                    self.limpiar()
                    self.VerInventario()
                    print('')
            #----------------------------------------------------------------------
                elif opcionint==4:                 #registro prestamos  txt
                    self.limpiar()
                    print('')
            #----------------------------------------------------------------------
                elif opcionint==5:                           #configuracion
                    system("cls")
                    print("----------------------------------------------------")
                    print("|Seleccione que configuracion desea realizar       |")
                    print("----------------------------------------------------")
                    print('1.- Cargar historial desde archivo local(fusionar Json)')
                    print('2.- Cargar historial desde archivo local(Reemplazar Json)')
                    print("")
                    print("3.- Crear Base de Datos(Mysql)")
                    print("4.- Crear tabla(Mysql)")
                    print("5.- Insertar datos de Prueba(Mysql)")
                    print("")
                    print("6.- Crear Base de Datos(MongoDB)")
                    print("7.- Crear tabla(MongoDB)")
                    print("8.- Insertar datos de Prueba(MongoDB)")
                    print("")
                    print("9.- Configurar BD por defecto")
                    print("10.-insertar datos prueba general")

                    print("")
                    print("0.- Salir")
                    opc=int(input('-> '))
                    if opc==1:
                        tmp=Articulo()
                        tmp.CargarArticulos()
                    elif opc==2:
                        tmp=Articulo()
                        tmp.CargarArticulosReemplazado()


                    elif opc==3:
                        self.limpiar()
                        tmp=MysqlDatabase()
                        tmp.crearBD()
                    elif opc==4:
                        self.limpiar()
                        tmp=MysqlDatabase()
                        tmp.crearTabla()
                    elif opc==5:
                        self.limpiar()
                        tmp=MysqlDatabase()
                        tmp.insertarDatosPrueba()


                    elif opc==6:
                        MongoDatabase.crearBD()
                    elif opc==7:
                        MongoDatabase.crearTabla()
                    elif opc==8:
                        MongoDatabase.insertarDatosPrueba()



                    elif opc==9:
                        self.limpiar()
                        self.masterBD()
                        
                    elif opc==10:
                        self.limpiar()
                        print("Entro 10")
                    
                    elif opc==11:
                        self.limpiar()
                        self.getDB()                

                    elif opc==0:
                        self.limpiar()
            #----------------------------------------------------------------------
                elif opcionint==0:                        #salir     yasta
                    print('Saliendo...')
                    break



    def getDB(self):
        print("Entro BD")
        print(self.dbActual)

    def limpiar(self):
        system("cls")        

    def RegistrarArticulo(self,matricula,articulo,cantidad):
        tmp=Articulo()
        tmp.RegistroArticulo(matricula,articulo,cantidad)
        self.masterBD(self.dbActual, matricula,articulo,cantidad)

    def VerInventario(self):
        print("------------------------------------------------------------------")
        print("|Matricula\t|Articulo\t\t\t| C/Prestada\t |")
        print("------------------------------------------------------------------")
        tmp=Articulo()
        listaA= tmp.VerArticulos()
        for articulo in listaA:
            print("|"+articulo.matricula+"\t|"+
            articulo.articulo+"\t\t|"+
            str(articulo.cantidad)+"\t\t |")
        print("------------------------------------------------------------------")
    
    def eliminar():
        tmp=Articulo()
        tmp.DevolucionesPrestamos()

    def masterBD(self,BDNum,matricula,articulo,cantidad):

        print("entroRegistro1")
        if(BDNum==1):
            tmp=MysqlDatabase()
            tmp.insertarDatos(matricula,articulo,cantidad)
            print("Entro BD 1")
        elif(BDNum==2):
            BD=MongoDatabase()
            BD.insertarDatos(matricula,articulo,cantidad)
            print("Entro BD 2")





        opc=input("-> ")
        if (opc=="1"):
            x=1
            self.dbActual=x
            print("Se a predeterminado Mysql")
            print("")
        elif(opc=="2"):
            x=2
            self.dbActual=x
            print("Se a predeterminado MongoDB")
            print("")


if __name__ == "__main__":
    x=Menu()
    x.menuPR()