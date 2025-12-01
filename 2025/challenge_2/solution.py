position = 50
solution = 0

with open("input.txt", 'r') as file:
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
                position -= int(space)
            else:
                position += int(space)
        except Exception:
            continue

        # Recover the number of times we went through 0 if we made a rotation of 300 for exemple 
        solution += abs(position // 100)
        
        # We reset the position of the dial
        position = position % 100

print(solution)
