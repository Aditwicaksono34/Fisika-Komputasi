import math
import random
import statistics
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.express as px
from collections import Counter
plt.style.use('seaborn-whitegrid')

R_list = np.linspace(2.0, 4.0, 20000)
x0 = 0.3
N = 1200

def logis(r):
    x_list = [x0]
    for i in range(N - 1):
        x_list.append(r * x_list[-1] * (1 - x_list[-1]))
    return x_list[200:]


non_repetitive = []
for r in R_list:
    non_repetitive.append(len(Counter(logis(r))))

plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(16, 6), facecolor='lightgray')
plt.xlabel('The value of R')
plt.ylabel('Counter non-repetitive numbers')
plt.title(f'\nCounter non-repetitive numbers\n\n2.0 < R < 4.0  |  x0=0.3\n')
plt.scatter(R_list, non_repetitive, color='red', s=3)
plt.show()