import json
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