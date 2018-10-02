#!/usr/bin/env python

import argparse
from copy import deepcopy
from time import sleep
from os import system, name


class Conway:

    def main(self):

        parser = argparse.ArgumentParser()
        parser.add_argument('iterations', type=int, help='Number of iterations')
        parser.add_argument('filename', help='Input file containing starting state, lines of \'0\'s and  \'1\'s')

        args = parser.parse_args()

        conway_grid = []

        for line in open(args.filename, 'r'):
            conway_grid.append(list(line.strip()))

        for x in range(args.iterations):
            self.clear_screen()
            self.draw_grid(conway_grid)
            sleep(1)
            conway_grid = self.iterate_grid(conway_grid)

        # Draw final state
        self.draw_grid(conway_grid)

    @staticmethod
    def draw_grid(conway_grid):
        for line in conway_grid:
            print(line)

    @staticmethod
    def iterate_grid(g):

        new_grid = deepcopy(g)

        x_len = len(g[0])
        y_len = len(g)

        for y, line in enumerate(g):
            for x in range(len(line)):

                alive = int(g[(x - 1) % x_len][(y - 1) % y_len]) + \
                        int(g[(x - 1) % x_len][y]) + \
                        int(g[(x - 1) % x_len][(y + 1) % y_len]) + \
                        int(g[x][(y - 1) % y_len]) + \
                        int(g[x][(y + 1) % y_len]) + \
                        int(g[(x + 1) % x_len][(y - 1) % y_len]) + \
                        int(g[(x + 1) % x_len][y]) + \
                        int(g[(x + 1) % x_len][(y + 1) % y_len])

                if g[x][y] is '1':
                    if alive > 3 or alive < 2:
                        new_grid[x][y] = '0'
                else:
                    if alive is 3:
                        new_grid[x][y] = '1'

        return new_grid

    @staticmethod
    def clear_screen():
        if name is 'nt':
            system('cls')
        else:
            system('clear')


if __name__ == "__main__":
    con = Conway()
    con.main()
