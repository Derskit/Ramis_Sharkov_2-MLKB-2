def draw_board(board,num):
    print(f" {board[6]}({num[6]})| {board[7]}({num[7]})| {board[8]}({num[8]})")
    print("-----|-----|-----")
    print(f" {board[3]}({num[3]})| {board[4]}({num[4]})| {board[5]}({num[5]})")
    print("-----|-----|-----")
    print(f" {board[0]}({num[0]})| {board[1]}({num[1]})| {board[2]}({num[2]})")
def get_player_move(board,player):
    while True:
        move = input(f'{player}, введите номер клетки: ')
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move) - 1] == ' ':
            return int(move) - 1
        else:
            print('Повторите попытку')
import random
def get_computer_move(board):
    while True:
        move = random.randint(0,8)
        if board[move] == ' ':
            return move
def check_win(board, player):
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] == player:
            return True
    if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
        return True
    return False
def number(board,num):
    for i in range(9):
        if board[i] == 'X' or board[i] == 'O':
            num[i] = ' '
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == 'X' or board[i] == board[i + 3] == board[i + 6] == 'O':
            num[i+3] = '!'
            num[i+6] = '!'
            num[i] = '!'
            return num
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] == 'X' or board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] == 'O':
            num[i*3] = '!'
            num[i*3+1] = '!'
            num[i*3+2] = '!'
            return num
    if board[0] == board[4] == board[8] == 'X' or board[0] == board[4] == board[8] == 'O':
        num[0] = '!'
        num[4] = '!'
        num[8] = '!'
        return num
    if board[2] == board[4] == board[6] == 'X' or board[2] == board[4] == board[6] == 'O':
        num[2] = '!'
        num[4] = '!'
        num[6] = '!'
        return num
    return num
def main():
    board = [' '] * 9
    num = [1,2,3,4,5,6,7,8,9]
    players = ['X', 'O']
    turn = 0
    print('Добро пожаловать в игру')
    while True:
        num = number(board,num)
        draw_board(board,num)
        player = players[turn % 2]
        if player == 'X':
            move = get_player_move(board, player)
        else:
            print(f'Компьютер {player} делает ход')
            move = get_computer_move(board)
        board[move] = player
        if check_win(board, player):
            num = number(board, num)
            draw_board(board,num)
            print(f'Поздравляем! Игрок {player} победил')
            break
        elif ' ' not in board:
            num = number(board,num)
            draw_board(board,num)
            print('Ничья')
            break
        turn += 1
main()
