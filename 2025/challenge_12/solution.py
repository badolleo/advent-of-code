import sys
import time
from pathlib import Path

import numpy as np

if __name__ == "__main__":
    # Remonte de 2 niveaux pour atteindre la racine
    root_dir = Path(__file__).parent.parent.parent
    sys.path.insert(0, str(root_dir))

from challenge import Challenge


class Solution(Challenge):
    def __init__(self) -> None:
        super().__init__()
        self.challenge_dir = Path(__file__).parent

    # This function will add space at the end of each line in order to unify their size
    def unify_rows(self, input):
        max_size = len(input[0])

        for line in input:
            if len(line) > max_size:
                max_size = len(line)

        for i in range(len(input)):
            input[i] = input[i] + " " * (max_size - len(input[i]))

    def resolve(self, standalone=False):
        start_time = time.time()
        input = []

        # Recover all our inputs data from the file "input.txt"
        with open(self.challenge_dir / "input.txt", "r") as file:
            for line in file:
                input.append(line.removesuffix("\n"))

        # We unify end of lines cause its not like we want
        self.unify_rows(input)

        """ Example data :
        [
            [123 328  51 64 ],
            [ 45 64  387 23 ],
            [  6 98  215 314],
            [*   +   *   +  ]
        ]
        """

        numbers = []
        operation = ""

        # First, we will parse each column, from the last to the first one like in the web example
        for column in range(len(input[0]) - 1, -1, -1):
            column_value = ""  # The string value of the int in the actual column
            is_number = False  # Boolean to know if there is a number in the column or just spaces

            # Then we parse all rown to recover the integer in the column
            for row in range(0, len(input)):
                # We first check if we have an operation in the position we are looking
                if "+" in input[row][column]:
                    operation = "+"
                    break
                elif "*" in input[row][column]:
                    operation = "*"
                    break
                elif input[row][column] != " " and input[row][column] != "\n":
                    is_number = True
                    column_value += str(input[row][column])

            # We keep all numbers that are in the same equation
            if is_number:
                numbers.append(int(column_value))

            # If we have an operation sigle, it means that we have to make it and reset viriables
            if operation != "":
                if operation == "+":
                    self.output += np.sum(numbers)
                elif operation == "*":
                    self.output += int(np.prod(numbers))
                numbers = []
                operation = ""

        end_time = time.time()
        self.time_elapsed = end_time - start_time

        if standalone:
            print(f"Finished in {end_time - start_time:.4f}s")
            print(f"output : {self.output}")

        return self.output


if __name__ == "__main__":
    challenge = Solution()
    challenge.resolve(True)
