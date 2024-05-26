# Munir Lucio da Costa Bisteni - RA:23023844

# Jogo da Velha em Python

Este é um simples jogo da velha implementado em Python. O jogo permite que um jogador humano jogue contra o computador. O computador utiliza uma estratégia básica para fazer suas jogadas.

## Descrição do Processo

O jogo segue os seguintes passos:

1. **Inicialização do Jogo**:
   - O tabuleiro é representado por uma matriz 3x3, inicialmente preenchida com zeros.

2. **Jogada do Jogador Humano**:
   - O jogador humano faz uma jogada digitando as coordenadas da linha e coluna desejadas (valores de 0 a 2).

3. **Jogada do Computador**:
   - O computador faz sua jogada de acordo com uma estratégia simples:
     - Primeiro, verifica se pode ganhar.
     - Em seguida, verifica se precisa bloquear o jogador humano.
     - Se nenhuma dessas condições for atendida, faz uma jogada aleatória.

4. **Verificação do Fim do Jogo**:
   - Após cada jogada, o jogo verifica se há um vencedor ou se o jogo terminou em empate.
     - Verifica-se se alguma linha, coluna ou diagonal contém três valores iguais.
     - Se não houver mais casas vazias no tabuleiro, o jogo termina em empate.

5. **Salvamento do Estado do Jogo**:
   - O estado do jogo após cada jogada é salvo em um arquivo JSON para permitir a retomada do jogo em outro momento.

6. **Finalização do Jogo**:
   - Quando um jogador vence ou o jogo termina em empate, a partida é encerrada e o resultado é exibido.

## Como Jogar

1. Clone este repositório em seu computador.
2. Execute o arquivo `jogo_da_velha.py` em um ambiente Python.
3. Siga as instruções no terminal para fazer suas jogadas.


## Explicação dos Métodos

1. **`conferir_linha(jogo)`**:
   - Esta função verifica se há alguma linha no jogo que contenha duas casas com o mesmo valor (1 ou 2) e uma casa vazia (0). Se sim, retorna a posição da casa vazia.
   - Se todas as casas em uma linha tiverem o mesmo valor (1 ou 2) e não forem vazias, indica o fim do jogo.
   - Retorna `None` se nenhuma das condições for atendida.

2. **`conferir_coluna(jogo)`**:
   - Similar à função anterior, porém verifica colunas em vez de linhas.
   - Retorna a posição da casa vazia se as condições forem atendidas, indicando que o computador ou o jogador humano pode ganhar.
   - Retorna "fim de jogo" se todas as casas em uma coluna tiverem o mesmo valor e não forem vazias.

3. **`conferir_diagonal(jogo)`**:
   - Esta função verifica as duas diagonais do jogo, buscando padrões semelhantes às funções de linha e coluna.
   - Retorna a posição da casa vazia se as condições forem atendidas ou "fim de jogo" se todas as casas em uma diagonal tiverem o mesmo valor.

4. **`conferir_velha(jogo)`**:
   - Verifica se não há mais casas vazias no jogo, indicando um empate.
   - Retorna True se não houver mais casas vazias e False caso contrário.

5. **`salvar_jogada(jogo, arquivo='jogo-da-velha.json')`**:
   - Adiciona a jogada atual ao arquivo JSON especificado, que armazena o histórico de jogadas.

6. **`limpar_arquivo(arquivo='jogo-da-velha.json')`**:
   - Limpa o conteúdo do arquivo JSON, pronto para um novo jogo.

7. **`mostrar_tabuleiro(jogo)`**:
   - Exibe o estado atual do jogo na forma de um tabuleiro de jogo da velha.

8. **`computador_jogar(jogo)`**:
   - Lógica para que o computador faça sua jogada.
   - Prioriza ganhar, bloquear o jogador humano ou faz uma jogada aleatória.

9. **`jogar()`**:
   - Função principal que controla a sequência do jogo.
   - Alternadamente, permite que o jogador humano e o computador façam suas jogadas até que haja um vencedor ou empate.
