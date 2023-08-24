import pandas as pd
import matplotlib.pyplot as plt
lista = pd.read_csv('archivo_1.csv')

print(lista)
print()

#Suma de Ingresos

total_ingresos = lista['ingresos'].sum()
print('total de ingresos es de ', total_ingresos)
print()
#promedio en las edades

promedio_edades = lista['edad'].mean()
print('el promedio en las edades es ', promedio_edades)
print()
#filtro de los que viven en trujillo

ciudad = 'Trujillo'

registros_filtrados = lista[lista['ciudad'] == ciudad]
print('personas que solo viven en trujillo')
print(registros_filtrados)
print()

#Promedio de ingresos por ciudad
promedios_por_ciudad = lista.groupby('ciudad')['ingresos'].mean()
print('promedio de ingresos por ciudad')
print(promedios_por_ciudad)
print()

#persona mayor, persona menor

# Encuentra la persona más joven
persona_mas_joven = lista[lista['edad'] == lista['edad'].min()]
print('persona mas joven')
print(persona_mas_joven)

# Encuentra la persona mayor
persona_mayor = lista[lista['edad'] == lista['edad'].max()]
print('persona mayor')
print(persona_mayor)

# conteo por ciudad
conteo_por_ciudad = lista['ciudad'].value_counts()
print('conteo por ciudad')
print(conteo_por_ciudad)
print()
# Ordena las edades de la más joven a la mayor
edades_ordenadas = lista.sort_values(by='edad')
print('edades ordenadas')
print(edades_ordenadas)
print()

#filtrar mayores a 30a y sacar el promedio
mayores_30 = lista[lista['edad'] > 30]
promedio = mayores_30['edad'].mean()
print('mayores de 30 años y con promedio', promedio)
print()

#ingresos totales por ciudad
ingresos_totales_por_ciudad = lista.groupby('ciudad')['ingresos'].sum()
print('ingresos totales por ciudad')
print(ingresos_totales_por_ciudad)
print()

#promedio de ingresos menores a 30
menores_30 = lista[lista['edad'] < 300]
promedio = menores_30['ingresos'].mean()
print('el promedio de ingresos de los menores de 30 años es ', promedio)

#el que gana mas
gana_mas = lista[lista['ingresos'] == lista['ingresos'].max()]
print('Mayor Ingresos')
print(gana_mas)


#ingresos por ciudad
suma_ciudad = lista.groupby('ciudad')['ingresos'].sum()
print('Suma por ciudad')
print(suma_ciudad)
print()


#promedio de edades por ciudad

promedio_edades_ciudad = lista.groupby('ciudad')['edad'].mean()
print('promedio edades por ciudad')
print(promedio_edades_ciudad)
print()

#ciudades con ingresos promedio superiores a 3000
mayores_3000 = lista[lista['ingresos'] > 3000]
promedio_mayores_3000 = mayores_3000.groupby('ciudad')['ingresos'].mean()
print('Ciudades con ingresos a 3000 promedio')
print(promedio_mayores_3000)
print()

#agregar columna de impuestos del 11%

def calcular_impuestos(ingresos):
    # Define la tasa de impuestos
    tasa_impuestos = 0.11
    
    # Calcula los impuestos como un porcentaje de los ingresos
    impuestos = ingresos * tasa_impuestos
    return impuestos

# Agrega una columna de impuestos al DataFrame
lista['impuestos'] = lista['ingresos'].apply(calcular_impuestos)

print(lista)
#ordenar por ingresos de forma decendente

ingresos_ordenados = lista.sort_values(by='ingresos', ascending=False)
print('forma decendente')
print(ingresos_ordenados)

#grafico pastel por numero de trabajadores por ciudad

trabajadores_por_ciudad = lista['ciudad'].value_counts()

plt.figure(figsize=(8, 6))  
plt.pie(trabajadores_por_ciudad, labels=trabajadores_por_ciudad.index, autopct='%1.0f', startangle=140)
plt.axis('equal') 

plt.title('Distribución de Trabajadores por Ciudad')
plt.show()

# Crea un histograma de las edades
plt.hist(lista['edad'], bins=10, edgecolor='black')

plt.xlabel('Edad')
plt.ylabel('Cantidad de Personas')
plt.title('Distribución de Edades')

plt.show()


