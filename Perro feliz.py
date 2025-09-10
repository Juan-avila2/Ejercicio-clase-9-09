#Autor: Juan Felipe Avila Rodriguez
#Acariciar, pasear, comer


class Perro:
    def __init__(self, nombre, raza, color):
        self.nombre = nombre
        self.raza = raza
        self.color = color
        self.comer = False
        self.pasear = False
        self.acariciar = False

    def ladrar(self):
        print(f"{self.nombre} está ladrando, Gof! Gof! Gof!")
    
    def feliz(self):
        if self.comer and self.pasear and self.acariciar:
            print(f"{self.nombre} está feliz de que seas su dueño.")
        else:
            print(f"{self.nombre} está triste, aún necesita cuidados.")
    
    def preguntar_estado(self):
        print("Ahora veamos los cuidados de su perro")
        self.comer = input("¿El perro ha comido? (si/no): ").lower() == "si"
        self.pasear = input("¿El perro ha paseado? (si/no): ").lower() == "si"
        self.acariciar = input("¿El perro ha sido acariciado? (si/no): ").lower() == "si"

    

print("Ingrese los datos del perro")
nombre_perro = input("Nombre del perro: ")
raza_perro = input("Raza del perro: ")
color_perro = input("Color del perro: ")

perro = Perro(nombre_perro, raza_perro, color_perro)
perro.preguntar_estado()
perro.feliz()


