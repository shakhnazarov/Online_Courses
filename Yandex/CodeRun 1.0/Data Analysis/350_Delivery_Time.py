import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
def simulation():
    x_1 = np.random.uniform(10,30)
    x_2 = np.random.uniform(2,7)
    x_3 = np.random.uniform(5, 20)
    x_4 = np.random.uniform(5, 15)

    return max(x_1, x_2 + x_3) + x_4

num_sim = 10000000

draws = []
for i in range(num_sim):
    draws.append(simulation())

#sns.histplot(draws)
#plt.show()
print(np.percentile(draws, 95))
