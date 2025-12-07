import time
import traceback
from pathlib import Path

from challenge import Challenge


class Solution(Challenge):
    def __init__(self):
        super().__init__()
        self.challenge_dir = Path(__file__).parent

    def recover_max(self, liste):
        # This function return the max of an integer list and his index
        maximum = liste[0]
        index = 0
        for i in range(0, len(liste)):
            if int(liste[i]) > int(maximum):
                maximum = liste[i]
                index = i
        return maximum, index

    def resolve(self, standalone=False):
        start_time = time.time()

        with open(self.challenge_dir / "input.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                try:
                    number = ""
                    start = 0
                    # We parse each value of a sub array that respect 2 conditions :
                    # - The start is at least the index of the last number + 1
                    # - The last number of the subarray is made just to let enough space at the end for others number
                    for i in range(11, -1, -1):
                        maximum, index = self.recover_max(line[start : len(line) - i])
                        number += str(maximum)
                        start += index + 1

                    # We increment our output
                    self.output += int(number)

                except Exception as e:
                    print(e)
                    traceback.print_exc()
                    continue

        end_time = time.time()
        self.time_elapsed = end_time - start_time

        if standalone:
            print(f"Finished in {end_time - start_time:.4f}s")
            print(f"output : {self.output}")

        return self.output


if __name__ == "__main__":
    Solution().resolve(standalone=True)
