#Exercises - Day 13
print()

# L2-2 - Usa map() para crear una nueva lista que cambie cada número por su cuadrado en la lista de números.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def Cuadrado(x):
    return x ** 2

NumerosAlCuadrado = map(Cuadrado, numbers)
print(list(NumerosAlCuadrado))
print()