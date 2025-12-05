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
            
            inside = False

            for range_id in input_ranges:
                if range_id[0] < start and start < range_id[1]:
                    if end > range_id[1]:
                        range_id[1] = end
                        inside = True
                        break
                elif range_id[0] > start and end > range_id[0]:
                    if range_id[1] > end:
                        range_id[0] = start
                        inside = True
                    else:
                        range_id[0] = start
                        range_id[1] = end


        

            input_ranges.append((int(start), int(end)))

start_time = time.time()

for id_range in input_ranges:
    output += id_range[1] - id_range[0] + 1

end_time = time.time()
print(f"Finished in {end_time - start_time:.4f}s")
print(f"output : {output}")

