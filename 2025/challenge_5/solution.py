import time


class Challenge:
    def __init__(self):
        self.output = 0
        self.time_elapsed = 0

    def resolve(self, standalone=False):
        start_time = time.time()
        with open("input.txt", "r") as file:
            for line in file:
                line = line.strip()
                try:
                    n1 = 0
                    n2 = 0
                    size: int = len(line)

                    maximum1 = 0
                    for i in range(0, size - 1):
                        if line[maximum1] < line[i]:
                            maximum1 = i

                    n1 = int(line[maximum1])

                    maximum2 = maximum1 + 1
                    for i in range(maximum1 + 1, size):
                        if line[maximum2] < line[i]:
                            maximum2 = i

                    n2 = int(line[maximum2])

                    number = int(str(n1) + str(n2))
                    self.output += number
                except Exception:
                    continue

        end_time = time.time()
        self.time_elapsed = end_time - start_time

        if standalone:
            print(f"Finished in {end_time - start_time:.4f}s")
            print(self.output)

        return self.output


if __name__ == "__main__":
    Challenge().resolve(standalone=True)
