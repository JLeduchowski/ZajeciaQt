import Cell
import random

class Map(object):

    def __init__(self, size, mines):
        self.size = size
        self.mines = mines
        self.map = []
        Map.initMap(self)
        Map.gameMines(self, 3, 3)
        #Map.testGameMines(self)

    def initMap(self):
        for i in range(self.size+2):
            self.map.append([])
            for y in range(self.size+2):
                self.map[i].append(Cell.Cell())
                if i == 0 or i == self.size + 1 or y == 0 or y == self.size + 1:
                    self.map[i][y].isBorder = True


    def showMap(self):
       for i in range(1, self.size+1):
           for y in range(1, self.size+1):
               print(f'{self.map[i][y].state}')

    def showMapConsole(self):
       for i in range(1, self.size+1):
           print(f'')
           for y in range(1, self.size+1):
               if self.map[i][y].isBomb:
                   print(f'b ', end=''),
               else:
                   if self.map[i][y].mineIndicator == 0:
                     print(f'{self.map[i][y].state.value} ', end =''),
                   else:
                       print(f'{self.map[i][y].mineIndicator} ', end=''),

    def showMines(self):
       for i in range(1, self.size+1):
           for y in range(1, self.size+1):
               print(f'{i},{y} {self.map[i][y].isBomb}')

    # def testGameMines(self):
    #     self.map[4][2].setIsBomb(True)
    #     self.map[1][4].setIsBomb(True)
    #     self.map[6][1].setIsBomb(True)
    #     self.map[6][2].setIsBomb(True)
    #     self.map[6][7].setIsBomb(True)
    #     self.map[7][2].setIsBomb(True)
    #     self.map[2][8].setIsBomb(True)
    #     self.map[4][7].setIsBomb(True)
    #     self.map[8][6].setIsBomb(True)
    #     self.map[8][5].setIsBomb(True)

    def gameMines(self, x, y):
        # bedzie generowac bomby w miejscach roznych od x y (1 wybor gracza)

        for i in range(self.mines):
            num1 = random.randint(1, self.size)
            num2 = random.randint(1, self.size)
            print(f'{num1},{num2}')
            while self.map[num1][num2].getIsBomb():
                print(f'szukam bombie nowego miejsca')
                num1 = random.randint(1, self.size)
                num2 = random.randint(1, self.size)
                print(f'{num1},{num2}')
            self.map[num1][num2].setIsBomb(True)
            print(f'wstawiono bombe na {num1},{num2}')

    def setSize(self,size):
        self.size = size

    def getSize(self):
        return self.size

    def setMines(self, mines):
        self.mines = mines

    def getMines(self):
        return self.mines

    def setGameMap(self, map):
        self.map = map

    def getGameMap(self):
        return self.map








