import requests


def envia_arquivo():
    # Caminho do arquivo que vamos enviar;
    path = 'C:/Users/mathe/Desktop/data_cleaner/scripts/Planilha_base.xlsx'

    # Envia arquivo (postando arquivos) ;
    '''url: endereço de postagem web, files: definição dos arquivos que deverão ser postados
    (cria um "dict" onde a chave se chama 'file', o valor é definido pelo método 'open()', 
    passamos então como argumento o 'path' do arquivo, e passamos também o argumento 'rb' que basicamente
     le o arquivo como binário, a fim de economizar memória.'''
    requisicao = requests.post('https://file.io', files={'file': open(path, 'rb')})

    '''Na variável 'saida_requisicao' nós transformamos a variável 'requisicao' para o formato json, a fim de
    estruturá-lo como se fosse um dict e facilitar trabalhar com o arquivo'''
    saida_requisicao = requisicao.json()

    '''O formato json é um formato parecido com um dict, ou seja, quando precisamos  acessar alguma informação em específico
    devemos acessar através da chave, assim como faríamos em um dicionário, por exemplo'''
    url = saida_requisicao['link']
    print(f'Arquivo enviado. Link para acesso: {url}')


def envia_arquivo_chave():
    # Essa técnica consiste em enviarmos o arquivo para o servidor diretamente para nossa conta através da KEY;
    path = 'C:/Users/mathe/Desktop/data_cleaner/scripts/Planilha_base.xlsx' # Caminho do arquivo que enviaremos;
    chave_de_acesso = '3P5KRB7.GSRE882-JD74ES4-N7Y4VRN-C4FHYG6' # A chave de acesso que geramos na nossa conta;

    # requisicao = request.postar(nesse site, este arquivo, utilizando essa credencial);
    requisicao = requests.post(url='https://file.io', # URL da postagem;
                              files={'file' : open(path, 'rb')}, # Arquivo a ser postado;
                              headers={'Authorization' : chave_de_acesso}) # Credencial;

    saida_requisicao = requisicao.json() # Retorno do processo;
    print(saida_requisicao)
    url = saida_requisicao['link'] # Selecionamos apenas o link de download do arquivo;
    print(f'Arquivo enviado com chave. Link para acesso: {url}') # Mostramos o link na tela;


def recebe_arquivo(file_url):
    # Receber o arquivo;
    requisicao = requests.get(file_url)

    if requisicao.ok: # Se conseguirmos o URL do arquivo
        # Salvar o arquivo;
        with open('C:/Users/mathe/Desktop/data_cleaner/scripts/Planilha_base.xlsx', 'wb') as file: # Abrimos o arquivo e salvamos suas informações na variável file;
            file.write(requisicao.content) # Escrevemos o conteúdo do arquivo;
        print('Arquivo baixado com sucesso!')
    else: # Se não conseguirmos o URL do arquivo;
        print(f'Erro ao baixar o arquivo!{requisicao.json()}') # Mostramos uma mensagem de erro e mostramos o conteúdo da requisição;


#envia_arquivo()
recebe_arquivo('https://file.io/JxTCZp3tbY2r')
#envia_arquivo_chave()