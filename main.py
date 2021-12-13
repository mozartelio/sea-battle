import json
import time

from backtracking import *
from dfs import *
from forward_checking import *
from gui import *
from statistics import *

our_first_map_file = open('maps.json', )
all_maps_data = json.load(our_first_map_file)
all_maps_data_copy = all_maps_data.copy()

# 16 was here 19
MAP_NUMBER = str(16)

NUMBER_OF_CELLS = all_maps_data[MAP_NUMBER]["NUMBER_OF_CELLS"]
ships = all_maps_data[MAP_NUMBER]["ships"]



class Game_state(Enum):
    PLAYING = 0
    GAME_CLOSED = 1
    SOLVED = 2
    FAILED = 3



checking_array = [[False for x in range(NUMBER_OF_CELLS)] for y in range(NUMBER_OF_CELLS)]
for a in range(0, NUMBER_OF_CELLS):
    for b in range(0, NUMBER_OF_CELLS):
        if all_maps_data[MAP_NUMBER]["map"][a][b] != "0":
            checking_array[a][b] = True


# print(checking_array)

gui=Gui(NUMBER_OF_CELLS,all_maps_data[MAP_NUMBER]["map"])

dfs_store=Dfs(NUMBER_OF_CELLS, checking_array, gui)

forward_checking_mrv= ForwardChecking(NUMBER_OF_CELLS, all_maps_data[MAP_NUMBER], gui, MRV=True)
forward_checking_lcv= ForwardChecking(NUMBER_OF_CELLS, all_maps_data[MAP_NUMBER], gui, LCV=True)

backtracking_mrv= Backtracking(NUMBER_OF_CELLS, all_maps_data[MAP_NUMBER], gui, MRV=True)
backtracking_lcv= Backtracking(NUMBER_OF_CELLS, all_maps_data[MAP_NUMBER], gui, LCV=True)

def print_stats_console(name_of_alg, time, memory_complexity, iterations):
    print("Time difference (s): " + str(time))
    print('Memory complexity ' + name_of_alg + ' (bytes): ' + str(memory_complexity))
    print('Iterations ' + name_of_alg + ' : ' + str(iterations))


def refresh_reset():
    dfs_store.reset()
    forward_checking_lcv.reset()
    forward_checking_mrv.reset()
    backtracking_mrv.reset()
    backtracking_lcv.reset()
    drawer()

def dfs():
    refresh_reset()
    name_of_alg = "DFS"
    time_before=time.time()
    print("DFS")
    dfs_store.preset()
    dfs_store.dfs()
    time_after=time.time()
    memory_complexity=sys.getsizeof(dfs_store)+dfs_store.size

    print_stats_console ( name_of_alg,(time_after - time_before),memory_complexity,dfs_store.iterations )
    stats = Statistics(gui.screen)
    stats.print_stats(time_after - time_before,memory_complexity,dfs_store.iterations,name_of_alg)



def lcv_backtracking():
    refresh_reset()
    print("backtracking + LCV")

    name_of_alg = "backtracking + LCV"
    time_before = time.time()
    backtracking_lcv.convert_to_binary_map()
    backtracking_lcv.backtrack()
    time_after = time.time()
    memory_complexity=sys.getsizeof(backtracking_lcv)+backtracking_lcv.size

    print_stats_console(name_of_alg,(time_after - time_before),memory_complexity,backtracking_lcv.iterations )

    stats = Statistics(gui.screen)
    stats.print_stats(time_after - time_before, memory_complexity, backtracking_lcv.iterations, name_of_alg)


def mrv_backtracking():
    refresh_reset()
    print("backtracking + MRV")
    name_of_alg = "backtracking + MRV"
    time_before = time.time()
    backtracking_mrv.convert_to_binary_map()
    backtracking_mrv.backtrack()
    time_after = time.time()
    memory_complexity=sys.getsizeof(backtracking_mrv)+backtracking_mrv.size

    print_stats_console(name_of_alg,(time_after - time_before),memory_complexity,backtracking_mrv.iterations )

    stats = Statistics(gui.screen)
    stats.print_stats(time_after - time_before,memory_complexity , backtracking_mrv.iterations, name_of_alg)


