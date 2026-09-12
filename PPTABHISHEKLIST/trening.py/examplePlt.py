import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = [
    [75, 80, 70],
    [80, 95, 70]
]

df = pd.DataFrame(
    data,
    index=['s1', 's2'],
    columns=["Physics", "Chemistry", "Maths"]
)

print(df)

# Total marks
total = df.sum(axis=1)

print("Total Marks:")
print(total)

# Create 2 graphs
plt.figure(figsize=(10, 5))

# Graph 1: Subject-wise comparison
plt.subplot(2, 2, 1)

plt.plot(df.columns, df.iloc[0], marker='o', label="Student 1")
plt.plot(df.columns, df.iloc[1], marker='o', label="Student 2")

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Subject-wise Marks Comparison")
plt.legend()
plt.grid(True)



plt.subplot(2, 2, 2)

plt.bar(df.columns, df.iloc[0], label="Student 1")
plt.bar(df.columns, df.iloc[1], label="Student 2")

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Subject-wise Marks Comparison")
plt.legend()
plt.grid(True)



# Graph 2: Total marks comparison
plt.subplot(2, 2, 3)

plt.plot(df.index, total)

plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.title("Total Marks Comparison")
plt.grid(axis='y')

plt.subplot(2, 2, 4)

plt.bar(df.index, total)

plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.title("Total Marks Comparison")
plt.grid(axis='y')

plt.tight_layout()
plt.show()