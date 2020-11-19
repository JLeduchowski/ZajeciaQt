import Cell
import Map
from CellState import CellState
import Game

if __name__ == '__main__':

    g1 = Game.Game()
    # g1.gameMap.showMapConsole()
    # print(f'')
    # g1.checkCell(2,2)
    # for i in range(1, g1.gameMap.size + 1):
    #     print(f'')
    #     for y in range(1, g1.gameMap.size + 1):
    #         print(f'{g1.gameMap.map[i][y].mineIndicator} ', end = "")
    g1.gameMap.showMapConsole()

    print(f'')

    string = input('Podaj wspolrzedne odkrywki (x,y) ')
    while string != "quit":
        stringsplit = string.split(',')
        x = int(stringsplit[0])
        y = int(stringsplit[1])
        # print(f'{x},{y}')
        g1.checkCell(x,y)
        g1.gameMap.showMapConsole()
        string = input('Podaj wspolrzedne odkrywki (x,y) ')








