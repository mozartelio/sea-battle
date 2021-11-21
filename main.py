import pygame
import random
import json
from enum import Enum
import sys

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

MAP_NUMBER = str(2)

our_first_map_file = open('maps.json', )

all_maps_data = json.load(our_first_map_file)



for k in range(1, 3):
    for x in range(0, NUMBER_OF_CELLS):
        for y in range(0, NUMBER_OF_CELLS):
            print(all_maps_data[str(k)][x][y] + " ", end='')
        print('\n')

    print('\n')




# print(map_data["1"][0][8])

######

def draw_ships():
    x_block_center= LEFT_INDENT + BLOCK_SIZE / 2
    y_block_center= UPPER_INDENT + BLOCK_SIZE / 2
    circle_radius=8


    img_vertical_top_edge = pygame.transform.scale(pygame.image.load('assets/VERTICAL_TOP_EDGE.png'), (16, 16))
    img_vertical_bottom_edge = pygame.transform.scale(pygame.image.load('assets/VERTICAL_BOTTOM_EDGE.png'), (16, 16))

    img_horizontal_left_edge = pygame.transform.scale(pygame.image.load('assets/HORIZONTAL_LEFT_EDGE.png'), (16, 16))
    img_horizontal_right_edge = pygame.transform.scale(pygame.image.load('assets/HORIZONTAL_RIGHT_EDGE.png'), (16, 16))

    for x  in range(0, NUMBER_OF_CELLS):
        for y  in range(0, NUMBER_OF_CELLS):

            if all_maps_data[MAP_NUMBER][y][x] == str(Map_cell_state.LONELY_SHIP_STATE.value):
                pygame.draw.circle(screen, BLACK, (x_block_center, y_block_center), circle_radius)

            elif all_maps_data[MAP_NUMBER][y][x] == str(Map_cell_state.MIDDLE_SHIP_SECTION.value):
                pygame.draw.rect(screen, BLACK, (x_block_center - 7, y_block_center - 7, 15, 15))

            elif all_maps_data[MAP_NUMBER][y][x] == str(Map_cell_state.VERTICAL_TOP_EDGE.value):
                screen.blit(img_vertical_top_edge,(x_block_center-circle_radius, y_block_center-circle_radius ))

            elif all_maps_data[MAP_NUMBER][y][x] == str(Map_cell_state.VERTICAL_BOTTOM_EDGE.value):
                screen.blit(img_vertical_bottom_edge,(x_block_center-circle_radius, y_block_center-circle_radius ))

            elif all_maps_data[MAP_NUMBER][y][x] == str(Map_cell_state.HORIZONTAL_LEFT_EDGE.value):
                screen.blit(img_horizontal_left_edge, (x_block_center - circle_radius, y_block_center - circle_radius))

            elif all_maps_data[MAP_NUMBER][y][x] == str(Map_cell_state.HORIZONTAL_RIGHT_EDGE.value):
                screen.blit(img_horizontal_right_edge, (x_block_center - circle_radius, y_block_center - circle_radius))
            elif all_maps_data[MAP_NUMBER][y][x] != str(Map_cell_state.EMPTY_STATE.value):
                sys.stderr.write('Problem in draw_ships(), not declared new cell state!\n')
                
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

    screen.fill(WHITE)
    draw_grid()
    pygame.display.update()

    # map_to_state_transfer()
    # for i in range(0,10):
    #     for z in range (0,10):
    #         print(str(arr[z][i].value) + " " , end='')
    #     print('\n')

    draw_ships()
    pygame.display.update()


    while game_state==Game_state.PLAYING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = Game_state.GAME_CLOSED


main()
pygame.quit()


our_first_map_file.close()
