from itertools import count
import random


def clear_game_field() :
    '''Возвращает пустое игровое поле 3х3'''
    return [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

def draw_field() :
    '''Выводит текущее игровое поле в консоль'''
    for i in (0,1,2) :
        for j in (0,1,2) :
            print(' ' + game_field[i][j] + ' ', end= '')
            print('|' if j < 2 else '', end='')
        print('\n------------' if i < 2 else '')

def set_field(row, col, tictactoe) :
    '''Вносит Х или 0 в заданную ячейку'''
    if  game_field[row][col] == ' ' :
        game_field[row][col] = tictactoe
    else :
        print('The cell is occupied, select another one')

def select_cell() :
    row = int(input('Select row : ')) - 1
    col = int(input('Select col : ')) - 1
    return [row, col]

def game_over() :
    # проверка на заполнение игрового поля
    if not ' ' in [x for l in game_field for x in l] :
        return True
    # проверка по строкам
    for rows in game_field :
        for sign in signs :
            if rows.count(sign) == 3 :
                return True
    # проверка по столбцам
    for sign in signs :
        for j in (0,1,2) :
            if [game_field[i][j] for i in (0,1,2)].count(sign) == 3 :
                return True
    # проверка по диагоналям
    for sign in signs :
        if sign == game_field[1][1] == game_field[2][2] == game_field[0][0] :
            return True
        if sign == game_field[0][2] == game_field[2][2] == game_field[2][0] :
            return True
    return False
    
def sign_selection() :
    '''Случайным образом определяется чьи крестики, чьи нолики'''
    if random.randint(0, 2) == 0 :
        print('You play by Zeros now')
        return ['0', 'X']
    else :
        print('You play by Crosses now')
        return ['X', '0']

game_field = clear_game_field()
signs = sign_selection()
current_player = 1 if signs[0] == 'X' else 2
draw_field()

while not game_over() :
    if current_player == 1 :
        current_cell = select_cell() 
        set_field(current_cell[0], current_cell[1], signs[current_player - 1])
        draw_field()
        current_player = 2
    else :
        current_cell = select_cell() 
        set_field(current_cell[0], current_cell[1], signs[current_player - 1])
        draw_field()
        current_player = 1

if ' ' in [x for l in game_field for x in l] :
    print('Player ' + str(1 if current_player == 2 else 1) + ' win')
else :
    print('There are no winners')