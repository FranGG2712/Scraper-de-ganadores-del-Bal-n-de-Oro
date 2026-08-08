import pandas as pd
import re
import requests
from bs4 import BeautifulSoup as BS


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'es-ES,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}

respuesta = requests.get('https://es.wikipedia.org/wiki/Balón_de_Oro',headers=headers)
respuesta.status_code

u = respuesta.text
soup = BS(u, 'html.parser')

tabla = soup.find('table', class_= 'wikitable')
filas = tabla.find_all('tr')
len(filas)

datos = []                          

for fila in filas[2:]:              
    celda = fila.find_all('td')
    if len(celda) < 3:      
        continue
    
    jugador_club = celda[1].text

    year = celda[0].text.strip()
    jugador = jugador_club.split("(")[0].strip()
    club = re.search(r"\((.*?)\)", jugador_club).group(1)
    puntos = celda[2].text.strip()

    year = re.sub(r"\[(\d+)\]",'',year)
    jugador = re.sub(r"\[(\d+)\]",'',jugador)
    club = re.sub(r"\[(\d+)\]",'',club)
    puntos = re.sub(r"\[(\d+)\]",'',puntos)


    datos.append({               
        'Año': year,
        'Jugador': jugador,
        'Club': club,
        'Puntos': puntos
    })


tabla = pd.DataFrame(datos)
tabla.to_csv('balon_de_oro.csv',index=False,encoding='utf-8-sig')
tabla