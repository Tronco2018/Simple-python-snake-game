import curses
from copy import copy
from random import randint
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
curses.initscr()
finestra = curses.newwin(30, 60, 0, 0)
finestra.keypad(True)
finestra.border(0)
finestra.timeout(10)
snake = [[15,13], [15,12], [15,11]]
cibo = [5,35]
doveGuardo = KEY_DOWN
punti = 0
finestra.addch(cibo[0], cibo[1], 'O')

while True: 
    finestra.addstr(0, 14, 'Score: ' + str(punti) + ' ')
    tasto = finestra.getch()
    if tasto != -1:
        doveGuardo = tasto
    
    nuovaTesta = copy(snake[0])
   
    
    
    if doveGuardo == KEY_DOWN:
        nuovaTesta[0] += 1
    elif doveGuardo == KEY_UP:
        nuovaTesta[0] -= 1
    elif doveGuardo == KEY_RIGHT:
        nuovaTesta[1] += 1
    elif doveGuardo == KEY_LEFT:
        nuovaTesta[1] -= 1
    
    snake.insert(0, nuovaTesta)
    
    
    
    if snake [0][0] == 0 or snake [0][0] == 29 or snake [0][1] == 0 or snake [0][1] == 59:
        break
    
    if snake[0] in snake[1:]:
        break
    
    if snake[0] == cibo:
        cibo = []
        punti += 1
        while cibo == []:
            cibo = [randint(1, 28), randint(1, 58)]
            if cibo in snake:
                cibo = []
        finestra.addch(cibo[0], cibo[1], 'O')
    
    else:
        ultimoPezzo = snake.pop()
        finestra.addch(ultimoPezzo[0], ultimoPezzo[1], ' ')
    
    finestra.addch(snake[0][0], snake[0][1], 'x')

curses.endwin()
print("\n GAME OVER! Your score is: " + str(punti))
