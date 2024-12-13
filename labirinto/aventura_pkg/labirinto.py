""""
Contém funções relacionadas à criação e exibição do labirinto.
"""
from random import shuffle, choice
from rich.console import Console
from rich.table import Table

console = Console()

def criar_labirinto(linhas, colunas):
    """Gera um labirinto com apenas um caminho para a saída."""
    labirinto = [["#" for _ in range(colunas)] for _ in range(linhas)]
    
    direcoes = [(-2, 0), (2, 0), (0, -2), (0, 2)]

    def dentro_do_labirinto(x, y):
        """Verifica se a célula está dentro dos limites do labirinto."""
        return 0 <= x < linhas and 0 <= y < colunas

    def criar_caminho(x, y):
        """Cria um caminho recursivamente a partir da posição atual."""
        labirinto[x][y] = " "
        shuffle(direcoes)
        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy
            wx, wy = x + dx // 2, y + dy // 2
            if dentro_do_labirinto(nx, ny) and labirinto[nx][ny] == "#":
                labirinto[wx][wy] = " "
                criar_caminho(nx, ny)

    criar_caminho(0, 0)

    saida_x, saida_y = linhas - 1, colunas - 1
    labirinto[saida_x][saida_y] = "X"
    if labirinto[saida_x - 1][saida_y] == "#" and labirinto[saida_x][saida_y - 1] == "#":
        labirinto[saida_x - 1][saida_y] = " "
    elif labirinto[saida_x - 1][saida_y] == "#":
        labirinto[saida_x - 1][saida_y] = " "
    elif labirinto[saida_x][saida_y - 1] == "#":
        labirinto[saida_x][saida_y - 1] = " "

    labirinto[0][0] = "J"

    return labirinto

def imprimir_labirinto(labirinto: list) -> None:
    """Imprime o labirinto formatado no terminal."""
    console.clear()
    table = Table(show_header=False, box=None, padding=(0, 1))

    for linha in labirinto:
        row = []
        for celula in linha:
            if celula == "#":
                row.append("[bold red]#[/]")
            elif celula == "J":
                row.append("[bold yellow]J[/]")
            elif celula == "*":
                row.append("[bold green]*[/]")
            elif celula == "X":
                row.append("[bold blue]X[/]")
            else:
                row.append(" ")
        table.add_row(*row)
    
    console.print(table)
