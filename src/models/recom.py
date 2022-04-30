import pandas as pd
import numpy as np
import random

arr = []
for i in range (39586):
    arr.append(random.randint(0,1))
newArr = np.reshape(arr, (39586,1))
df1= pd.DataFrame(newArr)
data = pd.read_csv("./data/results.csv")
