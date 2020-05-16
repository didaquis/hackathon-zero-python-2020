"""
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.

Escribe un programa que comience leyendo el número de barras vendidas que no son del día.  Después tu programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
"""

price_of_loave = 3.49

discount = 1 - 0.6

price_with_dicount = price_of_loave * discount

number_of_loaves = input('Write the number of selled loaves: ') # Caution: input always return a string!

number_of_loaves = int(number_of_loaves) # Convert string to integer

print('Normal price ' + str (price_of_loave))
print('discount ' + str (price_with_dicount))
print('Final price ' + str (number_of_loaves * price_with_dicount))