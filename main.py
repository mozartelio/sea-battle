import pygame
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
RED = (255, 0, 0)
BLUE = (0, 0, 255)

NUMBER_OF_CELLS = 10
BLOCK_SIZE = 20
LEFT_INDENT = 100
UPPER_INDENT = 10

MAP_NUMBER = str(1)

our_first_map_file = open('maps.json', )

all_maps_data = json.load(our_first_map_file)
all_maps_data_copy = all_maps_data.copy()

img_vertical_top_edge = pygame.transform.scale(pygame.image.load('assets/VERTICAL_TOP_EDGE.png'), (16, 16))
img_vertical_bottom_edge = pygame.transform.scale(pygame.image.load('assets/VERTICAL_BOTTOM_EDGE.png'), (16, 16))

img_horizontal_left_edge = pygame.transform.scale(pygame.image.load('assets/HORIZONTAL_LEFT_EDGE.png'), (16, 16))
img_horizontal_right_edge = pygame.transform.scale(pygame.image.load('assets/HORIZONTAL_RIGHT_EDGE.png'), (16, 16))

for k in range(1, 3):
    for x in range(0, NUMBER_OF_CELLS):
        for y in range(0, NUMBER_OF_CELLS):
            print(all_maps_data[str(k)][x][y] + " ", end='')
        print('\n')

    print('\n')

# print(map_data["1"][0][8])



vertical_ship_counter = [0] * NUMBER_OF_CELLS
horizontal_ship_counter = [0] * NUMBER_OF_CELLS

def flotila_plavidel(screen, img_horizontal_left_edge,img_horizontal_right_edge):
    font = pygame.font.SysFont('arial', font_size)
    text = font.render('Flotila plavidel:', True, BLACK)
    textRect = text.get_rect()
    textRect.center = (7*LEFT_INDENT,UPPER_INDENT)
    screen.blit(text, textRect)
    for i in range(1, NUMBER_OF_CELLS):
        if i < 7:
            screen.blit(img_horizontal_left_edge, (6.65* LEFT_INDENT, UPPER_INDENT + i * BLOCK_SIZE-5))
            if i < 4:
                pygame.draw.rect(screen, BLACK, (int(6.75*LEFT_INDENT + 9), int(UPPER_INDENT + i * BLOCK_SIZE-4), 15, 15))
                if i < 2:
                    pygame.draw.rect(screen, BLACK,(int(6.75 * LEFT_INDENT + 27), int(UPPER_INDENT + i * BLOCK_SIZE - 4), 15, 15))
                    screen.blit(img_horizontal_right_edge,(6.65 * LEFT_INDENT + 54, UPPER_INDENT + i * BLOCK_SIZE - 5))
                if i > 1 and i < 4:
                    screen.blit(img_horizontal_right_edge,(6.65 * LEFT_INDENT + 36.5, UPPER_INDENT + i * BLOCK_SIZE - 5))
            if i > 3 and i < 7:
                screen.blit(img_horizontal_right_edge, (6.65 * LEFT_INDENT + 18.5, UPPER_INDENT + i * BLOCK_SIZE - 5))
        if i > 5:
            pygame.draw.circle(screen, BLACK, (6.75*LEFT_INDENT, UPPER_INDENT + (i+1)* BLOCK_SIZE+2), 8)


def fill_vertical_or_horizontal_ship_counter(vertical):
    for row in range(0, NUMBER_OF_CELLS):
        for column in range(0, NUMBER_OF_CELLS):
            match int(all_maps_data[MAP_NUMBER][row if vertical else column][column if vertical else row]):
                case Map_cell_state.LONELY_SHIP_STATE.value | Map_cell_state.MIDDLE_SHIP_SECTION.value | \
                     Map_cell_state.HORIZONTAL_LEFT_EDGE.value | Map_cell_state.HORIZONTAL_RIGHT_EDGE.value | \
                     Map_cell_state.VERTICAL_TOP_EDGE.value | Map_cell_state.VERTICAL_BOTTOM_EDGE.value:
                    if vertical:
                        vertical_ship_counter[row] += 1
                    else:
                        horizontal_ship_counter[row] += 1

                case Map_cell_state.EMPTY_STATE.value:
                    pass

                case _:
                    sys.stderr.write('Problem in fill_vertical_or_horizontal_ship_counter(), ' +
                                     'not declared new cell state with number:' +
                                     str(all_maps_data[MAP_NUMBER][column][row]) + '\n')



