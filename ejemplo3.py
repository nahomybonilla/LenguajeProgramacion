# crear una lista de numeros
numeros = [1,2,3,4,5]

# imprimir la lista original 
print("Lista original:", numeros)

# acceder a elementos individuales por indice
print(" Primer elemento:", numeros[0])
print(" Ultimo elemento:", numeros[-1])

# remplazar un elemento en la lista
numeros[2] = 10
print("Lisata despues de remplazar el tercero elemento:", numeros)

# agregar un elemento al final de la lista
numeros.append(6)
print("Lista despues de agregar un nuevo elemento:", numeros)

# elinimar un elemento de la lista por valor

numeros.remove(4)
print("Lista despues de eliminar el numero 4:", numeros)

# ordenar la lista de forma ascendente
numeros.sort()
print("Lista en ordenar de forma ascendente:", numeros)

# reventir el orden de la lista
numeros.reverse()
print("Lista en orden descendente:", numeros)

# calcular la longitud den la lista
longitud = len(numeros)
print("Longitud de la lista:", longitud)








