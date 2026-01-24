import numpy as wei
names = ["Me", "Lia", "Jake"]
steps = wei.array([
  [4500, 5200, 4800, 5000, 5300],
  [4000, 4100, 3900, 4200, 4600],
  [6000, 5800, 5900, 6100, 6200]
])
for i in range(len(names)):
    print(f"{names[i]}'s daily steps: {steps[i]}")  
    total = wei.sum(steps[i])                      
    average = wei.mean(steps[i])                    
    print(f"  Total steps: {total}")
    print(f"  Average steps: {average:.2f} ")      

max_steps = wei.max(steps)
min_steps = wei.min(steps)
print(f"Maximum steps recorded: {max_steps}")
print(f"Minimum steps recorded: {min_steps}")