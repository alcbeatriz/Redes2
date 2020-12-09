import json
import socket
HOST = '127.0.0.1'
PORT = 50000 #mesma porta do servidor

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT)) #conectando o servidor
s.sendall(str.encode('Bom dia!')) #enviando a mensagem para o servidor
data = s.recv(1024)
    
print('Mensagem ecoada: ', data.decode())

def ler_json():
    with open('meu_arquivo.json', 'r',encoding='utf8') as f:
        return json.load(f)
data = ler_json()

print(data)