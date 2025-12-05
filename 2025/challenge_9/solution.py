import time

input_ranges = []
input_ids = []
output = 0

with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip()

        if line == "":
            continue

        if '-' in line:
            line = line.split('-')
            start = line[0]
            end = line[1]
            input_ranges.append((start, end))

        else:
            input_ids.append(int(line))

start_time = time.time()

for id in input_ids:
    for id_range in input_ranges:
        if id >= int(id_range[0]) and id <= int(id_range[1]):
            output += 1
            break

end_time = time.time()
print(f"Finished in {end_time - start_time:.4f}s")
print(f"output : {output}")

