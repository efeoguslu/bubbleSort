# this sorting program implements the bubble sort algorithm

noGrades = int(input("enter number of grades"))

grades = []
totalGrade = 0
highGrade = 0  # initiliaze it as low as possible
lowGrade = 100  # initiliaze it as high as possible
temp = 0

for i in range(0, noGrades, 1):
    grade = float(input("enter grade: "))
    grades.append(grade)
    print(grades)

for i in range(0, noGrades, 1):
    totalGrade += grades[i]

average = totalGrade/noGrades

print('average: ', average)

for i in range(0, noGrades, 1):
    if(grades[i] > highGrade):
        highGrade = grades[i]

for i in range(0, noGrades, 1):
    if(grades[i] < lowGrade):
        lowGrade = grades[i]

print('low grade: ', lowGrade)
print('high grade: ', highGrade)

for i in range(0, noGrades, 1):
    for j in range(0, noGrades-i-1, 1):
        if grades[j] > grades[j+1]:
            temp = grades[j]
            grades[j] = grades[j+1]
            grades[j+1] = temp

print('sorted list: ', grades)
