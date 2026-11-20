from Student import Avg, max, status

name = input("Enter Student name: ")

grades = [15, 18, 20, 17]

print("\nStudent:", name)
print("Avg =", Avg(grades))
print("max =", max(grades))
print("status =", status(grades))