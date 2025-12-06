import time

import numpy as np


class Challenge:
    def __init__(self) -> None:
        self.output = 0
        self.time_elapsed = 0

    def resolve(self, standalone=False):
        start_time = time.time()
        input = []
        index = 0

        with open("input.txt", "r") as file:
            for line in file:
                input.append([])
                line = line.strip().split(" ")

                for char in line:
                    if char != "":
                        input[index].append(char)

                index += 1

        for column in range(0, len(input[0])):
            numbers = []
            operation = input[-1][column]

            for row in range(0, len(input) - 1):
                numbers.append(int(input[row][column]))

            if operation == "*":
                self.output += np.prod(numbers)
            elif operation == "+":
                self.output += np.sum(numbers)

        end_time = time.time()
        self.time_elapsed += end_time - start_time

        if standalone:
            print(f"Finished in {end_time - start_time:.4f}s")
            print(f"output : {self.output}")

        return self.output


if __name__ == "__main__":
    challenge = Challenge()
    challenge.resolve(True)
