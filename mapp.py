#Convert marks (out of 50 → out of 100) using a normal loop
#Using map() 
marks_50 = [35, 42, 28, 50, 31]
marks_100 = list(map(lambda x: x * 2, marks_50))
print(marks_100)

#using for loop instead
marks_50 = [35, 42, 28, 50, 31]
marks_100 = []

for mark in marks_50:
    marks_100.append(mark * 2)

print(marks_100)
