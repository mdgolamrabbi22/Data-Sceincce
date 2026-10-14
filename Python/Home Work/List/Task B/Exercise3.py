numbers = [10, 20, 30, 40]

running_sum = 0
count = 0
averages = []


for i in numbers:
    running_sum = running_sum + i
    count = count + 1
    average = running_sum / count
    averages.append(average)

print(averages)
