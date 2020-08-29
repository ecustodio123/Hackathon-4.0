from time import sleep
from Es import escuela

data = {}
data['estudiantes_creados'] = []
data_1 = {}
data_1['docentes_creados'] = []

notas = []

class Estudiante():
    def __init__(self, dni, nombre, edad, cargo):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo

    def configurar_estudiante(self):
        print(""""\n Por favor indique si usted es Alumno o Docente\n
                1) Alumno
                2) Docente\n""")
        cargo = input("> ")
        if cargo == "1":
            cargo = "Alumno"
            self.crear_estudiante(cargo)
        elif cargo == "2":
            cargo = "Docente"
            self.crear_estudiante(cargo)
        else:
            print("\nOpción no valida")

    def crear_estudiante(self, cargo):
        dni = input("\nPor favor introduzca su DNI: ")
        nombre = input("\nPor favor introduzca su Nombre: ")
        edad = input("\nPor favor introduzca su Edad: ")
        nuevo_estudiante = Estudiante(dni,nombre,edad,cargo)
        datos = {
                "DNI" : nuevo_estudiante.dni,
                "Nombre" : nuevo_estudiante.nombre,
                "Edad" : nuevo_estudiante.edad,
                "Cargo" : nuevo_estudiante.cargo
            }
        self.guardar_estudiante(datos)




        print(f"\nSe ha registrado a {nombre}")
        

    def guardar_estudiante(self, datos):

        notas = []

        if (datos['Cargo'] == "Alumno"):

            for i in range(4):

                nota = int(input(f"Por favor ingrese la nota {i + 1}: "))
                notas.append(nota)
            
            nota_promedio = sum(notas) / len(notas)

            # data["estudiantes_creados"].append(datos)
            # data["estudiantes_creados"].append(notas)
            # data["estudiantes_creados"].append(min(notas))
            # data["estudiantes_creados"].append(max(notas))
            # data["estudiantes_creados"].append(nota_promedio)
            
            # est = str(data["estudiantes_creados"])
            archivo = open("alumnos.txt", "a+")
            archivo.write(f"-Alumno: {datos['DNI']}, {datos['Nombre']}, {datos['Edad']}, {notas}, {max(notas)}, {min(notas)}, {nota_promedio}\n")
            # archivo.write(est)
            archivo.close()

        elif(datos['Cargo'] == "Docente"):
            # data_1["docentes_creados"].append(datos)
            # doc = str(data_1["docentes_creados"])
            # print(doc)
            archivo = open("docente.txt", "a+")
            archivo.write(f"-Docente: {datos['DNI']}, {datos['Nombre']}, {datos['Edad']}\n")
            # archivo.write(doc)
            archivo.close()
            
    def interfaz(self):
        while True:
            print("""\n¡Bienvenido al colegio Pachaqtec! Por favor indique que desea hacer?
            1) Registrarse en nuestra base de datos
            2) Salir del programa\n""")
            opcion = input("> ")
            if opcion == "1":
                self.configurar_estudiante()
            elif opcion == "2":
                print("\nGracias por usar esta aplicacion")
                sleep(2)
                quit()
            else:
                print("\nHas introducido una opción erronea")


class Iniciar(Estudiante):
    def __init__(self):
        self.interfaz()

Iniciar()