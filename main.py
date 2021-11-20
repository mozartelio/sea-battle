import pygame
import random
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



def draw_ships():
    x_block_center= LEFT_INDENT + BLOCK_SIZE / 2
    y_block_center= UPPER_INDENT + BLOCK_SIZE / 2

    for x  in range(0, NUMBER_OF_CELLS):
        for y  in range(0, NUMBER_OF_CELLS):
            # print(str(x_block_center) + ", " + str(y_block_center))

            if all_maps_data["1"][x][y]=="1":
                pygame.draw.circle(screen, BLACK, (x_block_center, y_block_center), 7)
                pygame.display.update()

            y_block_center= y_block_center + BLOCK_SIZE

        y_block_center= UPPER_INDENT + BLOCK_SIZE / 2
        x_block_center= x_block_center + BLOCK_SIZE

    pygame.display.update()




size = (LEFT_INDENT + 30 * BLOCK_SIZE, UPPER_INDENT + 15 * BLOCK_SIZE)

pygame.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Lode")

font_size = int(BLOCK_SIZE / 1.5)

font = pygame.font.SysFont('arial', font_size)






def draw_grid():
    #letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for i in range(NUMBER_OF_CELLS+1):
        # horizontal grid1
        pygame.draw.line(screen, BLACK, (LEFT_INDENT, UPPER_INDENT + i * BLOCK_SIZE),
                         (LEFT_INDENT + NUMBER_OF_CELLS * BLOCK_SIZE, UPPER_INDENT + i * BLOCK_SIZE), 1)

        # print(str(LEFT_INDENT) + ',' + str(UPPER_INDENT + i * BLOCK_SIZE) + ";", end='')
        # print(str(LEFT_INDENT + 10 * BLOCK_SIZE) + ',' + str(UPPER_INDENT + i * BLOCK_SIZE))
        # print('***')

        # vertical grid1
        pygame.draw.line(screen, BLACK, (LEFT_INDENT + i * BLOCK_SIZE, UPPER_INDENT),
                         (LEFT_INDENT + i * BLOCK_SIZE, UPPER_INDENT + NUMBER_OF_CELLS * BLOCK_SIZE), 1)
        # horizontal grid2
        pygame.draw.line(screen, BLACK, (LEFT_INDENT + 15 * BLOCK_SIZE, UPPER_INDENT +
                                         i * BLOCK_SIZE),
                         (LEFT_INDENT + 25 * BLOCK_SIZE, UPPER_INDENT + i * BLOCK_SIZE), 1)
        # vertical grid2
        pygame.draw.line(screen, BLACK, (LEFT_INDENT + (i + 15) * BLOCK_SIZE, UPPER_INDENT),
                         (LEFT_INDENT + (i + 15) * BLOCK_SIZE, UPPER_INDENT + NUMBER_OF_CELLS * BLOCK_SIZE), 1)

        if i < NUMBER_OF_CELLS:
            num = font.render(str(i + 1), True, BLACK)
            #letters_hor = font.render(letters[i], True, BLACK)

            num_width = num.get_width()
            num_height = num.get_height()
            #letters_hor_width = letters_hor.get_width()

            # vertical num grid1
            screen.blit(num, (3.2 * LEFT_INDENT - (BLOCK_SIZE // 2 + num_width // 2),
                              UPPER_INDENT + i * BLOCK_SIZE + (BLOCK_SIZE // 2 - num_height // 2)))
            # horizontal letters grid1
            screen.blit(num, (LEFT_INDENT + i * BLOCK_SIZE + (BLOCK_SIZE // 2 - num_width // 2), UPPER_INDENT + 10 * BLOCK_SIZE))
            # vertical num grid2
            screen.blit(num, (3.2 * LEFT_INDENT - (BLOCK_SIZE // 2 + num_width // 2) + 15 *
                              BLOCK_SIZE, UPPER_INDENT + i * BLOCK_SIZE + (BLOCK_SIZE // 2 - num_height // 2)))
            # horizontal letters grid2
            screen.blit(num, (LEFT_INDENT + i * BLOCK_SIZE + (BLOCK_SIZE // 2 - num_width // 2) + 15 * BLOCK_SIZE, UPPER_INDENT + 10 * BLOCK_SIZE))


def main():

    game_state=Game_state.PLAYING

    game_over = False
    screen.fill(WHITE)
    draw_grid()
    pygame.display.update()

    draw_ships()
    pygame.display.update()


    while game_state==Game_state.PLAYING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = Game_state.GAME_CLOSED


main()
pygame.quit()


our_first_map_file.close()
