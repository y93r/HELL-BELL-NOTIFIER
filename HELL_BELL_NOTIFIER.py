#bibliotecas
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from plyer import notification
import time
from datetime import datetime

#URL do feed de notícias do Whiplash
url = "https://whiplash.net/feeds/news.xml"

#Adicionar um User-Agent para evitar bloqueios
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
request = Request(url, headers=headers)

#Ler os dados da URL no formato XML
response = urlopen(request)
dados_xml = response.read()
response.close()

#Usar BeautifulSoup para extrair os dados do arquivo XML
sp = BeautifulSoup(dados_xml, "xml")
lista_noticias = sp.find_all("item")
lista_noticias = lista_noticias[0:11]  #Pegar as notícias de 0 a 10

#Iterar pelas notícias extraídas e mostrar notificações
for noticias in lista_noticias:
    pub_date = noticias.pubDate.text
    #Converter para um objeto datetime
    date_obj = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %z")
    #Converter para o formato brasileiro (dd/mm/aaaa HH:MM)
    date_br = date_obj.strftime("%d/%m/%Y %H:%M")
    notification.notify(
        title= "HELL BELL NOTIFIER",
        message= noticias.title.text +
                 "\nPublicado em: " + date_br,
        timeout=2
    )

    time.sleep(10)
