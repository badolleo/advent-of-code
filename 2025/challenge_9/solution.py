import time
from pathlib import Path

from challenge import Challenge


class Solution(Challenge):
    def __init__(self):
        super().__init__()
        self.challenge_dir = Path(__file__).parent

    def resolve(self, standalone=False):
        start_time = time.time()
        input_ranges = []
        input_ids = []

        with open(self.challenge_dir / "input.txt", "r") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                # if there is a dash, that means it's a range
                if "-" in line:
                    line = line.split("-")
                    start = line[0]
                    end = line[1]
                    input_ranges.append((start, end))
                # else it's a single id
                else:
                    input_ids.append(int(line))

        # And then we iterate on each id to
        for id in input_ids:
            for id_range in input_ranges:
                if id >= int(id_range[0]) and id <= int(id_range[1]):
                    self.output += 1
                    break

        end_time = time.time()
        self.time_elapsed = end_time - start_time

        if standalone:
            print(f"Finished in {end_time - start_time:.4f}s")
            print(f"output : {self.output}")

        return self.output


if __name__ == "__main__":
    challenge = Solution()
    challenge.resolve(standalone=True)
