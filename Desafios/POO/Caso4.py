"""Realizar una clase que administre una agenda
Se debe almacenar para cada contacto el nombre, el teléfono y el email
Además deberá mostrar un menú con las siguientes opciones
Añadir contacto
Lista de contactos
Buscar contacto
Editar contacto
Cerrar agenda"""

class Agenda:
    def __init__(self,nombre="",telefono=0,email=""):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.contactos = []
    
    def añadirContacto(self):
        persona1=Agenda(input("ingrese nombre "),input("Ingrese telefono "),input("Ingrese email "))
        self.contactos.append(persona1)

    def listadeContactos(self):
        for i in self.contactos:
            print(i.nombre)
            print(i.telefono)
            print(i.email)
            print("*******************")

    def buscarContacto(self,nom):
        for i in self.contactos:
            if(nom==i.nombre):
                print(i.nombre)
                print(i.telefono)
                print(i.email)
            else:
                print("No se encontro contacto")
    
    def editarContacto(self):
        editar = input("De quien desea editar? ")
        for i in self.contactos:
            if(editar==i.nombre):
                que =input("Que desea editar de juan ")
                if(que.capitalize()=="Nombre"):
                    i.nombre=input("Ingrese nuevo valor para nombre ")
                    print(i.nombre)
                elif(que.capitalize()=="Telefono"):
                    i.telefono=input("Ingrese nuevo valor para nombre ")
                    print(i.telefono)
                elif(que.capitalize()=="Email"):
                    i.email=input("Ingrese nuevo valor para nombre ")
                    print(i.email)

def agenda():
    contactos=Agenda()
    seguir="Si"
    print("1_Añadir contacto")
    print("2_Lista de contactos")
    print("3_Buscar contacto")
    print("4_Editar contacto")
    print("5_Cerrar agenda")
    accion = input("\nQue desea hacer? (1-5) ")
    while seguir =="Si":
        if(accion=="1"):
            contactos.añadirContacto()
            accion = input("\nQue desea hacer? (1-5) ")
        elif(accion=="2"):
            contactos.listadeContactos()
            accion = input("\nQue desea hacer? (1-5) ")
        elif(accion=="3"):
            contactos.buscarContacto(input("Ingrese el nombre de quein busca "))
            accion = input("\nQue desea hacer? (1-5) ")
        elif(accion=="4"):
            contactos.editarContacto()
            accion = input("\nQue desea hacer? (1-5) ")
        elif(accion=="5"):
            seguir="No"
        else:
            print("Ingrese solo las opciones de 1-5")
            accion = input("\nQue desea hacer? (1-5) ")

agenda()