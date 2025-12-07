import time
from pathlib import Path

from challenge import Challenge


class Solution(Challenge):
    def __init__(self):
        super().__init__()
        self.position: int = 50
        self.challenge_dir = Path(__file__).parent

    def resolve(self, standalone: bool = False) -> int:
        start_time = time.time()

        with open(self.challenge_dir / "input.txt", "r") as file:
            # I copy past each lined of the input int the file input.txt
            # then we recover each line of treat them one by one
            for line in file:
                # We consider that the first char of each line is the direction and the others this number of click
                direction = line[0]
                space = line[1:-1]

                if space == "":
                    continue

                if direction == "L":
                    self.position -= int(space)
                else:
                    self.position += int(space)

                # We reset the position of the dial
                self.position = self.position % 100

                # Position is equals to 0 so we increment our solution by 1
                if self.position == 0:
                    self.output += 1

        end_time = time.time()
        self.time_elapsed = end_time - start_time
        if standalone:
            print(f"Finished in {self.time_elapsed:.4f}s")
            print(f"output : {self.output}")

        return self.output


if __name__ == "__main__":
    Solution().resolve(standalone=True)
