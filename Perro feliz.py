#Autor: Juan Felipe Avila Rodriguez
#Acariciar, pasear, comer


class Perro:
    def __init__(self, nombre, raza, color):
        self.nombre = nombre
        self.raza = raza
        self.color = color

    def ladrar(self):
        print(f"{self.nombre} está ladrando, Gof! Gof! Gof!")
    

print("Ingrese los datos del perro")
nombre_perro = input("Nombre del perro: ")
raza_perro = input("Raza del perro: ")
color_perro = input("Color del perro: ")

perro = Perro(nombre_perro, raza_perro, color_perro)
perro.ladrar()