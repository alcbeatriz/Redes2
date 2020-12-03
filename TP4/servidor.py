import socket
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