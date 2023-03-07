universities = [
    ["california", 2175, 37704],
    ["Harvard", 19627, 39849],
    ["MIT", 10566, 40732],
    ["Princeton", 7802, 37000],
    ["Rice", 5879, 35551],
    ["Stanford", 19535, 40569],
    ["Yale", 11701, 40500],
]


def enrollment_stats(x):
    students = []
    tuition = []
    for i in range(len(x)):
        students.append(x[i][1])
    for i in range(len(x)):
        tuition.append(x[i][2])

    data = (students, tuition)
    print("****************************")
    print("Total students: ", sum(students))
    print("Total tuition: $", sum(tuition))
    print("----------------------------")
    print("Student mean: %.2f" % mean(students))
    print("Student median: ", median(students))
    print("----------------------------")
    print("Tuition mean: %.2f" % mean(tuition))
    print("Tuition median: ", median(tuition))
    print("****************************")

def sum(x):
    sum = 0
    for i in range(len(x)):
        sum += x[i]
    return sum

def mean(x):
    return sum(x) / len(x)

def median(x):
    y = sorted(x)
    mid = int(len(y) / 2)
    return y[mid]

enrollment_stats(universities)
