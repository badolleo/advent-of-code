import time

output = 0
start = time.time()
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        try:
            n1 = 0
            n2 = 0
            size: int = len(line)
        
            maximum1 = 0
            for i in range(0, size - 1):
                if line[maximum1] < line[i]:
                    maximum1 = i

            n1 = int(line[maximum1])
        
            maximum2 = maximum1 + 1
            for i in range(maximum1 + 1, size):
                if line[maximum2] < line[i]:
                    maximum2 = i

            n2 = int(line[maximum2])
    
            number = int(str(n1) + str(n2))
            output += number
        except Exception:
            continue
end = time.time()
print(f"Finished in {end-start}s")
print(output)

