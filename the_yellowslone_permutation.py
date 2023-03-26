
import math
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def generate_the_yellowstone_permutation(n):
    sequence = [1, 2, 3]
    i = 4
    while len(sequence) < n:
        # no term is repeated
        # always pick the smallest
        # gcd(a(n), a(n-1)) = 1
        # gcd(a(n), a(n-2)) > 1
        if math.gcd(i, sequence[len(sequence) - 1]) == 1 and math.gcd(i, sequence[len(sequence) - 2]) > 1 and i not in sequence:
            sequence.append(i)
            i = 4
        i += 1
    return sequence

sequence = generate_the_yellowstone_permutation(20)
print(sequence)

# Basic Scatterplots
'''
n = 10
sequence = generate_the_yellowstone_permutation(n)
df = pd.DataFrame(sequence, columns=["Number"])
indices = [i for i in range(n)]
df['index'] = indices
sns.scatterplot(x="index", y='Number', data=df)
plt.show()

n = 100
sequence = generate_the_yellowstone_permutation(n)
df = pd.DataFrame(sequence, columns=["Number"])
indices = [i for i in range(n)]
df['index'] = indices
sns.scatterplot(x="index", y='Number', data=df)
plt.show()

n = 1000
sequence = generate_the_yellowstone_permutation(n)
df = pd.DataFrame(sequence, columns=["Number"])
indices = [i for i in range(n)]
df['index'] = indices
sns.scatterplot(x="index", y='Number', data=df)
plt.show()
'''

n = 10000
sequence = generate_the_yellowstone_permutation(n)
df = pd.DataFrame(sequence, columns=["Number"])
indices = [i for i in range(n)]
df['index'] = indices
sns.scatterplot(x="index", y='Number', data=df)
plt.show()