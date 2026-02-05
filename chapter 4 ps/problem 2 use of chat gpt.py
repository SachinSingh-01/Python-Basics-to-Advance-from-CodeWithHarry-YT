marks = []

for i in range(6):
    mark = int(input(f"Enter marks for student {i + 1}: "))
    marks.append(mark)

marks.sort()

print("Sorted marks:", marks)
