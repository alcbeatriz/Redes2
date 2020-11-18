import socket #usado para enviar dados através da rede
portas_abertas = []
host = input('Digite o ip: ') #pega o IP a conferir

for porta in range(1,65535):#Há 65535 portas tcp,irá verificar quais estão abertas
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #criação do SOCKET, toda vez que é executado, uma nova conexão será feita no alvo (tcp)
    s.settimeout(0.001) #tempo

    if s.connect_ex((host, porta)) == 0: #verifica a conexao
        portas_abertas.append(porta)#pra informar a quantidade de portas estão abertas
        print("Porta",porta, "aberta!") #printa se aberta, quando a conexão é realizada 
    else:
        pass

print("TOTAL DE PORTAS ABERTAS: %s"%portas_abertas)
s.close() #finaliza a conexão