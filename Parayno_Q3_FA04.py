import numpy as np
names = ["Me", "Lia", "Jake"]

steps = [
  [4500, 5200, 4800, 5000, 5300],
  [4000, 4100, 3900, 4200, 4600],
  [6000, 5800, 5900, 6100, 6200]
]
totals = [] 
for i in range(len(names)):
    total = 0
    for j in range(len(steps[i])):
        total += steps[i][j]
    totals.append(total)
    print(names[i], "total steps:", total)
first_total = sum(steps[0])
max_total = first_total
min_total = first_total
max_person = names[0]
if total > max_total:
    max_total = total
    max_person = names[i]
    
if total < min_total:
        min_total = total
print("Person with highest total steps:", max_person, "with", max_total, "steps")
print("Difference between highest and lowest total steps:", max_total - min_total)