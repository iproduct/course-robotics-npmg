import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

if __name__ == '__main__':
    x = np.random.randn(100)
    ax = sns.distplot(x)

    plt.show()