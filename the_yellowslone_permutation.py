
import math
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def generate_the_yellowstone_permutation(n):
    sequence = [1, 2, 3]
    i = 4
    smallestNotDoneYet = 4
    while len(sequence) < n:
        # no term is repeated
        # gcd(a(n), a(n-1)) = 1
        # gcd(a(n), a(n-2)) > 1
        # always pick the smallest
        if i not in sequence and math.gcd(i, sequence[len(sequence) - 1]) == 1 and math.gcd(i, sequence[len(sequence) - 2]) > 1:
            sequence.append(i)
            for j in range(4,i):
                if j not in sequence:
                    smallestNotDoneYet = j - 1
                    break
            i = smallestNotDoneYet
        i += 1
    return sequence

print(generate_the_yellowstone_permutation(100))

# Basic Scatterplots
n = 10
sequence = generate_the_yellowstone_permutation(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y='Number', data=df)
plt.savefig("images/10.png")
plt.show()

n = 100
sequence = generate_the_yellowstone_permutation(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y='Number', data=df)
plt.savefig("images/100.png")
plt.show()

n = 1000
sequence = generate_the_yellowstone_permutation(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y='Number', data=df)
plt.savefig("images/1000.png")
plt.show()

n = 10000
sequence = generate_the_yellowstone_permutation(n)
df = pd.DataFrame(sequence, columns=["Number"])
df['index'] = [i for i in range(n)]
sns.scatterplot(x="index", y='Number', data=df)
plt.savefig("images/10000.png")
plt.show()