"""
Bill Splitter

Description: A simple Python program that splits a restaurant bill among multiple people and calculates the tip.

Author: Shrestha Sarangi
"""

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

num_people = int(input("How many people are there in the group?: "))
if num_people <= 0:
    print("Number of people must be greater than 0.")
    exit()
else:
    names = []

for i in range(num_people):
    name = input(f"Enter the name of person #{i+1}: ").strip()
    names.append(name)

total_bill = get_float("Enter the bill amount in number only: ")

share = round(total_bill / num_people, 2)

print("*" * 40)
print("\n -----Bill Summary-----")
print(f"Total bill: {total_bill}")
print(f"Each person should pay: ₹{share}")

for name in names:
    print(f"{name} owes {share} rupees")
print("\n" + "*" * 40)