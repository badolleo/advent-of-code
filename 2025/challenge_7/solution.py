import time


class Challenge:
    def __init__(self):
        self.time_elapsed = 0
        self.output = 0

    def get_neighbor(self, matrice, x, y):
        number_of_neighbor = 0
        rows = len(matrice)
        cols = len(matrice[0])

        # We go throught the 8 directions
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                # We ignore central case
                if dx == 0 and dy == 0:
                    continue

                nx, ny = x + dx, y + dy

                # We verifie if the neighbor is inside the limits
                if 0 <= nx < rows and 0 <= ny < cols:
                    if matrice[nx][ny] == "@":
                        number_of_neighbor += 1

        return number_of_neighbor

    def resolve(self, standalone=False):
        start_time = time.time()
        input = []

        with open("input.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line != "":
                    input.append(list(line.strip()))

        for y in range(0, len(input)):
            for x in range(0, len(input[y])):
                if input[y][x] == "@":
                    if self.get_neighbor(input, y, x) < 4:
                        self.output += 1

        end_time = time.time()
        self.time_elapsed = end_time - start_time

        if standalone:
            print(f"Finished in {end_time - start_time:.4f}s")
            print(f"output : {self.output}")

        return self.output


if __name__ == "__main__":
    Challenge().resolve(standalone=True)