dfska_field =[["0" for x in range(NUMBER_OF_CELLS)] for y in range(NUMBER_OF_CELLS)]
# 'x' as cross
def cross_maker():
    for row in range(0, NUMBER_OF_CELLS):
        for column in range(0, NUMBER_OF_CELLS):

            if horizontal_ship_counter[column]==0 and dfska_field[row][column]!="x":
                dfska_field[row][column] = "x"
            if vertical_ship_counter[row]==0 and dfska_field[row][column] != "x":
                dfska_field[row][column] = "x"
            else:
                # match int(all_maps_data[MAP_NUMBER][row][column]):
                    # case:


                for xr in range(0, NUMBER_OF_CELLS):
                    for yr in range(0, NUMBER_OF_CELLS):
                        print(str(dfska_field[xr][yr]) + " ", end='')
                    print('\n')
                print('\n')
                print("row: " + str(row) + " column: " + str(column))


######
def treeer():
    for i in range(0, NUMBER_OF_CELLS):
        for j in range(0, NUMBER_OF_CELLS):
            if (int(all_maps_data_copy[MAP_NUMBER][i][j])) != 0:
                # count+=1
                dfska(i, j)


# def dfska():


# def dfs(i, j):
#     if i < 0 or i >= NUMBER_OF_CELLS or j < 0 or j >= NUMBER_OF_CELLS or all_maps_data_copy[MAP_NUMBER][i][j] == 0:
#         return
#     all_maps_data_copy[MAP_NUMBER][i][j] = 0
#     dfs(i + 1, j)
#     dfs(i - 1, j)
#     dfs(i, j + 1)
#     dfs(i, j - 1)


# def board_mover():
#     count=0
#     for i in range (0, NUMBER_OF_CELLS):
#         for j in range (0, NUMBER_OF_CELLS):
#             if(int(all_maps_data_copy[MAP_NUMBER][i][j]))!=0:
#                 count+=1
#                 dfs(i,j)
######


def draw_ships():
    x_block_center = LEFT_INDENT + BLOCK_SIZE / 2
    y_block_center = UPPER_INDENT + BLOCK_SIZE / 2
    circle_radius = 8

    img_vertical_top_edge = pygame.transform.scale(pygame.image.load('assets/VERTICAL_TOP_EDGE.png'), (16, 16))
    img_vertical_bottom_edge = pygame.transform.scale(pygame.image.load('assets/VERTICAL_BOTTOM_EDGE.png'), (16, 16))

    img_horizontal_left_edge = pygame.transform.scale(pygame.image.load('assets/HORIZONTAL_LEFT_EDGE.png'), (16, 16))
    img_horizontal_right_edge = pygame.transform.scale(pygame.image.load('assets/HORIZONTAL_RIGHT_EDGE.png'), (16, 16))

    for x in range(0, NUMBER_OF_CELLS):
        for y in range(0, NUMBER_OF_CELLS):

            match int(all_maps_data[MAP_NUMBER][y][x]):
                case Map_cell_state.LONELY_SHIP_STATE.value:
                    pygame.draw.circle(screen, BLACK, (x_block_center, y_block_center), circle_radius)
                case Map_cell_state.MIDDLE_SHIP_SECTION.value:
                    pygame.draw.rect(screen, BLACK, (int(x_block_center - 7), int(y_block_center - 7), 15, 15))
                case Map_cell_state.VERTICAL_TOP_EDGE.value:
                    screen.blit(img_vertical_top_edge, (x_block_center - circle_radius, y_block_center - circle_radius))
                case Map_cell_state.VERTICAL_BOTTOM_EDGE.value:
                    screen.blit(img_vertical_bottom_edge, (x_block_center - circle_radius, y_block_center - circle_radius))
                case Map_cell_state.HORIZONTAL_LEFT_EDGE.value:
                    screen.blit(img_horizontal_left_edge, (x_block_center - circle_radius, y_block_center - circle_radius))
                case Map_cell_state.HORIZONTAL_RIGHT_EDGE.value:
                    screen.blit(img_horizontal_right_edge, (x_block_center - circle_radius, y_block_center - circle_radius))
                case Map_cell_state.EMPTY_STATE.value:
                    pass
                case _:
                        sys.stderr.write('Problem in draw_ships(), ' +
                        'not declared new cell state with number:' +
                         str(all_maps_data[MAP_NUMBER][y][x]) + '\n')
            y_block_center = y_block_center + BLOCK_SIZE
        y_block_center = UPPER_INDENT + BLOCK_SIZE / 2
        x_block_center = x_block_center + BLOCK_SIZE
    pygame.display.update()


