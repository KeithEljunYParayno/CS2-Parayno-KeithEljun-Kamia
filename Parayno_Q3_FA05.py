import numpy as np
names = ["Me", "Lia", "Jake"]

steps = [
  [4500, 5200, 4800, 5000, 5300],
  [4000, 4100, 3900, 4200, 4600],
  [6000, 5800, 5900, 6100, 6200]
]

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

day_totals = []

for j in range(len(days)):
    total = 0
    for i in range(len(names)):
        total += steps[i][j]
    day_totals.append(total)
    print(days[j], "total steps:", total)


max_total = day_totals[0]
max_index = 0
for j in range(1, len(day_totals)):
    if day_totals[j] > max_total:
        max_total = day_totals[j]
        max_index = j

print("Most active day overall:", days[max_index], "with", max_total, "steps")
