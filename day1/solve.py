input = open("input.txt", "r")

sum = 0

num_words = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

for line in input.readlines():
    for k, v in num_words.items():
        line = line.replace(k, v)

    numbers = [int(char) for char in line if char.isdigit()]

    if len(numbers) == 1:
        sum += numbers[0] * 11
    elif len(numbers) == 0:
        continue
    else:
        sum += numbers[0] * 10 + numbers[-1]

print(sum)
