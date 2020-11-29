import os #Para informações do S.O
import socket #usado para enviar dados através da rede
import multiprocessing #theading
import subprocess #executa programas externos e le suas saídas no código
import platform #verificar a plataforma, abaixo vamos dizer a sua necessidade
portas_abertas = []
if platform.system().lower()=="windows": #para executar o ping no windows
    from ping3 import ping


def ping_rede(tarefa, resultado): # valida o ip, para saber se esta ativo em rede
    DEVNULL = open(os.devnull, 'w') #O caminho do arquivo do dispositivo nulo.
    while True: #enquanto for verdadeiro
        ip = tarefa.get() #a variavel ip recebe a tarefa
        if ip is None: #se ip for vazio ele para
            break
        try:    #tratamento de excessão
            if platform.system().lower()=="windows": #se estiver no windowns
                if(ping(ip)!=None): #se o ping no ip foir diferente de vazio
                    print("Um Ip foi encontrado") #vai informar uma mensagem para sabermos que encontrou um ip, vai repedir toda vez que um ip for encontrado
                    resultado.put(ip) #printa o resultado da verificação 
            else:    
                subprocess.check_call(['ping', '-c1', ip],stdout=DEVNULL) #subprocesso com saída diferente de zero       
                resultado.put(ip) #printa o resultado das saídas
        except:
            pass

def VerificaMeuIp(): # verifica o meu ip na rede e identifica o ip base
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#criação do SOCKET, toda vez que é executado, uma nova conexão será feita no alvo UDP
    s.connect(("8.8.8.8", 80)) #padrao, faz a conexao
    ip = s.getsockname()[0] #faz o IP receber o nome e a porta
    s.close() #finaliza
    return ip #retorna o IP


def MapeamentoRede(pool_size=255): # Mapeia toda a rede e cria os multiprocessos

    listaIp = list() #criação de uma lista para armazenar os IPs

    partesIp = VerificaMeuIp().split('.') #verifica o número decimal que representa as partes do ip, os separa por ponto
    baseIp = partesIp[0] + '.' + partesIp[1] + '.' + partesIp[2] + '.' #concatenação

    
    trabalho = multiprocessing.Queue() #cria a fila 
    resultadoAux = multiprocessing.Queue() #faz a variavel resultadoAux receber o valor armazenado na fila

    pool = [multiprocessing.Process(target=ping_rede, args=( #chegar ao alvo
        trabalho, resultadoAux)) for i in range(pool_size)]

    for p in pool: #pool paraleliza a execução em vários valores de entrada
        p.start()

    
    for i in range(1, 255): #for para percorrer devido o valor da mascara
        trabalho.put(baseIp + '{0}'.format(i)) #cria o valor da base

    for p in pool:
        trabalho.put(None)

    for p in pool:
        p.join()

    while not resultadoAux.empty(): #enquanto o resultadoAux nao estiver vazio
        ip = resultadoAux.get() #ip vai receber o valor
        listaIp.append(ip) #Adiciona a lista

    return listaIp #retorna a lista


if __name__ == '__main__': 

    print('Analisando a a rede, por favor aguarde um momento...')
    lst = MapeamentoRede() #imprime o mapeamento da rede
    print("\nIPs ativos encontados na rede:")
    print(lst) #pega a lista e retorna um vetor com os IPs
    for ip in lst: #para a verificação das portas abertas
        print("\nVerificando o IP: " + ip)
        for porta in range(1, 65535):  # escaneando portas
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #criação do SOCKET, toda vez que é executado, uma nova conexão será feita no alvo (tcp)
            s.settimeout(0.0000000000000000000000000001) #tempo
            if s.connect_ex((ip, porta)) == 0:  #verifica a conexao e se a porta estiver aberta
                print(f"A Porta {porta} está aberta!")#printa seu valor
            else:
                pass
            s.close()

