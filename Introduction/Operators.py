import numpy as np


# Comparison operators
# < | <= | > | >= | == | !=


height = np.array([1.73,1.68,1.71,1.89,1.79])

weight = np.array([65.4,59.2,63.6,88.4,68.7])

bmi = np.round(weight / height ** 2, 3)
print(bmi[bmi>23])

# Boolean operators
# and | or | not
# logical_and | logical_or | logical_not

LogicalAnd = np.logical_and(bmi>21, bmi<22)

print(bmi[LogicalAnd])