# from main import *
from statistics import *
import numpy as np
import time

class DFS:
    def __init__(self, number_of_cells, two_dimensional_answer_field,gui):
        self.gui = gui
        self.NUMBER_OF_CELLS = number_of_cells
        self.one_dimensional_answer_field = np.array(two_dimensional_answer_field).flatten()
        self.GAME_SOLVED = False
        self.values = [True, False]
        self.iterations = 0
        self.dfs_array = []

    def array_comparator(self, array_to_compare):
        if len(array_to_compare) == len(self.one_dimensional_answer_field):
            # time.sleep(0.5)
            self.gui.draw_ships_algorithm(array_to_compare)

            test = np.array(array_to_compare)
            comparison = test == self.one_dimensional_answer_field
            equal_arrays = comparison.all()
            if equal_arrays:
                self.GAME_SOLVED = True
                print("GAME SOLVED!!!")
                return True
        return False

    def dfs(self):
        if len(self.dfs_array) < (self.NUMBER_OF_CELLS * self.NUMBER_OF_CELLS):
            if self.GAME_SOLVED:
                return

            for i in self.values:
                self.dfs_array.append(i)
                self.iterations += 1
                print("Iterations: " + str(self.iterations))
                #print(array)
                # for xqr in range(0, len(self.dfs_array) - 1):
                #     if self.dfs_array[xqr]:
                #         print("1" + " ", end='')
                #         #print(str(dfska_field[xq][yq]) + " ", end='')
                #     else:
                #         print("0" + " ", end='')
                # for df in range(0, self.NUMBER_OF_CELLS * self.NUMBER_OF_CELLS - (len(self.dfs_array) - 1)):
                #     print("  ", end='')
                # print('\n')
                # print(len(array))
                if self.array_comparator(self.dfs_array):
                    return
                self.dfs()
                self.dfs_array.pop(len(self.dfs_array) - 1)
