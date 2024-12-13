# aventura_pkg/utils.py
from rich.console import Console
import os

console = Console()

def imprime_instrucoes():
    """Lê e exibe as instruções do jogo formatadas."""
    caminho_arquivo = os.path.join("assets", "instrucoes.txt")
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            console.print(f"[bold cyan]{conteudo}[/]")
    except FileNotFoundError:
        console.print("[bold red]Arquivo instrucoes.txt não encontrado![/]")
    except Exception as e:
        console.print(f"[bold red]Erro ao ler o arquivo: {e}[/]")

def imprimir_menu():
    """Exibe o menu principal."""
    console.print("[bold magenta]Menu Principal[/]")
    console.print("1. Jogar")
    console.print("2. Instruções")
    console.print("3. Sair")