def mrv_forward_checking():
    refresh_reset()
    print("forward_checking + MRV")
    name_of_alg = "forward_checking + MRV"
    time_before = time.time()
    forward_checking_mrv.convert_to_binary_map()
    forward_checking_mrv.backtrack()
    time_after = time.time()
    memory_complexity= sys.getsizeof(forward_checking_mrv)+forward_checking_mrv.size

    print_stats_console(name_of_alg, (time_after - time_before), memory_complexity, forward_checking_mrv.iterations)

    stats = Statistics(gui.screen)
    stats.print_stats(time_after - time_before, memory_complexity, forward_checking_mrv.iterations, name_of_alg)


def lcv_forward_checking():
    refresh_reset()

    print("forward_checking + LCV")
    name_of_alg = "forward_checking + LCV"
    time_before = time.time()
    forward_checking_lcv.convert_to_binary_map()
    forward_checking_lcv.backtrack()
    time_after = time.time()
    memory_complexity= sys.getsizeof(forward_checking_lcv)+forward_checking_lcv.size

    print_stats_console(name_of_alg, (time_after - time_before), memory_complexity, forward_checking_lcv.iterations)

    stats = Statistics(gui.screen)
    stats.print_stats(time_after - time_before,memory_complexity , forward_checking_lcv.iterations, name_of_alg)

buttonDFS = Button(gui.screen, gui.BLOCK_SIZE, 120, 45, 'DFS', dfs)
buttonMRV_backtracking = Button(gui.screen, gui.BLOCK_SIZE, 120, 45, 'backtracking + MRV', mrv_backtracking)
buttonLCV_backtracking = Button(gui.screen, gui.BLOCK_SIZE, 120, 45, 'backtracking + LCV', lcv_backtracking)
buttonMRV_forward_checking = Button(gui.screen, gui.BLOCK_SIZE, 120, 45, 'forward checking + MRV', mrv_forward_checking)
buttonLCV_forward_checking = Button(gui.screen, gui.BLOCK_SIZE, 120, 45, 'forward checking LCV', lcv_forward_checking)


def drawer():
    gui.screen.fill(gui.WHITE)
    gui.flotila_plavidel(gui.screen, gui.img_horizontal_left_edge, gui.img_horizontal_right_edge,ships)
    gui.draw_grid()
    gui.draw_ships()
    pygame.display.update()



def main():
    game_state = Game_state.PLAYING

    gui.screen.fill(gui.WHITE)
    gui.flotila_plavidel(gui.screen, gui.img_horizontal_left_edge, gui.img_horizontal_right_edge, ships)
    gui.draw_grid()

    buttonDFS.draw(800, 20)
    buttonMRV_forward_checking.draw(800, 80)
    buttonLCV_forward_checking.draw(800, 140)
    buttonMRV_backtracking.draw(800, 200)
    buttonLCV_backtracking.draw(800, 260)
    gui.draw_ships()
    pygame.display.update()



    while game_state == Game_state.PLAYING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = Game_state.GAME_CLOSED
            #
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttonDFS.draw(800, 20)
                buttonMRV_forward_checking.draw(800, 80)
                buttonLCV_forward_checking.draw(800, 140)
                buttonMRV_backtracking.draw(800, 200)
                buttonLCV_backtracking.draw(800, 260)
            if event.type == pygame.MOUSEMOTION:
                buttonDFS.draw(800, 20)
                buttonMRV_forward_checking.draw(800, 80)
                buttonLCV_forward_checking.draw(800, 140)
                buttonMRV_backtracking.draw(800, 200)
                buttonLCV_backtracking.draw(800, 260)
            pygame.display.update()


main()
pygame.quit()

our_first_map_file.close()
