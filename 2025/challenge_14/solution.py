import sys
import time
from pathlib import Path

if __name__ == "__main__":
    # Remonte de 2 niveaux pour atteindre la racine
    root_dir = Path(__file__).parent.parent.parent
    sys.path.insert(0, str(root_dir))

from challenge import Challenge


class Solution(Challenge):
    def __init__(self):
        super().__init__()
        self.challenge_dir = Path(__file__).parent
        self.input = []

    def resolve(self, standalone: bool = False) -> int:
        start_time = time.time()

        # Recovering each lines of the input as lists
        with open(self.challenge_dir / "input.txt") as file:
            self.input = [list(line.strip()) for line in file]

        # We register the index of the start
        start = self.found_start()

        # We rewrite the input in order to change each char in a array of [char, value] where the value is the number of timelines this char creates
        self.rewrite_input()

        # We compute how many timelines are created
        self.output = self.iteration_recursive(start, 0)
        self.output += 1

        end_time = time.time()
        self.time_elapsed = end_time - start_time

        if standalone:
            print(f"Finished in {end_time - start_time:.4f}s")
            print(f"output : {self.output}")

        return self.output

    def iteration_recursive(self, x, y):
        while True:
            if y == len(self.input):  # Reach the end of the map
                return 0
            elif (
                self.input[y][x][1] != -1
            ):  # If the value is not -1, that means that we already visited tis case and we know how much timelines it creats
                return self.input[y][x][1] + 1
            elif (
                self.input[y][x][0] == "^"
            ):  # That means that the next case just bellow is a spliter
                result = 1

                result += self.iteration_recursive(x + 1, y)
                result += self.iteration_recursive(x - 1, y)

                self.input[y][x][1] += result

                return result
            else:  # Nothing to do, we just continue to bring down
                y += 1

    def rewrite_input(self):
        # The goal of this function is to write inside each case, the number of timline they can create
        # So each char will we the key and their number ascociated the number of timelines they create

        liste = []
        for line in self.input:
            chars = []
            for char in line:
                chars.append([char, -1])
            liste.append(chars.copy())

        self.input = liste

    # Function that recover the char 'S' in the first line of the input
    def found_start(self):
        for char in range(0, len(self.input[0])):
            if self.input[0][char][0] == "S":
                return char


if __name__ == "__main__":
    solution = Solution()
    solution.resolve(True)
