import json
from os import system
from bd import MysqlDatabase
from bd import MongoDatabase

class Articulo:
    bd=""
    ListaArticulos = []
    data = {}
    data['ListaPrestamos'] = []

    vacio = {}
    vacio['ListaPrestamos'] = []

    def __init__(self,matricula=None, articulo=None, cantidad=None):
        self.matricula      = matricula
        self.articulo       = articulo
        self.cantidad     = cantidad
        
    def limpiar():
        system("cls")

    def RegistroArticulo(self,matricula, articulo, cantidad):
        newArticulo = Articulo(matricula,articulo, cantidad)
        self.ListaArticulos.append(newArticulo)
        self.data['ListaPrestamos'].append(encoderArticulo(newArticulo))
        with open('Registro.json', 'w') as file:
            json.dump(self.data, file, indent=4)
        print('Registrado :)\n')
        return newArticulo

    def VerArticulos(self):
        return self.ListaArticulos


    def CargarArticulos(self):
        with open('Registro.json') as f:
            listillaJSON = json.load(f)
        for li in listillaJSON['ListaPrestamos']:
            newArticulo = Articulo(li['matricula'],li['articulo'],li['cantidad'])
            self.ListaArticulos.append(newArticulo)
            self.data['ListaPrestamos'].append(encoderArticulo(newArticulo))
        print('Datos cargados\n')
        return self.ListaArticulos

    def CargarArticulosReemplazado(self):  #reemplaza el jason por los diccionar
        with open('Registro.json', 'w') as file:
            json.dump(self.data, file, indent=4)
        print("Cargado....")
        Articulo.limpiar()

    def DevolucionesPrestamos(self):
        print('Ingrese su #/Pres para eliminar')
        elimInt=int(input("->"))
        if elimInt==0:
          return
        x=(elimInt-1)
        print(x)
        del self.ListaArticulos[x]
        del self.data["ListaPrestamos"][x]
        print("Se ha realizado la debolucion satisfactoriamente")
        tmp=Articulo()
        tmp.CargarArticulosReemplazado()


'''
    def verBdActual(self):
        print(self.bd)
    def seleccionarBD(self,eleccion):
        print("Selecciona la Base de datos por defecto")
        print('1.- Configurar con MySQL')
        print('2.- Configurar con MongoDB')
        if eleccion==1:
            self.bd="MySQL" 
        elif eleccion==2:
            self.bd="MongoDB"
    def guardarDatosBD(self,x,y,z):
        if self.bd=="MySQL" :
          tmp=MysqlDatabase()
          tmp.insertarDatos(x,y,z)
        elif self.bd=="MongoDB" :
          pass  
'''


def encoderArticulo(articulo):
        if isinstance(articulo,Articulo):
            return {
            'matricula'  : articulo.matricula,
            'articulo'   : articulo.articulo,
            'cantidad' : articulo.cantidad
            }
        raise TypeError(f'El objeto {articulo} no es de tipo Persona')



