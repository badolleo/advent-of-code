import dis
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
        self.input = np.array([])
        self.box_circuits: list[list] = []

    def resolve(self, standalone: bool = False) -> int:
        start_time = time.time()
        liste = []

        # Recovering each lines of the input as lists
        with open(self.challenge_dir / "input_2.txt") as file:
            for line in file:
                line = line.strip().split(",")
                liste.append([int(line[0]), int(line[1]), int(line[2])])

        self.input = np.array(liste)

        pair_with_distances = self.get_smallest_distances()

        limit = 0

        for distance in pair_with_distances:
            self.insert_box(self.input[distance[0]], self.input[distance[1]])
            if limit == 999:
                break
            limit += 1

        self.comput_final_value()

        end_time = time.time()
        self.time_elapsed = end_time - start_time

        if standalone:
            print(f"Finished in {end_time - start_time:.4f}s")
            print(f"output : {self.output}")

        return self.output

    # Return all distances between each points of our input and sort them from the smaller to the bigger
    def get_smallest_distances(self):
        distances = cdist(self.input, self.input, metric="euclidean")

        triu_indices = np.triu_indices(len(self.input), k=1)
        i_indices, j_indices = triu_indices
        all_distances = distances[triu_indices]

        n_pairs = len(i_indices)
        pairs = np.zeros(n_pairs, dtype=[("i", int), ("j", int), ("dist", float)])
        pairs["i"] = i_indices
        pairs["j"] = j_indices
        pairs["dist"] = all_distances

        pairs.sort(order="dist")
        return pairs

    # Compute the distance between 2 points
    def compute_distance(self, box1, box2):
        return math.sqrt(
            (box2[0] - box1[0]) ** 2
            + (box2[1] - box1[1]) ** 2
            + (box2[2] - box1[2]) ** 2
        )

    def get_circuit_from_box(self, box):
        for c in self.box_circuits:
            if any(
                np.array_equal(box, p) for p in c
            ):  # That means that a point of this circuit is box
                return c
        return None  # Nothing founded than we return None

    # This function insert 2 box ( it represents a connexion ) insde a circuits
    def insert_box(self, box1, box2):
        circuit_b1 = self.get_circuit_from_box(box1)
        circuit_b2 = self.get_circuit_from_box(box2)

        if (
            circuit_b1 is circuit_b2 is not None
        ):  # We first check if they are not in them same circuit
            return
        elif (
            circuit_b1 is not None and circuit_b2 is not None
        ):  # This case means that both of our boxes are already in a circuit, we have to merge them
            circuit_b1.extend(circuit_b2)
            for i, circuit in enumerate(self.box_circuits):
                if circuit is circuit_b2:
                    del self.box_circuits[i]
                    break
        elif (
            circuit_b1 is None and circuit_b2 is not None
        ):  # We add box1 in the circuit of box2
            circuit_b2.append(box1)
        elif (
            circuit_b2 is None and circuit_b1 is not None
        ):  # We add box2 in the circuit of box1
            circuit_b1.append(box2)
        else:
            self.box_circuits.append(
                [box1, box2]
            )  # Either box1 and box2 didnt have circuit yet so we create a new one

    def comput_final_value(self):
        self.box_circuits.sort(key=len)
        self.box_circuits = self.box_circuits[::-1]
        self.output = int(
            np.prod(
                [
                    len(self.box_circuits[0]),
                    len(self.box_circuits[1]),
                    len(self.box_circuits[2]),
                ]
            )
        )


if __name__ == "__main__":
    solution = Solution()
    solution.resolve(True)
