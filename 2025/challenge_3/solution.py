
output = 0
input = ""
with open("input.txt", 'r') as file:
    for line in file:
        input += line

input_list = input.split(",")

for rng in input_list:
    
    number_1 = rng.split('-')[0]
    number_2 = rng.split('-')[1]
    
    for number in range(int(number_1), int(number_2) + 1):
        number = str(number)
        if len(number) % 2 == 0:
            if number[0:len(number)//2] == number[len(number)//2:len(number)]:
                output += int(number)

print(output)
