import numpy as np
from pympler import asizeof

class Dfs:
    def __init__(self, number_of_cells, two_dimensional_answer_field,gui):
        self.gui = gui
        self.NUMBER_OF_CELLS = number_of_cells
        self.one_dimensional_answer_field = np.array(two_dimensional_answer_field).flatten()
        self.GAME_SOLVED = False
        self.values = [True, False]
        self.iterations = 0
        self.dfs_array = []
        self.size=0

    def preset(self):
        self.size = asizeof.asizeof(self.NUMBER_OF_CELLS) + asizeof.asizeof(self.one_dimensional_answer_field) + \
                    asizeof.asizeof(self.GAME_SOLVED) + asizeof.asizeof(self.values) + asizeof.asizeof(self.iterations)

    def reset(self):
        self.GAME_SOLVED = False
        self.iterations = 0
        self.dfs_array = []
        self.size=0


    def array_comparator(self, array_to_compare):
        if self.GAME_SOLVED:
            return True
        if len(array_to_compare) == len(self.one_dimensional_answer_field):
            for x in range(0, self.NUMBER_OF_CELLS):
                for y in range(0, self.NUMBER_OF_CELLS):
                    if array_to_compare[x * self.NUMBER_OF_CELLS + y]:
                        print("O ", end='')
                    else:
                        print("X " , end='')
                print()

            self.gui.draw_ships_algorithm(array_to_compare, dimension=1)
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
                self.size += asizeof.asizeof(i)
                self.iterations += 1
                print("Iterations: " + str(self.iterations))

                if self.array_comparator(self.dfs_array):
                    return
                self.dfs()
                self.dfs_array.pop(len(self.dfs_array) - 1)