def draw_grid():
    for i in range(NUMBER_OF_CELLS + 1):
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
            num_vertical = font.render(str(vertical_ship_counter[i]), True, BLACK)
            num_horizontal = font.render(str(horizontal_ship_counter[i]), True, BLACK)

            # TODO: width and height for both num_vertical and num_horizontal
            # width of rendered numbers
            num_width = num_vertical.get_width()
            # height of rendered numbers
            num_height = num_vertical.get_height()
            # letters_hor_width = letters_hor.get_width()

            # vertical num_vertical grid1
            screen.blit(num_vertical, (3.2 * LEFT_INDENT - (BLOCK_SIZE // 2 + num_width // 2),
                                       UPPER_INDENT + i * BLOCK_SIZE + (BLOCK_SIZE // 2 - num_height // 2)))
            # horizontal letters grid1
            screen.blit(num_horizontal, (
            LEFT_INDENT + i * BLOCK_SIZE + (BLOCK_SIZE // 2 - num_width // 2), UPPER_INDENT + 10 * BLOCK_SIZE))
            # vertical num_vertical grid2
            screen.blit(num_vertical, (3.2 * LEFT_INDENT - (BLOCK_SIZE // 2 + num_width // 2) + 15 *
                                       BLOCK_SIZE, UPPER_INDENT + i * BLOCK_SIZE + (BLOCK_SIZE // 2 - num_height // 2)))
            # horizontal letters grid2
            screen.blit(num_horizontal, (
            LEFT_INDENT + i * BLOCK_SIZE + (BLOCK_SIZE // 2 - num_width // 2) + 15 * BLOCK_SIZE,
            UPPER_INDENT + 10 * BLOCK_SIZE))




size = (LEFT_INDENT + 40 * BLOCK_SIZE, UPPER_INDENT + 15 * BLOCK_SIZE)
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Lode")
font_size = int(BLOCK_SIZE / 1.5)
font = pygame.font.SysFont('arial', font_size)


def main():
    game_state = Game_state.PLAYING

    screen.fill(WHITE)
    fill_vertical_or_horizontal_ship_counter(vertical=False)
    fill_vertical_or_horizontal_ship_counter(vertical=True)
    flotila_plavidel(screen,img_horizontal_left_edge, img_horizontal_right_edge)
    draw_grid()
    pygame.display.update()

    # map_to_state_transfer()
    # for i in range(0,10):
    #     for z in range (0,10):
    #         print(str(arr[z][i].value) + " " , end='')
    #     print('\n')

    draw_ships()
    pygame.display.update()

    # print('\n')
    # print(vertical_ship_counter)
    # cross_maker()

    # board_mover()
    # print(all_maps_data_copy)

    for xq in range(0, NUMBER_OF_CELLS):
        for yq in range(0, NUMBER_OF_CELLS):
            print(str(all_maps_data_copy[MAP_NUMBER][xq][yq]) + " ", end='')
        print('\n')

    # print('\n')

    while game_state == Game_state.PLAYING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = Game_state.GAME_CLOSED


main()
pygame.quit()

our_first_map_file.close()
