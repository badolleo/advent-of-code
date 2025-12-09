import math
import sys
import time
from pathlib import Path

import numpy as np
from scipy.spatial.distance import cdist

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
        with open(self.challenge_dir / "input_2.txt") as file:
            for line in file:
                self.input.append(line.strip())

        # We set up the minimum rectangle as the first one possible
        self.output = self.compute_area(self.input[0], self.input[1])

        # We parse each coordinates in order to compute the area of the rectangle
        for i in range(0, len(self.input)):
            for j in range(i + 1, len(self.input)):
                area = self.compute_area(self.input[i], self.input[j])

                if area > self.output:
                    self.output = area

        end_time = time.time()
        self.time_elapsed = end_time - start_time

        if standalone:
            print(f"Finished in {end_time - start_time:.4f}s")
            print(f"output : {self.output}")

        return self.output

    # This function take 2 coordinate and compute the size of the area
    def compute_area(self, coord_1, coord_2):
        x1, y1 = int(coord_1.split(",")[0]), int(coord_1.split(",")[1])
        x2, y2 = int(coord_2.split(",")[0]), int(coord_2.split(",")[1])

        return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


if __name__ == "__main__":
    solution = Solution()
    solution.resolve(True)
