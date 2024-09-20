from bs4 import BeautifulSoup
import requests

url = 'https://wiki.python.org.br/AprendaMais'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

def conta_tag():
    contador_titulo = 0
    contator_paragrafo = 0
    for linha in extracao.find_all('h2'): # Seleciona e conta quantidade de títulos h2;
        if linha.name == 'h2': # Se o nome (ou tag) da linha for h2;
            contador_titulo += 1
    print(f'Total de titulos: {contador_titulo}')

    for linha in extracao.find_all('p'): # Seleciona e conta a quantidade de parágrafos;
        if linha.name == 'p': # Se o nome (ou tag) da linha for p;
            contator_paragrafo += 1
    print(f'Total de parágrafos: {contator_paragrafo}')

def coleta_texto():
    for texto in extracao.find_all(['h2', 'p']):
        if texto.name == 'h2':
            titulo = texto
            print(f'Titulo: \n{titulo}')
        elif texto.name == 'p':
            paragrafo = texto
            print(f'Parágrafo: \n{paragrafo}')

def coleta_aninhada():
    for titulo in extracao.find_all('h2'): # Localiza todos os títulos 'h2';
        print(f'Titulo: \n {titulo.text.strip()}') # Mostra na tela todos os títulos 'h2';
        for link in titulo.find_next_siblings('p'): # Realiza um segundo loop buscando por todas as tags 'p' irmãs dentro da tag atual (no caso, h2);
            for a in link.find_all('a'): # Finalmente busca por todas as tags 'a' do arquivo html;
                print(f'Link do texto: {a.text.split()} URL: {a["href"]}')

if __name__ == '__main__':
    coleta_aninhada()


'''
Obs: O método de coleta aninhada permite a navegação por dentro das tags HTML para buscar valores específicos aninhados;
'''