# Pandas
"""
Biblioteca para el analisis y manipulacion de datos. Proporciona herramientas para 
trabajar con grandes volumenes de informacion, como tablas, series temporables,
datos tabulares, similares a una hoja de calculo

Leer/Escribir CSV, Excel, JSON, SQL, etc.
Filtra, ordena y agrupa datos
Limpia y transforma datos
Manejar datos faltantes
Realizar operaciones estadisticas y matematicas

pip install pandas
"""
import pandas as pd
import charts
import utils
import read_csv

def run():

    # de donde se obtiene la información
    df = pd.read_csv('data.csv') # lo pasa a una tabla

    # Mostrar la tabla
    # print(df)
    
    # Filtrar los datos - Solo obtener suramerica
    df = df[df['Continent'] == 'Africa']
    # print(df)

    # Obtener los países y porcentajes
    countries = df['Country'].values
    percentages = df['World Population Percentage'].values

    # grafico

    charts.generate_pie_chart(countries, percentages)
  
    country = input('Type Country => ')
    # print(country)

    data = read_csv.read_csv('data.csv')
    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        print(country)
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country'], labels, values)
    


if __name__ == '__main__':
    run()
