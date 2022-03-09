
max_score = -100
runner_up_score = -100
n = 5
arr = [-10,-11,0,0,0]

for k in range(n):
    if arr[k] > max_score:
        runner_up_score = max_score
        max_score = arr[k]
    elif arr[k] == max_score:
        pass
    else:
        if arr[k] > runner_up_score:
            runner_up_score = arr[k]

print(runner_up_score)