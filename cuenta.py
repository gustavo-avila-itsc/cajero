import csv

class Cliente():
    def __init__(self):
        self.nombre = None
        self.apellido = None
        self.dni = None
        self.edad = None
        self.numcliente=None
        
    def personas(self,cliente):  
        with open ('personas.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            
            
            for row in reader:
                if row['Numcliente'] == cliente:
                    
                
                    self.nombre= row['Nombre']
                    self.apellido =row['Apellido']
                    self.dni =row['DNI']
                    self.edad =row['Edad']
                    self.numcliente =row['Numcliente']
                    print self.nombre
                    print self.apellido
                    print self.edad
                    print self.dni
                    print self.numcliente
                    return "continuar"
               
            
            print "el cliente no existe"
            return "exit"

class Cuenta():
    def __init__(self,cliente,cont):

        with open ('cuentas.csv') as csvfile:
            reader = csv.DictReader(csvfile)
    
            for row in reader:
                if row['numcliente'] == cliente and row['contrasenia'] == cont:
                    self.numcliente=row['numcliente']
                    self.saldo=row['saldo']
                    

                    
                    
    def consultar(self):
        print self.saldo
            
    def agregar_din_cuenta(self,din): 
        self.saldo=int(self.saldo)+din
        print "se han agregado  $", din, "a su cuenta"
        print "saldo: ", self.saldo
    def extraer_din_cuenta(self,din):
        if din <= self.saldo:
            self.saldo=int(self.saldo)-din
            print "se han extraido  $", din, "a su cuenta"
            print "saldo: ", self.saldo
        else:
            print "no puede extraer  $", din
            print "su saldo es de $", self.saldo
    

def cajero():
    salir = 0
    con=""
    
    c=raw_input("ingrese el numero de cliente: ")
    a=Cliente()
    persona=a.personas(c)
    if persona=="exit":
        salir = 1
    if salir == 0:
        con=raw_input("ingrese la contrasenia: ")
    
    b=Cuenta(c,con)

    while salir == 0:
        tarea=raw_input("ELIJA UNA DE LAS OPCIONES: --consultar saldo-- --depositar dinero-- --extraer dinero-- --salir-- :")
        if tarea == "consultar saldo":
            b.consultar()
        if tarea == "depositar dinero":
            dinero=int(raw_input("ingrese cantidad de dinero a depositar: "))
            b.agregar_din_cuenta(dinero)
        if tarea == "extraer dinero":
            dinero=int(raw_input("ingrese cantidad de dinero a extraer: "))
            b.extraer_din_cuenta(dinero)
        if tarea == "salir":
            salir = 1
