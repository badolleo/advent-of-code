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
    Challenge().resolve(standalone=True)
