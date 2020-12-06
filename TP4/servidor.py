import socket
import json
HOST = 'localhost'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT)) #vinculamos com o socket com o host e port
s.listen() #modo de esculta
print('Aguardando conexão de um cliente')

conn, ender = s.accept() #aceitar a coneccao e dps endereco

print('Conectado em', ender) #mostra na tela o endereco conectado

while True:
    data = conn.recv(1024)
    if not data: #quando nao tiver mais nada
        print('Fechando a conexão')
        conn.close()
        break
    conn.sendall(data) #enviando de volta os dados para o cliente

def escrever_jason(dados): #criar o arquivo
    with open('meu_arquivo.json', 'w',encoding='utf8') as f: #cria o arquivo json
        json.dump(dados,f,ensure_ascii=False, sort_keys=True, indent=4,separators=(',',':')) #cria garantindo alguns paramentros para a organização da informação

meu_dict ={ #informações para o json
    'Disciplina': 'Redes de Computadores 2',
    "Professor": 'Alessandro Vivas',
    "Aluno1":'Beatriz',
    "Aluno2":'Amanda', 
    "Aluno3":'Caliny',
    "Aluno4": 'Pietro'
}

escrever_jason(meu_dict) #gerar o arquivo