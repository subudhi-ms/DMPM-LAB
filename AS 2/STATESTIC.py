import numpy as np

# Input
l = [int(x) for x in input("Enter the list of numbers (comma separated): ").split(",")]

# -------------------- Q1: Mean without NumPy --------------------
mean_without = sum(l) / len(l)
print("\nQ1. Mean without NumPy =", mean_without)

# -------------------- Q2: Mean with NumPy --------------------
mean_with = np.mean(l)
print("Q2. Mean with NumPy =", mean_with)

# -------------------- Q3: Median without NumPy --------------------
sorted_list = sorted(l)

if len(sorted_list) % 2 == 0:
    median_without = (sorted_list[len(sorted_list)//2] +
                      sorted_list[len(sorted_list)//2 - 1]) / 2
else:
    median_without = sorted_list[len(sorted_list)//2]

print("Q3. Median without NumPy =", median_without)

# -------------------- Q4: Median with NumPy --------------------
median_with = np.median(l)
print("Q4. Median with NumPy =", median_with)

# -------------------- Q5: Mode without NumPy --------------------
count = {}

for x in l:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1

mode_without = max(count, key=count.get)
print("Q5. Mode without NumPy =", mode_without)

# -------------------- Q6: Mode with NumPy --------------------
mode_with = np.bincount(l).argmax()
print("Q6. Mode with NumPy =", mode_with)

# -------------------- Q7: Variance without NumPy --------------------
mean = sum(l) / len(l)
sum_squared_diff = sum((x - mean) ** 2 for x in l)
variance_without = sum_squared_diff / len(l)

print("Q7. Variance without NumPy =", round(variance_without, 4))

# -------------------- Q8: Variance with NumPy --------------------
variance_with = np.var(l)

print("Q8. Variance with NumPy =", round(variance_with, 4))

# -------------------- Q9: Standard Deviation --------------------
sd_without = (variance_without) ** 0.5
sd_with = np.std(l)

print("Q9. Standard Deviation without NumPy =", round(sd_without, 4))
print("Q9. Standard Deviation with NumPy =", round(sd_with, 4))

# -------------------- Q10: Variance & Standard Deviation --------------------
print("\nQ10.")
print("Variance =", round(variance_without, 4))
print("Standard Deviation =", round(sd_without, 4))