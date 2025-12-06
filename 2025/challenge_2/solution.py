import time


class Challenge:
    def __init__(self):
        self.position = 50
        self.output = 0
        self.time_elapsed = 0

    def resolve(self, standalone=False):
        start_time = time.time()

        with open("input.txt", "r") as file:
            # I copy past each lined of the input int the file input.txt
            # then we recover each line of treat them one by one
            for line in file:
                # We consider that the first char of each line is the direction and the others this number of click
                direction = line[0]
                space = line[1:-1]

                if space == "":
                    continue

                try:
                    if direction == "L":
                        self.position -= int(space)
                    else:
                        self.position += int(space)
                except Exception:
                    continue

                # Recover the number of times we went through 0 if we made a rotation of 300 for exemple
                self.output += abs(self.position // 100)

                # We reset the position of the dial
                self.position = self.position % 100

            end_time = time.time()
            self.time_elapsed = end_time - start_time
            if standalone:
                print(f"Finished in {end_time - start_time:.4f}s")
                print(f"output : {self.output}")

            return self.output


if __name__ == "__main__":
    Challenge().resolve(True)
