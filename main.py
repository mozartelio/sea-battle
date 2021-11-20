import json
from enum import Enum


class Map_cell_state(Enum):
    EMPTY_STATE = 0
    LONELY_SHIP_STATE = 1
    MIDDLE_SHIP_SECTION = 2
    HORIZONTAL_LEFT_EDGE = 3
    HORIZONTAL_RIGHT_EDGE = 4
    VERTICAL_TOP_EDGE = 5
    VERTICAL_BOTTOM_EDGE = 6

class Game_state(Enum):
    PLAYING = 0
    GAME_CLOSED = 1
    SOLVED = 2
    FAILED = 3

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,   0,   0)
BLUE = (  0,   0, 255)

NUMBER_OF_CELLS = 10
BLOCK_SIZE = 20
LEFT_INDENT = 100
UPPER_INDENT = 10


our_first_map_file = open('maps.json', )

all_maps_data = json.load(our_first_map_file)



for k in range(1, 3):
    for x in range(0, NUMBER_OF_CELLS):
        for y in range(0, NUMBER_OF_CELLS):
            print(all_maps_data[str(k)][x][y] + " ", end='')
        print('\n')

    print('\n')

# print(map_data["1"][0][8])

our_first_map_file.close()
