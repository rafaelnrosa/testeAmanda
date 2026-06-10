# Acho que no geral o código funcionou bem, gostei do resultado e da ideia.
import random

# Constantes do tabuleiro
ROWS = 6
COLS = 7
EMPTY = '.'
PLAYER_X = 'X'
PLAYER_O = 'O'


def create_board():
    """Inicializa o tabuleiro vazio com 6 linhas e 7 colunas."""
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]


def print_board(board):
    """Exibe o tabuleiro na tela, com os índices de 0 a 6 no topo."""
    print("0 1 2 3 4 5 6")
    for r in range(ROWS):
        print(" ".join(board[r]))
    print()  # Linha em branco para separar os turnos


def is_valid_location(board, col):
    """Verifica se a coluna escolhida é válida e não está cheia."""
    if 0 <= col < COLS:
        # Se a linha do topo da coluna estiver vazia, ainda cabe peça
        return board[0][col] == EMPTY
    return False


def get_next_open_row(board, col):
    """Simula a gravidade: encontra a linha mais baixa vazia na coluna."""
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == EMPTY:
            return r
    return -1


def drop_piece(board, row, col, piece):
    """Coloca a peça (X ou O) na linha e coluna especificadas."""
    board[row][col] = piece


def check_win(board, piece):
    """Verifica se há 4 peças iguais consecutivas."""
    # Verifica vitória na Horizontal
    for c in range(COLS - 3):
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Verifica vitória na Vertical
    for c in range(COLS):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Verifica vitória na Diagonal Positiva (inclinada para cima)
    for c in range(COLS - 3):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Verifica vitória na Diagonal Negativa (inclinada para baixo)
    for c in range(COLS - 3):
        for r in range(3, ROWS):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

    return False


def is_board_full(board):
    """Verifica se o tabuleiro inteiro está preenchido."""
    for c in range(COLS):
        if board[0][c] == EMPTY:
            return False
    return True


def main():
    print("=== CONNECT FOUR ===")
    print("Modo de Jogo: Humano x Computador")
    print()

    modo = '2'  # Modo fixo: Humano x Computador

    board = create_board()
    game_over = False
    turn = 0  # 0 para Jogador X, 1 para Jogador O

    while not game_over:
        print_board(board)

        # Configura o jogador atual e sua respectiva peça
        if turn == 0:
            current_player = "Jogador 1"
            piece = PLAYER_X
        else:
            current_player = "Computador" if modo == '2' else "Jogador 2"
            piece = PLAYER_O

        # Fase de Leitura de Jogada
        if current_player == "Computador":
            print("O Computador está jogando...")
            # Pega todas as colunas que ainda têm espaço
            valid_cols = [c for c in range(
                COLS) if is_valid_location(board, c)]
            col = random.choice(valid_cols)
        else:
            try:
                col = int(
                    input(f"{current_player} ({piece}), escolha uma coluna (0-6): "))
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.\n")
                continue

            # Verifica se a jogada é aceita
            if not is_valid_location(board, col):
                print(
                    "Jogada inválida! Coluna cheia ou índice inexistente. Tente novamente.\n")
                continue

        # Processamento da Jogada
        row = get_next_open_row(board, col)
        drop_piece(board, row, col, piece)

        # Condição de Fim de Jogo: Vitória
        if check_win(board, piece):
            print_board(board)
            if current_player == "Computador":
                print("Computador venceu!")
            else:
                print(f"Jogador {piece} venceu!")
            game_over = True

        # Condição de Fim de Jogo: Empate
        elif is_board_full(board):
            print_board(board)
            print("Empate! Nenhum jogador venceu.")
            game_over = True

        # Alterna o turno para o próximo jogador
        turn = (turn + 1) % 2


if __name__ == "__main__":
    main()
