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

    def resolve(self, standalone: bool = False) -> int:
        start_time = time.time()
        input = []

        # Recovering each lines of the input as lists
        with open(self.challenge_dir / "input.txt") as file:
            input: list = [list(line.strip()) for line in file]

        start_position = input[0].index("S")  # Recovering the starting position
        input[1][start_position] = "|"

        # We parse each lines in order to bring down each "|"
        for index in range(1, len(input)):
            for char_index in range(len(input[index])):
                if input[index][char_index] == "^":  # If we got a ^
                    if input[index - 1][char_index] == "|":  # Then we split
                        self.output += 1
                        if char_index - 1 > 0 and input[index][char_index - 1] != "^":
                            input[index][char_index - 1] = "|"
                        if (
                            char_index + 1 < len(input[index])
                            and input[index][char_index + 1] != "^"
                        ):
                            input[index][char_index + 1] = "|"
                elif input[index - 1][char_index] == "|":
                    input[index][char_index] = "|"

        end_time = time.time()
        self.time_elapsed = end_time - start_time

        if standalone:
            print(f"Finished in {end_time - start_time:.4f}s")
            print(f"output : {self.output}")

        return self.output


if __name__ == "__main__":
    solution = Solution()
    solution.resolve(True)
