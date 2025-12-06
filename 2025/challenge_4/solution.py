import time


class Challenge:
    def __init__(self):
        self.output = 0
        self.time_elapsed = 0

    def resolve(self, standalone=False):
        start_time = time.time()

        output = 0
        input = ""

        # This function in n equal parts the array s
        def split_equal_parts(s, n):
            taille_partie = len(s) // n
            return [s[i : i + taille_partie] for i in range(0, len(s), taille_partie)]

        # This function check if the number is a repetition of a patern or not
        # We rty first to split the number in 2, and we check if both parts are equals.
        # If not, we increment the number of part we split the number until we reach the one by one element repetition
        def check_patern(number):
            for patern_size in range(len(number) // 2, 0, -1):
                if len(number) % (len(number) // patern_size) != 0:
                    continue

                paterns_list = split_equal_parts(number, len(number) // patern_size)

                if len(set(paterns_list)) == 1:
                    return True
            return False

        with open("input.txt", "r") as file:
            for line in file:
                input += line

        input_list = input.split(",")

        # We try, for each range of our input, if each element of this range is a patern repetition
        for rng in input_list:
            number_1 = rng.split("-")[0]
            number_2 = rng.split("-")[1]
            for number in range(int(number_1), int(number_2) + 1):
                number = str(number)
                result = check_patern(number)

                # Result is True if the number we consider is a patern repetition or not
                if result:
                    self.output += int(number)

        end_time = time.time()
        self.time_elapsed = end_time - start_time

        if standalone:
            print(f"Finished in {end_time - start_time:.4f}s")
            print(f"output : {output}")

        return self.output


if __name__ == "__main__":
    Challenge().resolve(standalone=True)
