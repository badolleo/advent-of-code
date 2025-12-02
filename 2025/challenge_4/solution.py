
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
        
        size_of_substring = 1
        for _ in range(1, len(number)//2):
            first_substring = ""
            verif = True
            if len(number) % size_of_substring != 0:
                continue
            for substring in range(0, len(number), size_of_substring):
                if first_substring == "":
                    first_substring = number[substring:substring + size_of_substring]
                    continue
                else:
                    if number[substring:substring + size_of_substring] != first_substring:
                        verif = False
                        break
            if verif:
                output += number
                break
            size_of_substring += 1

print(output)
