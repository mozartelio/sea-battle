import sys
from enum import Enum
import pygame

class Map_cell_state(Enum):
    EMPTY_STATE = 0
    LONELY_SHIP_STATE = 1
    MIDDLE_SHIP_SECTION = 2
    HORIZONTAL_LEFT_EDGE = 3
    HORIZONTAL_RIGHT_EDGE = 4
    VERTICAL_TOP_EDGE = 5
    VERTICAL_BOTTOM_EDGE = 6

class Gui:
    def __init__(self, number_of_cells, two_dimensional_full_answer_field):
        self.NUMBER_OF_CELLS=number_of_cells
        self.all_maps_data=two_dimensional_full_answer_field
        self.BLOCK_SIZE = 20
        self.LEFT_INDENT = 100
        self.UPPER_INDENT = 10
        self.size = (self.LEFT_INDENT + 43 * self.BLOCK_SIZE, self.UPPER_INDENT + 15 * self.BLOCK_SIZE)
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Lode")
        self.font_size = int(self.BLOCK_SIZE / 1.5)
        self.font_x = pygame.font.SysFont('arial', self.font_size)

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)



        self.img_vertical_top_edge = pygame.transform.scale(pygame.image.load('assets/VERTICAL_TOP_EDGE.png'), (16, 16))
        self.img_vertical_bottom_edge = pygame.transform.scale(pygame.image.load('assets/VERTICAL_BOTTOM_EDGE.png'), (16, 16))

        self.img_horizontal_left_edge = pygame.transform.scale(pygame.image.load('assets/HORIZONTAL_LEFT_EDGE.png'), (16, 16))
        self.img_horizontal_right_edge = pygame.transform.scale(pygame.image.load('assets/HORIZONTAL_RIGHT_EDGE.png'), (16, 16))

        self.vertical_ship_counter = [0] * self.NUMBER_OF_CELLS
        self.horizontal_ship_counter = [0] * self.NUMBER_OF_CELLS


    def flotila_plavidel(self, screen, img_horizontal_left_edge, img_horizontal_right_edge):
        font = pygame.font.SysFont('arial', self.font_size)
        text = font.render('Flotila plavidel:', True, self.BLACK)
        textRect = text.get_rect()
        textRect.center = (7 * self.LEFT_INDENT, self.UPPER_INDENT)
        screen.blit(text, textRect)
        for i in range(1, self.NUMBER_OF_CELLS):
            if i < 7:
                screen.blit(img_horizontal_left_edge, (6.65 * self.LEFT_INDENT, self.UPPER_INDENT + i * self.BLOCK_SIZE - 5))
                if i < 4:
                    pygame.draw.rect(screen, self.BLACK,
                                     (int(6.75 * self.LEFT_INDENT + 9), int(self.UPPER_INDENT + i * self.BLOCK_SIZE - 4), 15, 15))
                    if i < 2:
                        pygame.draw.rect(screen, self.BLACK,
                                         (int(6.75 * self.LEFT_INDENT + 27), int(self.UPPER_INDENT + i * self.BLOCK_SIZE - 4), 15, 15))
                        screen.blit(img_horizontal_right_edge, (6.65 * self.LEFT_INDENT + 54, self.UPPER_INDENT + i * self.BLOCK_SIZE - 5))
                    if i > 1:
                        screen.blit(img_horizontal_right_edge,
                                    (6.65 * self.LEFT_INDENT + 36.5, self.UPPER_INDENT + i * self.BLOCK_SIZE - 5))
                if i > 3 and i < 7:
                    screen.blit(img_horizontal_right_edge, (6.65 * self.LEFT_INDENT + 18.5, self.UPPER_INDENT + i * self.BLOCK_SIZE - 5))
            if i > 5:
                pygame.draw.circle(screen, self.BLACK, (6.75 * self.LEFT_INDENT, self.UPPER_INDENT + (i + 1) * self.BLOCK_SIZE + 2), 8)


    def fill_vertical_or_horizontal_ship_counter(self, vertical):
        for row in range(0, self.NUMBER_OF_CELLS):
            for column in range(0, self.NUMBER_OF_CELLS):
                match int(self.all_maps_data[row if vertical else column][column if vertical else row]):
                    case Map_cell_state.LONELY_SHIP_STATE.value | Map_cell_state.MIDDLE_SHIP_SECTION.value | \
                         Map_cell_state.HORIZONTAL_LEFT_EDGE.value | Map_cell_state.HORIZONTAL_RIGHT_EDGE.value | \
                         Map_cell_state.VERTICAL_TOP_EDGE.value | Map_cell_state.VERTICAL_BOTTOM_EDGE.value:
                        if vertical:
                            self.vertical_ship_counter[row] += 1
                        else:
                            self.horizontal_ship_counter[row] += 1

                    case Map_cell_state.EMPTY_STATE.value:
                        pass

                    case _:
                        sys.stderr.write('Problem in fill_vertical_or_horizontal_ship_counter(), ' +
                                         'not declared new cell state with number:' +
                                         str(self.all_maps_data[column][row]) + '\n')


    def draw_ships(self):
        x_block_center = self.LEFT_INDENT + self.BLOCK_SIZE / 2
        y_block_center = self.UPPER_INDENT + self.BLOCK_SIZE / 2
        circle_radius = 8

        img_vertical_top_edge = pygame.transform.scale(pygame.image.load('assets/VERTICAL_TOP_EDGE.png'), (16, 16))
        img_vertical_bottom_edge = pygame.transform.scale(pygame.image.load('assets/VERTICAL_BOTTOM_EDGE.png'), (16, 16))

        img_horizontal_left_edge = pygame.transform.scale(pygame.image.load('assets/HORIZONTAL_LEFT_EDGE.png'), (16, 16))
        img_horizontal_right_edge = pygame.transform.scale(pygame.image.load('assets/HORIZONTAL_RIGHT_EDGE.png'), (16, 16))

        for x in range(0, self.NUMBER_OF_CELLS):
            for y in range(0, self.NUMBER_OF_CELLS):

                match int(self.all_maps_data[y][x]):
                    case Map_cell_state.LONELY_SHIP_STATE.value:
                        pygame.draw.circle(self.screen, self.BLACK, (x_block_center, y_block_center), circle_radius)
                    case Map_cell_state.MIDDLE_SHIP_SECTION.value:
                        pygame.draw.rect(self.screen, self.BLACK, (int(x_block_center - 7), int(y_block_center - 7), 15, 15))
                    case Map_cell_state.VERTICAL_TOP_EDGE.value:
                        self.screen.blit(img_vertical_top_edge, (x_block_center - circle_radius, y_block_center - circle_radius))
                    case Map_cell_state.VERTICAL_BOTTOM_EDGE.value:
                        self.screen.blit(img_vertical_bottom_edge,
                                    (x_block_center - circle_radius, y_block_center - circle_radius))
                    case Map_cell_state.HORIZONTAL_LEFT_EDGE.value:
                        self.screen.blit(img_horizontal_left_edge,
                                    (x_block_center - circle_radius, y_block_center - circle_radius))
                    case Map_cell_state.HORIZONTAL_RIGHT_EDGE.value:
                        self.screen.blit(img_horizontal_right_edge,
                                    (x_block_center - circle_radius, y_block_center - circle_radius))
                    case Map_cell_state.EMPTY_STATE.value:
                        pass
                    case _:
                        sys.stderr.write('Problem in draw_ships(), ' +
                                         'not declared new cell state with number:' +
                                         str(self.all_maps_data[y][x]) + '\n')
                y_block_center = y_block_center + self.BLOCK_SIZE
                print("x_block_center CHECKER: " + str(x_block_center))
                print("y_block_center CHECKER: " + str(y_block_center))
            y_block_center = self.UPPER_INDENT + self.BLOCK_SIZE / 2
            x_block_center = x_block_center + self.BLOCK_SIZE

        pygame.display.update()


    def draw_ships_algorithm(self,array_to_compare):


        row_block_center = self.UPPER_INDENT + self.BLOCK_SIZE / 2
        # column_block_center = self.UPPER_INDENT + self.BLOCK_SIZE / 2
        column_block_center = self.UPPER_INDENT + self.BLOCK_SIZE*20

        circle_radius = 8

        print("row_block_center: " + str(row_block_center))
        print("column_block_center: " + str(column_block_center))
        for x in range(0, self.NUMBER_OF_CELLS):
            for y in range(0, self.NUMBER_OF_CELLS):
                if array_to_compare[x*self.NUMBER_OF_CELLS+y]:
                    print("1" + " ", end='')
                    #print(str(dfska_field[xq][yq]) + " ", end='')
                else:
                    print("0" + " ", end='')
            print()

        # pygame.draw.circle(self.screen, self.BLACK, (column_block_center,row_block_center), circle_radius * 20)
        # pygame.display.update()
        for x in range(0, self.NUMBER_OF_CELLS):
            for y in range(0, self.NUMBER_OF_CELLS):
                if array_to_compare[x*self.NUMBER_OF_CELLS+y]:
                    # pygame.draw.circle(self.screen, self.BLACK, (row_block_center, column_block_center), circle_radius * 10)
                    pygame.display.update()
                    pygame.draw.circle(self.screen, self.BLACK, (column_block_center,row_block_center), circle_radius)
                else:
                    pygame.draw.circle(self.screen, self.WHITE, (column_block_center,row_block_center), circle_radius)
                column_block_center = column_block_center +self.BLOCK_SIZE

            column_block_center = self.UPPER_INDENT + self.BLOCK_SIZE*20
            row_block_center = row_block_center + self.BLOCK_SIZE
            print("row_block_center in cycle: " + str(row_block_center))
            print("column_block_center in cycle: " + str(column_block_center))
        # pygame.draw.circle(self.screen, self.BLACK, (row_block_center, column_block_center), circle_radius * 20)
        pygame.display.update()


    def draw_grid(self):
        for i in range(self.NUMBER_OF_CELLS + 1):
            # horizontal grid1
            pygame.draw.line(self.screen, self.BLACK, (self.LEFT_INDENT, self.UPPER_INDENT + i * self.BLOCK_SIZE),
                             (self.LEFT_INDENT + self.NUMBER_OF_CELLS * self.BLOCK_SIZE, self.UPPER_INDENT + i * self.BLOCK_SIZE), 1)

            # print(str(LEFT_INDENT) + ',' + str(UPPER_INDENT + i * BLOCK_SIZE) + ";", end='')
            # print(str(LEFT_INDENT + 10 * BLOCK_SIZE) + ',' + str(UPPER_INDENT + i * BLOCK_SIZE))
            # print('***')

            # vertical grid1
            pygame.draw.line(self.screen, self.BLACK, (self.LEFT_INDENT + i * self.BLOCK_SIZE, self.UPPER_INDENT),
                             (self.LEFT_INDENT + i * self.BLOCK_SIZE, self.UPPER_INDENT + self.NUMBER_OF_CELLS * self.BLOCK_SIZE), 1)
            # horizontal grid2
            pygame.draw.line(self.screen, self.BLACK, (self.LEFT_INDENT + 15 * self.BLOCK_SIZE, self.UPPER_INDENT +
                                             i * self.BLOCK_SIZE),
                             (self.LEFT_INDENT + 25 * self.BLOCK_SIZE, self.UPPER_INDENT + i * self.BLOCK_SIZE), 1)
            # vertical grid2
            pygame.draw.line(self.screen, self.BLACK, (self.LEFT_INDENT + (i + 15) * self.BLOCK_SIZE, self.UPPER_INDENT),
                             (self.LEFT_INDENT + (i + 15) * self.BLOCK_SIZE, self.UPPER_INDENT + self.NUMBER_OF_CELLS * self.BLOCK_SIZE), 1)

            if i < self.NUMBER_OF_CELLS:
                num_vertical = self.font_x.render(str(self.vertical_ship_counter[i]), True, self.BLACK)
                num_horizontal = self.font_x.render(str(self.horizontal_ship_counter[i]), True, self.BLACK)

                # TODO: width and height for both num_vertical and num_horizontal
                # width of rendered numbers
                num_width = num_vertical.get_width()
                # height of rendered numbers
                num_height = num_vertical.get_height()
                # letters_hor_width = letters_hor.get_width()

                # vertical num_vertical grid1
                self.screen.blit(num_vertical, (3.2 * self.LEFT_INDENT - (self.BLOCK_SIZE // 2 + num_width // 2),
                                           self.UPPER_INDENT + i * self.BLOCK_SIZE + (self.BLOCK_SIZE // 2 - num_height // 2)))
                # horizontal letters grid1
                self.screen.blit(num_horizontal, (
                    self.LEFT_INDENT + i * self.BLOCK_SIZE + (self.BLOCK_SIZE // 2 - num_width // 2), self.UPPER_INDENT + 10 * self.BLOCK_SIZE))
                # vertical num_vertical grid2
                self.screen.blit(num_vertical, (3.2 * self.LEFT_INDENT - (self.BLOCK_SIZE // 2 + num_width // 2) + 15 *
                                           self.BLOCK_SIZE, self.UPPER_INDENT + i * self.BLOCK_SIZE + (self.BLOCK_SIZE // 2 - num_height // 2)))
                # horizontal letters grid2
                self.screen.blit(num_horizontal, (
                    self.LEFT_INDENT + i * self.BLOCK_SIZE + (self.BLOCK_SIZE // 2 - num_width // 2) + 15 * self.BLOCK_SIZE,
                    self.UPPER_INDENT + 10 * self.BLOCK_SIZE))




class Button:
    def __init__(self,screen, block_size,  width, height, text, action):
        self.font_size =  int(block_size / 1.5)
        self.screen=screen
        self.width = width
        self.text = text
        self.height = height
        self.action = action

        self.inactive_color = (23, 204, 58)
        self.active_color = (13, 162, 58)
        self.BLACK = (0, 0, 0)

    def draw(self, x, y):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # if x < mouse[0] < x + self.width:
        #     if y < mouse[1] < y + self.height:
        if pygame.Rect(x, y, self.width, self.height).collidepoint((mouse[0], mouse[1])):
            pygame.draw.rect(self.screen, self.active_color, (x, y, self.width, self.height))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if self.action is not None:
                    self.action()
                    # TODO: ...
        else:
            pygame.draw.rect(self.screen, self.inactive_color, (x, y, self.width, self.height))

        font = pygame.font.SysFont('arial', self.font_size)
        text = font.render(self.text, True, self.BLACK)
        text_rectangle = text.get_rect()
        text_rectangle.center = (x + 48, y + 20)
        self.screen.blit(text, text_rectangle)
