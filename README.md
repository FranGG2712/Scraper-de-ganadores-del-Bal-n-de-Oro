# Scraper de ganadores del Balón de Oro

Mi primer proyecto es un scraper de los ganadores del Balón de Oro, desde el primero (año 1956) hasta el último (2025), ganado por Dembélé.

Extrae desde Wikipedia todos los ganadores del título y los exporta a un archivo CSV. También está la opción de ver la tabla desde el código: solo tenés que llamar a la variable `tabla`.

Utilizo expresiones regulares para limpiar los datos, como por ejemplo los `[ ]` que aparecen como referencias. Además, salteo el año 2020, ya que no hubo entrega de premios debido al Covid-19.

El CSV tiene 70 filas: 1 de encabezado (Año, Jugador, Club, Puntos) y 69 de ganadores.

## Requisitos

- Python 3.10 o superior
- pandas
- requests
- beautifulsoup4

## Cómo ejecutarlo

```
pip install pandas requests beautifulsoup4
python Balon_de_oro.ipynb
```

## Notas

Proyecto de práctica hecho a mano, quería probar mis habilidades de scraping y limpieza de datos. Es mi primer proyecto, y ojalá el primero de muchos que en el futuro me consigan trabajo. :)

Fecha: 08-08-2026

# Análisis de puntos por ganadores del Balón de Oro 
## Esto es parte del proyecto 2 (el gráfico)
Se ve claro como en 2021, 2022 y 2023 los puntos son bajos y es debido a cambiaron el sistema de puntuaciones en los años posteriores. 
Antes cada periodista podía votar su top 5 y los puntos se distribuían así: Top 5 → 6, 4, 3, 2, 1.
Después de 2023 los periodistas pasaron a votar a su top 10 y cambiaron la cantidad de puntos que recibía cada puesto: Top 10 → 15, 12, 10, 8, 7, 5, 4, 3, 2, 1
Algo clave para contar es que en 2021 votaban 170 periodistas, en 2022 ese numero se redujo a 100. Pero en 2023 solo votaron 92, el resto no votó.

