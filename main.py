# Munir Lucio da Costa Bisteni - RA:23023844

import json
import random

jogo = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

# Lê linha a linha, caso haja duas casas com o valor igual a 1 ou duas casas com o valor igual a 2  retorna a posição que ainda está com 0
# Se estiver com as 3 posições da linha com números iguais retorna "fim de jogo"
def conferir_linha(jogo):
    for i in range(3):
        if jogo[i][0] == jogo[i][1] == jogo[i][2] != 0:
            return "fim de jogo"
        if jogo[i].count(1) == 2 and jogo[i].count(0) == 1:
            return (i, jogo[i].index(0))
        if jogo[i].count(2) == 2 and jogo[i].count(0) == 1:
            return (i, jogo[i].index(0))
    return None


# Lê coluna a coluna, caso haja duas casas com o valor igual a 1  ou duas casas com o valor igual a 2  retorna a posição que ainda está com 0
# Se estiver com as 3 posições da coluna números iguais retorna "fim de jogo"
def conferir_coluna(jogo):
    for j in range(3):
        col = [jogo[i][j] for i in range(3)]
        if col[0] == col[1] == col[2] != 0:
            return "fim de jogo"
        if col.count(1) == 2 and col.count(0) == 1:
            return (col.index(0), j)
        if col.count(2) == 2 and col.count(0) == 1:
            return (col.index(0), j)
    return None


# Lê as duas diagonais existentes no jogo,caso haja duas casas com o valor igual a 1  ou duas casas com o valor igual a 2  retorna a posição que ainda está com 0
# Se estiver com as 3 posições da diagonal números iguais retorna "fim de jogo"
def conferir_diagonal(jogo):
    diag1 = [jogo[i][i] for i in range(3)]
    diag2 = [jogo[i][2-i] for i in range(3)]
    
    if diag1[0] == diag1[1] == diag1[2] != 0 or diag2[0] == diag2[1] == diag2[2] != 0:
        return "fim de jogo"
    
    if diag1.count(1) == 2 and diag1.count(0) == 1:
        return (diag1.index(0), diag1.index(0))
    if diag1.count(2) == 2 and diag1.count(0) == 1:
        return (diag1.index(0), diag1.index(0))
    
    if diag2.count(1) == 2 and diag2.count(0) == 1:
        return (diag2.index(0), 2-diag2.index(0))
    if diag2.count(2) == 2 and diag2.count(0) == 1:
        return (diag2.index(0), 2-diag2.index(0))
    
    return None


# Verifica se não resta nenhuma casa igual a 0, caso não exista, retorna True, else False
def conferir_velha(jogo):
    for linha in jogo:
        if 0 in linha:
            return False
    return True


# Adiciona a jogada (estrutura de dados jogo) no arquivo jogo-da-velha.json
def salvar_jogada(jogo, arquivo='jogo-da-velha.json'):
    try:
        with open(arquivo, 'r') as f:
            res = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        res = {}
    
    jogada_num = len(res)
    res[f'jogada {jogada_num}'] = [linha[:] for linha in jogo] 
    
    with open(arquivo, 'w') as f:
        json.dump(res, f, indent=4, separators=(',', ':'))


# Zera o arquivo para uma próxima vez
def limpar_arquivo(arquivo='jogo-da-velha.json'):
    with open(arquivo, 'w') as f:
        f.write('')


# Mostra a estutura de dados "jogo" na formatação de jogo da velha
def mostrar_tabuleiro(jogo):
    for linha in jogo:
        print(" | ".join(str(x) for x in linha))
        print("-" * 9)



def computador_jogar(jogo):
    # Verificar se o computador pode ganhar
    for i in range(3):
        for j in range(3):
            if jogo[i][j] == 0:
                jogo[i][j] = 2
                if conferir_linha(jogo) == "fim de jogo" or conferir_coluna(jogo) == "fim de jogo" or conferir_diagonal(jogo) == "fim de jogo":
                    return
                jogo[i][j] = 0

    # Verificar se o computador precisa bloquear o jogador
    for i in range(3):
        for j in range(3):
            if jogo[i][j] == 0:
                jogo[i][j] = 1
                if conferir_linha(jogo) == "fim de jogo" or conferir_coluna(jogo) == "fim de jogo" or conferir_diagonal(jogo) == "fim de jogo":
                    jogo[i][j] = 2
                    return
                jogo[i][j] = 0

    # Fazer uma jogada aleatória
    while True:
        i, j = random.randint(0, 2), random.randint(0, 2)
        if jogo[i][j] == 0:
            jogo[i][j] = 2
            return

def jogar():
    limpar_arquivo()

    # Jogador humano começa
    jogador = 1  
    
    while True:
        mostrar_tabuleiro(jogo)
        
        if jogador == 1:
            try:
                linha = int(input("Jogador 1, digite a linha (0-2): "))
                coluna = int(input("Jogador 1, digite a coluna (0-2): "))
                
                if linha not in range(3) or coluna not in range(3):
                    raise ValueError("Posição inválida. Escolha entre 0 e 2 para linha e coluna.")
                
                if jogo[linha][coluna] != 0:
                    raise ValueError("Posição já ocupada. Escolha outra.")
                
                jogo[linha][coluna] = 1
                
            except ValueError as e:
                print(e)
                continue
        else:
            print("Computador está jogando...")
            computador_jogar(jogo)
        
        # Salvar estado do jogo
        salvar_jogada(jogo)
        
        # Verificar se alguém ganhou
        if conferir_linha(jogo) == "fim de jogo" or conferir_coluna(jogo) == "fim de jogo" or conferir_diagonal(jogo) == "fim de jogo":
            mostrar_tabuleiro(jogo)
            if jogador == 1:
                print("Jogador 1 venceu!")
            else:
                print("Computador venceu!")
            break
        
        # Verificar empate
        if conferir_velha(jogo):
            mostrar_tabuleiro(jogo)
            print("Empate! O jogo terminou em velha.")
            break
        
        # Alternar jogador
        jogador = 1 if jogador == 2 else 2

# Iniciar o jogo
jogar()