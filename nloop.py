"""
nested loops
"""

numbers = [5, 2, 5, 2, 2]

for number in numbers:
    totalcount = 0
    for count in range(number):
        totalcount += 1
        if totalcount == count:
            break
    print("x" * totalcount)

