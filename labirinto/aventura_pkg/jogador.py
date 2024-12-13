""""
Gerencia os processos relacionados à movimentação do jogador no labirinto.
"""

from rich.console import Console

console = Console()

def iniciar_jogador():
    """Inicializa o jogador na posição inicial e a pontuação."""
    return {"posicao": [0, 0], "pontuacao": 0}

def mover(jogador, comando, labirinto):
    """Move o jogador baseado na tecla pressionada."""
    linhas, colunas = len(labirinto), len(labirinto[0])
    x, y = jogador["posicao"]

    if comando == "w" and x> 0 and labirinto[x - 1][y] != "#":
        x -= 1
    elif comando == "s" and x< linhas - 1 and labirinto[x + 1][y] != "#":
        x += 1
    elif comando == "a" and y> 0 and labirinto[x][y - 1] != "#":
        y -= 1
    elif comando == "d" and y< colunas - 1 and labirinto[x][y + 1] != "#":
        y += 1
    else:
        console.print("Movimento inválido!")

    jogador["posicao"] = [x, y]
    return jogador

def atualizar_labirinto(jogador, labirinto):
    """Atualiza o labirinto para e a nova posição do jogador."""
    for i, linha in enumerate(labirinto):
        for j, celula in enumerate(linha):
            if celula == "J":
                labirinto[i][j] = " "

    x, y = jogador["posicao"]
    labirinto[x][y] = "J"
    return labirinto

