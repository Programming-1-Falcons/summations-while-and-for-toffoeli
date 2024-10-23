
num = int(input("Enter a number: "))
total = 0
current_number = 1

while current_number <= num:
    total += current_number
    current_number += 1

print(f"Total:\n{total}")
