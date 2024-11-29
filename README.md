# HELL-BELL-NOTIFIER 🎸🐍🔔

## TECNOLOGIAS USADAS:
- PyCharm Community Edition 2023.1.1
- Python 3.12.0
  - beautifulsoup4==4.12.3
  - lxml==5.3.0
  - plyer==2.1.0
  - soupsieve==2.6
 
## Instalação das bibliotecas
```bash
pip install lxml
pip install plyer
pip install beautifulsoup4
```

## DESENVOLVIMENTO
- Este projeto tem como objetivo criar um notificador de noticias do site Whiplash;
- Usar a url do site whiplash no formato xml através de um RSS Feed;
- Criar um User-Agent, adicionando-o ao cabeçalho da requisição HTTP, assim evitando bloqueios por parte de servidores que rejeitam requisições sem um identificador de navegador;
- Processamento dos dados xml;
- Extração dos dados, buscando elementos contidos na tag <item>;
- Limitar as 10 últimas publicadas;
- Para cada notícia extraída será exibida uma notificação contendo a data de publicação no formato brasileiro e o título da manchete;
- O script faz uma pausa de 10 segundos entre as notificações para garantir que todas sejam exibidas devidamente.
- Após exibir a última notícia, o programa será encerrado automaticamente. 
- Durante a execução, é possível continuar utilizando o computador normalmente para outras atividades, sem interrupções.

## Documentação
[lxml](https://lxml.de/) | [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/) | [Plyer](https://plyer.readthedocs.io/en/latest/#)
