from pympler import asizeof
from gui import *


class Orientation(Enum):
    HORIZONTAL =0
    VERTICAL = 1


class Backtracking:
    def __init__(self, number_of_cells, all_map_data, gui, MRV=None, LCV=None):
        if LCV and MRV:
            sys.stderr.write("OOOps, problems Backtracking __init__() lcv=mrv=True...\n")
            return
        self.empty_mark = 0
        self.ship_mark = 1

        self.all_map_data = all_map_data
        self.mrv = MRV
        self.lcv = LCV
        self.NUMBER_OF_CELLS = number_of_cells
        self.two_dimensional_answer_field = all_map_data["map"]
        self.converted_two_dimensional_answer_field = []
        self.GAME_SOLVED = False
        self.iterations = 0
        self.generated_array = [[self.empty_mark for x in range(self.NUMBER_OF_CELLS)] for y in
                                range(self.NUMBER_OF_CELLS)]

        self.gui = gui
        self.vertical_ship_total = gui.vertical_ship_counter
        self.horizontal_ship_total = gui.horizontal_ship_counter
        self.vertical_ship_counter = [0] * self.NUMBER_OF_CELLS
        self.horizontal_ship_counter = [0] * self.NUMBER_OF_CELLS

        self.ships_to_place = sorted(all_map_data["ships"]) if self.lcv else (
            sorted(all_map_data["ships"], reverse=True) if self.mrv else None)

        self.ship_start_row_posit = []
        self.ship_start_col_posit = []
        self.ship_start_pos_orien = []

    def reset(self):
        self.GAME_SOLVED = False
        self.iterations = 0
        # at the same time cleans counters and a generated array
        for i in range(0, len(self.generated_array)):
            self.vertical_ship_counter[i] = 0
            self.horizontal_ship_counter[i] = 0
            for column in range(0, len(self.generated_array)):
                self.generated_array[i][column] = self.empty_mark
        self.ships_to_place = sorted(self.all_map_data["ships"]) if self.lcv else (
            sorted(self.all_map_data["ships"], reverse=True) if self.mrv else None)
        self.ship_start_row_posit = []
        self.ship_start_col_posit = []
        self.ship_start_pos_orien = []
        self.size=0


    def convert_to_binary_map(self):
        self.size = asizeof.asizeof(self.empty_mark) + asizeof.asizeof(self.ship_mark) + asizeof.asizeof(
            self.all_map_data) + \
                    +asizeof.asizeof(self.mrv) + asizeof.asizeof(self.lcv) + asizeof.asizeof(
            self.NUMBER_OF_CELLS) + asizeof.asizeof(self.two_dimensional_answer_field) + \
                    +asizeof.asizeof(self.converted_two_dimensional_answer_field) + asizeof.asizeof(
            self.GAME_SOLVED) + asizeof.asizeof(self.iterations) + \
                    +asizeof.asizeof(self.generated_array) + asizeof.asizeof(
            self.vertical_ship_total) + asizeof.asizeof(self.horizontal_ship_total) + \
                    +asizeof.asizeof(self.vertical_ship_counter) + asizeof.asizeof(
            self.horizontal_ship_counter) + asizeof.asizeof(self.ships_to_place) + \
                    +asizeof.asizeof(self.ship_start_row_posit) + asizeof.asizeof(
            self.ship_start_col_posit) + asizeof.asizeof(self.ship_start_pos_orien)

        field = [[0 for xa in range(len(self.two_dimensional_answer_field))] for ya in
                 range(len(self.two_dimensional_answer_field))]

        for row in range(0, len(self.two_dimensional_answer_field)):
            for column in range(0, len(self.two_dimensional_answer_field)):
                if self.two_dimensional_answer_field[row][column] == "0":
                    field[row][column] = 0
                    print("0 ", end="")
                elif 1 <= int(self.two_dimensional_answer_field[row][column]) <= 6:
                    field[row][column] = 1
                    print("1 ", end="")
                else:
                    sys.stderr.write("OOOps, problems convert_to_binary_map()...")
            print()
        print("Map was converted successfully!")
        self.converted_two_dimensional_answer_field = field
        self.size += asizeof.asizeof(field)


    def array_comparator(self):
        if self.GAME_SOLVED:
            return True
        # define according to ships left to place list
        if len(self.ships_to_place) == 0:
            self.gui.draw_ships_algorithm(self.generated_array, dimension=2)
            for x in range(0, self.NUMBER_OF_CELLS):
                for y in range(0, self.NUMBER_OF_CELLS):
                    if self.generated_array[x][y] == 1:
                        print("O" + " ", end='')
                    else:
                        print("X" + " ", end='')
                print()

            if self.generated_array == self.converted_two_dimensional_answer_field:
                self.GAME_SOLVED = True
                print("GAME solved!!!")

        if self.generated_array == self.converted_two_dimensional_answer_field:
            self.GAME_SOLVED = True
            print("GAME SOLVED!!!")
            return True
        return False

    def backtrack(self):
        if self.array_comparator():
            return True
        self.iterations += 1
        print("Iterations: " + str(self.iterations))

        for i in range(0, len(self.ships_to_place)):
            size = self.ships_to_place[i]
            self.size += asizeof.asizeof(size)
            for z in Orientation:
                possib_positions = self.find_possib_positions(size, z)
                self.size += asizeof.asizeof(possib_positions)
                for j in range(0, len(possib_positions)):

                    row = possib_positions[j][0]
                    col = possib_positions[j][1]
                    placed = self.place_ship(row, col, size, z)
                    self.size += asizeof.asizeof(row)
                    self.size += asizeof.asizeof(col)
                    self.size += asizeof.asizeof(placed)

                    if placed:
                        self.update_row_col_counters(0, row, col, size, z)
                        self.ship_start_row_posit.append(row)
                        self.ship_start_col_posit.append(col)
                        self.ship_start_pos_orien.append(z)
                        self.ships_to_place.pop(i)
                        result = self.backtrack()
                        self.size += asizeof.asizeof(result)
                        if result:
                            return True
                        else:
                            self.ships_to_place.insert(i, size)
                            bad_ship_row = self.ship_start_row_posit.pop()
                            bad_ship_col = self.ship_start_col_posit.pop()
                            bad_ship_cord = self.ship_start_pos_orien.pop()

                            self.size += asizeof.asizeof(bad_ship_row)
                            self.size += asizeof.asizeof(bad_ship_col)
                            self.size += asizeof.asizeof(bad_ship_cord)

                            self.remove_ship(bad_ship_row, bad_ship_col, size, bad_ship_cord)
                            self.update_row_col_counters(1, bad_ship_row, bad_ship_col, size, bad_ship_cord)
        return False


    def remove_ship(self, row, col, size, orientation):
        # set cells with ship to empty
        if orientation == Orientation.HORIZONTAL:
            for j in range(col, col + size):
                self.generated_array[row][j] = self.empty_mark
        else:
            for i in range(row, row + size):
                self.generated_array[i][col] = self.empty_mark


    def update_row_col_counters(self, add_or_remove, row, col, size, orientation):
        # 0 = add, else = remove
        if orientation == Orientation.HORIZONTAL:
            for i in range(col, col + size):
                if add_or_remove == 0:
                    self.horizontal_ship_counter[i] += 1
                else:
                    self.horizontal_ship_counter[i] -= 1
            if add_or_remove == 0:
                self.vertical_ship_counter[row] += size
            else:
                self.vertical_ship_counter[row] -= size

        elif orientation == Orientation.VERTICAL:
            for i in range(row, row + size):
                if add_or_remove == 0:
                    self.vertical_ship_counter[i] += 1
                else:
                    self.vertical_ship_counter[i] -= 1
            if add_or_remove == 0:
                self.horizontal_ship_counter[col] += size
            else:
                self.horizontal_ship_counter[col] -= size
        else:
            sys.stderr.write("OOOps, problems update_row_col_counters()...")


    def place_ship(self, row, col, size, orientation):
        # check that placement is within bounds of grid
        # and that ship won't overlap existing nodes
        try:
            if orientation == Orientation.HORIZONTAL:

                for j in range(col, col + size):
                    if self.generated_array[row][j] != self.empty_mark:
                        return False
                for j in range(col, col + size):
                    self.generated_array[row][j] = self.ship_mark

            elif orientation == Orientation.VERTICAL:
                for i in range(row, row + size):
                    if self.generated_array[i][col] != self.empty_mark:
                        return False
                for i in range(row, row + size):
                    self.generated_array[i][col] = self.ship_mark
            else:
                sys.stderr.write("OOOps, problems place_ship()...")
        except IndexError:
            return False
        return True

    def get_cell_value(self, row, col):
        # check if ship_mark is empty or not
        # avoid "out of bounds" error
        if row < 0 or col < 0:
            return self.empty_mark
        try:
            value = self.generated_array[row][col]
        except IndexError:
            value = self.empty_mark
        return value

    def adjacent_ships(self, row, col, size, orientation):
        # returns True if there are adjacent ships,
        # false otherwise
        if orientation == Orientation.HORIZONTAL:
            if self.get_cell_value(row, col + size) != self.empty_mark:
                return True
            if self.get_cell_value(row, col - 1) != self.empty_mark:
                return True
            for j in range(-1, size + 1):
                if self.get_cell_value(row + 1, col + j) != self.empty_mark:
                    return True
                if self.get_cell_value(row - 1, col + j) != self.empty_mark:
                    return True
        elif orientation == Orientation.VERTICAL:
            if self.get_cell_value(row + size, col) != self.empty_mark:
                return True
            if self.get_cell_value(row - 1, col) != self.empty_mark:
                return True
            for i in range(-1, size + 1):
                if self.get_cell_value(row + i, col + 1) != self.empty_mark:
                    return True
                if self.get_cell_value(row + i, col - 1) != self.empty_mark:
                    return True
        else:
            sys.stderr.write("OOOps, problems adjacent_ships()...")
        return False

    def find_possib_positions(self, size, orientation):
        possible_movements = []
        for row in range(0, self.NUMBER_OF_CELLS):
            for col in range(0, self.NUMBER_OF_CELLS):
                possible_movements.append([row, col])
        return possible_movements



