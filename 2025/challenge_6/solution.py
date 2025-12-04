import time
import traceback

def recover_max(liste):
    # This function return the max of an integer list and his index
    maximum = liste[0]
    index = 0
    for i in range(0, len(liste)):
        if int(liste[i]) > int(maximum):
            maximum = liste[i]
            index = i
    return maximum, index

output = 0
start_time = time.time()

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            continue
        try:
            size = len(line)
            number = ""
            start = 0
            # We parse each value of a sub array that respect 2 conditions : 
            # - The start is at least the index of the last number + 1
            # - The last number of the subarray is made just to let enough space at the end for others number
            for i in range(11, -1, -1):
                maximum, index = recover_max(line[start: len(line) - i])
                number += str(maximum)
                start += index + 1

            # We increment our output
            output += int(number)

        except Exception as e:
            print(e)
            traceback.print_exc()
            continue

end_time = time.time()
print(f"Finished in {end_time - start_time:.4f}s")
print(f"output : {output}")

