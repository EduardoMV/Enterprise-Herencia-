class Empresa:

    def __init__(self, nombre, puesto, antiguedad, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.antiguedad = antiguedad
        self.salario = salario

    def trabajar(self):
        print(f"\n {self.nombre} está trabajando cómo {self.puesto}")

class Gerente(Empresa):
    def __init__(self, nombre, puesto, antiguedad, salario):
        super().__init__(nombre, puesto, antiguedad, salario)
        self.salario = 50000

    def persona(self):
        print(f"\n {self.nombre} tiene {self.antiguedad} años en la empresa y cuenta con un salario de ${self.salario}")

    def salary(self, aumento, Usuario2):
        Usuario2.salario = self.salario + aumento
        print(f"El nuevo salario del {self.puesto} {self.nombre} {self.salario}")

    def trabajar(self):
        return super().trabajar()
            

class Programador(Gerente):
    def __init__(self, nombre, puesto, antiguedad, salario):
        super().__init__(nombre, puesto, antiguedad, salario)
        self.salario = salario + (antiguedad2 * 1000) 
        
    def persona(self):
        return super().persona()

    def trabajar(self):
        return super().trabajar()


class Asistente(Empresa):
    def __init__(self, nombre, puesto, antiguedad, salario):
        super().__init__(nombre, puesto, antiguedad, salario)
        self.salario = salario + (antiguedad3 * 1000) 

    def persona(self):
        print(f"\n {self.nombre} tiene {self.antiguedad} años en la empresa y cuenta con un salario de ${self.salario}")
    
    def trabajar(self):
        return super().trabajar()

    
nombre = input("\nIngresa el nombre: ")
puesto = input("Ingresa el puesto: ")
antiguedad = int(input("Ingresa la antiguedad: "))


Usuario = Gerente(nombre, puesto, antiguedad, "50000")
Usuario.persona()
Usuario.trabajar()


nombre2 = input("\nIngresa el nombre: ")
puesto2 = input("Ingresa el puesto: ")
antiguedad2 = int(input("Ingresa la antiguedad: "))

Usuario2 = Programador(nombre2, puesto2, antiguedad2 , 25000)
Usuario2.persona()
Usuario2.trabajar()


nombre3 = input("\nIngresa el nombre: ")
puesto3 = input("Ingresa el puesto: ")
antiguedad3 = int(input("Ingresa la antiguedad: "))

Usuario3 = Asistente(nombre3, puesto3, antiguedad3, 15000)
Usuario3.persona()
Usuario3.trabajar()

aumento = int(input("\nIngresa el aumento para el programador: $"))
Usuario2.salary(aumento, Usuario2)