import time
import argparse
import os

from state import State


def render(state):
    n, m = state.get_size()
    os.system('clear')

    for i in range(n):
        print(' '.join([str(state.get_cell(i, j)) for j in range(m)]))


def parse_filename():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', dest="filename", type=argparse.FileType('r'), help='file name')
    args = parser.parse_args()

    if args.filename is None:
        return None

    return args.filename.name


def main():
    filename = parse_filename()
    state = State(filename)

    while True:
        render(state)
        state.tick()
        time.sleep(1)


main()
