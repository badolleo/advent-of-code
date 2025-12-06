import time
from doctest import OutputChecker


class Challenge:
    def __init__(self):
        self.output = 0
        self.time_elapsed = 0

    def resolve(self, standalone=False):
        start_time = time.time()
        input_ranges = []

        with open("input.txt", "r") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                if "-" in line:
                    line = line.split("-")
                    start = int(line[0])
                    end = int(line[1])

                    inside = False
                    # For each range already registered, we will look if it overlaps with our new interval
                    for rng in input_ranges:
                        if (
                            start < rng[0] and end > rng[1]
                        ):  # Scenario ou notre nouvel intervale englobe rng
                            rng[1] = 0
                            rng[0] = 1
                        elif (
                            start < rng[0] and end >= rng[0] and end <= rng[1]
                        ):  # Scenario ou notre nouvel intervale a sa borne min inferieur et sa borne max dans rng
                            end = rng[0] - 1
                        elif (
                            start >= rng[0] and start <= rng[1] and end > rng[1]
                        ):  # Scenario ou notre nouvel intervale à sa borne max supérieur et sa borne min dans rng
                            start = rng[1] + 1
                        elif (
                            start >= rng[0] and end <= rng[1]
                        ):  # Scenario ou le nouvel interval est à l'interieur de rng
                            inside = True
                            break

                    if not inside:
                        input_ranges.append([start, end])

        for rng in input_ranges:
            self.output += rng[1] - rng[0] + 1

        end_time = time.time()
        self.time_elapsed = end_time - start_time

        if standalone:
            print(f"Finished in {end_time - start_time:.4f}s")
            print(f"output : {self.output}")

        return self.output


if __name__ == "__main__":
    challenge = Challenge()
    challenge.resolve()
