import numpy as np
names = ["Me", "Lia", "Jake"]
steps = np.array([
  [4500, 5200, 4800, 5000, 5300],
  [4000, 4100, 3900, 4200, 4600],
  [6000, 5800, 5900, 6100, 6200]
])
print("Name Steps                 Total Average")
for i in range(len(names)):
    total = 0
    print(names[i], end=" ")
    for j in range(len(steps[i])):
        print(steps[i][j], end=" ")
        total += steps[i][j]
    avg = total / len(steps[i])
    print(total, avg)

print("Maximum steps:", steps.max())
print("Minimum steps:", steps.min())