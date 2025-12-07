import time
from pathlib import Path

import numpy as np

from challenge import Challenge


class Solution(Challenge):
    def __init__(self) -> None:
        super().__init__()
        self.challenge_dir = Path(__file__).parent

    def resolve(self, standalone=False):
        start_time = time.time()
        input = []
        index = 0

        # Recover all our inputs data from the file "input.txt"
        with open(self.challenge_dir / "input.txt", "r") as file:
            for line in file:
                input.append(
                    []
                )  # input is a list where each element represent a row of the input.
                line = line.strip().split(" ")

                for char in line:
                    if char != "":
                        input[index].append(char)

                index += 1

        # First, we need to recover number column by column
        for column in range(0, len(input[0])):
            numbers = []  # Numbers in the column
            operation = input[-1][column]  # The operation to perform on the numbers

            # We parse all rows to recover the numbers in the column except that last one because it's the operation
            for row in range(0, len(input) - 1):
                numbers.append(int(input[row][column]))

            if operation == "*":
                self.output += int(np.prod(numbers))
            elif operation == "+":
                self.output += np.sum(numbers)

        end_time = time.time()
        self.time_elapsed += end_time - start_time

        if standalone:
            print(f"Finished in {end_time - start_time:.4f}s")
            print(f"output : {self.output}")

        return self.output


if __name__ == "__main__":
    challenge = Solution()
    challenge.resolve(True)
