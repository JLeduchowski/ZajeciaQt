# ZajeciaQt

Projekt gry Saper

Gra jednoosobowa polegająca na odkrywaniu planszy w taki sposób aby nie natrafić na losowo generowane miny.
Każde odkryte pole zawiera licznik min które stykają się z danym polem, gracz oznacza potencjalne miejsca min
flagą. Gracz wygrywa gdy każde pole jest odkryte oraz każda mina oflagowana.

Klasy:

CellState.py - klasa odpowiadająca za enumerator stanów pola (uncovered,covered,flagged)

Cell.py - klasa zawierająca CellState.py czyli stan pola, licznik min otaczających pole, czy dane pole
posiada mine i czy jest granicą mapy.

Map.py - klasa zawierająca Cell.py, tablice 2-wymiarową pól, rozmiar mapy, ilość min, inicjalizuje mapę oraz
określa położenie min.

Game.py - klasa zawierająca Map.py, logikę gry (odkrywanie mapy, flagowanie poszczególnych pól, zliczanie min
dookoła pól, wybór poziomu trudności), posiada stoper, licznik pozostałych graczowi flag. 
