import random


class State:
    @staticmethod
    def __initial_state(filename):
        if filename is not None:
            return State.__read_from_file(filename)

        return State.__gen_random()

    @staticmethod
    def __read_from_file(filename):
        matrix = []
        n = 0

        with open(filename, 'r') as file:
            for line in file:
                n += 1
                m = len(line.rstrip('\n'))

                for i in line.rstrip('\n'):
                    matrix.append(int(i))

        return n, m, matrix

    @staticmethod
    def __gen_random():
        n, m = random.randint(2, 10), random.randint(2, 10)
        matrix = [random.randint(0, 1) for _ in range(0, n * m)]

        return n, m, matrix

    def __init__(self, filename):
        self.n, self.m, self.matrix = self.__initial_state(filename)

    def tick(self):
        next_state = self.matrix.copy()

        for i in range(self.n):
            for j in range(self.m):
                nb = self.__check_neighbours(i, j)
                index = self.__get_index(i, j)

                if self.matrix[index] == 0 and nb == 3:
                    next_state[index] = 1
                elif self.matrix[index] == 1 and (nb < 2 or nb > 3):
                    next_state[index] = 0

        self.matrix = next_state

    def get_cell(self, i, j):
        return self.matrix[self.__get_index(i, j)]

    def get_size(self):
        return self.n, self.m

    def __get_index(self, i, j):
        return i * self.m + j

    def __check_neighbours(self, i, j):
        count = 0

        for row in range(i - 1, i + 2):
            for col in range(j - 1, j + 2):
                if row == i and col == j:
                    continue

                if row < 0:
                    row = self.n - 1
                elif row > self.n - 1:
                    row = 0

                if col < 0:
                    col = self.m - 1
                elif col > self.m - 1:
                    col = 0

                count += self.matrix[self.__get_index(row, col)]

        return count
