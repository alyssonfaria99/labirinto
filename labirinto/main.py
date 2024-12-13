from pynput.keyboard import Listener, Key
from rich.console import Console
from aventura_pkg.labirinto import criar_labirinto, imprimir_labirinto
from aventura_pkg.jogador import iniciar_jogador, mover, atualizar_labirinto
from aventura_pkg.utils import imprime_instrucoes

console = Console()

def exibir_menu():
    """Exibe o menu inicial e retorna a escolha do jogador."""
    console.print("[bold magenta]--- Menu Inicial ---[/]")
    console.print("[1] Jogar")
    console.print("[2] Instruções")
    console.print("[3] Sair")
    escolha = input("Escolha uma opção: ").strip()
    return escolha

def finalizar_jogo_com_sucesso():
    """Exibe uma mensagem de sucesso e encerra o jogo."""
    console.print("\n[bold green]🎉 Parabéns! Você encontrou a saída do labirinto! 🎉[/]\n")
    console.print("[bold blue]Obrigado por jogar![/]")
    exit(0) 

def verificar_saida(jogador, saida, listener):
    """Verifica se o jogador alcançou a posição da saída."""
    if tuple(jogador["posicao"]) == saida:
        listener.stop()
        finalizar_jogo_com_sucesso()

def iniciar_jogo():
    """Inicia o jogo principal."""
    linhas, colunas = 10, 10
    labirinto = criar_labirinto(linhas, colunas)
    jogador = iniciar_jogador()
    saida = (linhas - 1, colunas - 1)

    def on_press(tecla):
        nonlocal jogador, labirinto
        try:
            if hasattr(tecla, 'char') and tecla.char in ["w", "a", "s", "d"]:
                jogador = mover(jogador, tecla.char, labirinto)
                labirinto = atualizar_labirinto(jogador, labirinto)
                imprimir_labirinto(labirinto)
                verificar_saida(jogador, saida, listener)
            elif tecla == Key.esc:
                console.print("[bold red]Jogo encerrado pelo jogador.[/]")
                listener.stop()
                exit(0)
        except Exception as e:
            console.print(f"[bold red]Erro ao processar o movimento: {e}[/]")

    console.print("[bold magenta]Use W, A, S, D para mover pelo labirinto. Pressione ESC para sair.[/]")
    imprimir_labirinto(labirinto)

    with Listener(on_press=on_press) as listener:
        listener.join()

def main():
    while True:
        escolha = exibir_menu()
        if escolha == "1":
            iniciar_jogo()
            return
        elif escolha == "2":
            imprime_instrucoes()
        elif escolha == "3":
            console.print("[bold cyan]Obrigado por jogar! Até a próxima![/]")
            exit(0)
        else:
            console.print("[bold red]Opção inválida. Tente novamente![/]")

if __name__ == "__main__":
    main()
