from abc import ABC, abstractmethod


class Challenge(ABC):
    """This is the abstract class of a single challenge
    - output is the solution of the challenge
    - time_elapsed is the time that the methode resolved() made to finish
    """

    def __init__(self):
        self.output: int = 0
        self.time_elapsed: int | float = 0

    @abstractmethod
    def resolve(self, standalone: bool = False) -> int:
        print("Call this function to resolve a new Challenge !")
        return 0
