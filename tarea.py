import pandas as pd

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
menores_30 = lista[lista['edad'] < 30]
promedio = menores_30['ingresos'].mean()
print('el promedio de ingresos de los menores de 30 años es ', promedio)
