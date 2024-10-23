num = int(input("Enter a number: "))

total = 0

for current_number in range(1, num + 1):
    total += current_number

print(f"Total:\n{total}")
