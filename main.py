from dfs import *
import pygame
import json
from enum import Enum
import sys

from gui import *

MAP_NUMBER = str(3)
NUMBER_OF_CELLS = 10

our_first_map_file = open('maps.json', )
all_maps_data = json.load(our_first_map_file)
all_maps_data_copy = all_maps_data.copy()



class Game_state(Enum):
    PLAYING = 0
    GAME_CLOSED = 1
    SOLVED = 2
    FAILED = 3


#vypis prve 2 mapy
# for k in range(1, 3):
#     for x in range(0, NUMBER_OF_CELLS):
#         for y in range(0, NUMBER_OF_CELLS):
#             print(all_maps_data[str(k)][x][y] + " ", end='')
#         print('\n')
#
#     print('\n')

# print(map_data["1"][0][8])



dfska_field = [["0" for x in range(NUMBER_OF_CELLS)] for y in range(NUMBER_OF_CELLS)]


# 'x' as cross
def cross_maker():
    for row in range(0, NUMBER_OF_CELLS):
        for column in range(0, NUMBER_OF_CELLS):

            if gui.horizontal_ship_counter[column] == 0 and dfska_field[row][column] != "x":
                dfska_field[row][column] = "x"
            if gui.vertical_ship_counter[row] == 0 and dfska_field[row][column] != "x":
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
'''def treeer():
    for i in range(0, NUMBER_OF_CELLS):
        for j in range(0, NUMBER_OF_CELLS):
            if (int(all_maps_data_copy[MAP_NUMBER][i][j])) != 0:
                # count+=1
                dfska(i, j)'''


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


control_field = [[False for xa in range(NUMBER_OF_CELLS)] for ya in range(NUMBER_OF_CELLS)]
control_field[2][2] = True
# control_field[0][3] = True
control_field[0][0] = True
control_field[0][1] = True
control_field[2][1] = True


checking_array = [[False for x in range(NUMBER_OF_CELLS)] for y in range(NUMBER_OF_CELLS)]
for a in range(0, NUMBER_OF_CELLS):
    for b in range(0, NUMBER_OF_CELLS):
        if all_maps_data[MAP_NUMBER][a][b] != "0":
            checking_array[a][b] = True


print(checking_array)

gui=Gui(NUMBER_OF_CELLS,all_maps_data[MAP_NUMBER])
dfs_store=DFS(NUMBER_OF_CELLS, checking_array, gui)

def checker():
    print("PaIZKKKDFAS")
    dfs_store.dfs()
    # gui.draw_ships_algorithm(np.array(checking_array).flatten())


def main():
    game_state = Game_state.PLAYING

    gui.screen.fill(gui.WHITE)
    gui.fill_vertical_or_horizontal_ship_counter(vertical=False)
    gui.fill_vertical_or_horizontal_ship_counter(vertical=True)
    gui.flotila_plavidel(gui.screen, gui.img_horizontal_left_edge, gui.img_horizontal_right_edge)
    gui.draw_grid()

    print(str(dfs_store.one_dimensional_answer_field))
    buttonDFS = Button(gui.screen, gui.BLOCK_SIZE,100, 45, 'DFS', checker)
    buttonMRV = Button(gui.screen, gui.BLOCK_SIZE, 100, 45, 'MRV', print('MRV'))
    # buttonLCV = Button(100, 45)
    # buttonMRV = Button(100, 45)
    buttonDFS.draw(800, 20)
    buttonMRV.draw(800, 80)
    # button.draw(800, 140, 'no name',None)
    # button.draw(800, 200, 'Reset',None)
    # pygame.display.update()

    # map_to_state_transfer()
    # for i in range(0,10):
    #     for z in range (0,10):
    #         print(str(arr[z][i].value) + " " , end='')
    #     print('\n')

    gui.draw_ships()
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
            #
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttonDFS.draw(800, 20)
                buttonMRV.draw(800, 80)
            #     button.draw(800, 20, 'DFS', print("OPA4A"))
            #     button.draw(800, 80, 'no name', None)
            #     button.draw(800, 140, 'no name', None)
            #     button.draw(800, 200, 'Reset', None)
            #     pygame.display.update()
            if event.type == pygame.MOUSEMOTION:
                buttonDFS.draw(800, 20)
                buttonMRV.draw(800, 80)
                # button.draw(800, 20, 'DFS', checker())
                # button.draw(800, 80, 'no name', None)
                # button.draw(800, 140, 'no name', None)
                # button.draw(800, 200, 'Reset', None)
                pygame.display.update()


main()
# dfs_class = DFS(NUMBER_OF_CELLS, checking_array)
pygame.quit()

our_first_map_file.close()
