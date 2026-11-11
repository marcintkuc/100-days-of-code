sequence_end = int(input("How many numbers would you like to add up? "))

total = 0
for number in range(1, sequence_end + 1):
    total += number

print(f"The total sum of numbers from 1 to {sequence_end} is: {total}")