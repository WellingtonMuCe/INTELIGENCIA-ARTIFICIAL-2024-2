pila = []

   pila.append(23)
   pila.append(100)
   pila.append(25)

   
print('Actualizacion del contenedor antes del pop {aux1}')
for elem in pila:
    print(elem)

aux1=pila.pop()

print('Ultimo elemento que se muestra {aux1}')

print('Actualizacion del contenedor despues del pop {aux1}')
    for elem in pila:
    print(elem)

aux2=pila[-1]

print('el ultimo elemento {aux2}')

print('Actualizacion del contenedor despues de [-1]')
    for elem in pila:
    print(elem)


    