import numpy as np
marks = np.array([
    [80,78,45],
    [85,65,59],
    [48,89,55]
])
#average of marks in python
subject = ["SQL" ,"PYTHON","JAVA"]
print(np.mean(marks[:, 1]))
print(np.max(marks[:,0]))
