n = 1
student_marks = {'Harsh':[25,26.5,28]}
for _ in range(n):
    name, *line = input().split()
    print(name)
    scores = list(map(float, line))
    student_marks[name] = scores
