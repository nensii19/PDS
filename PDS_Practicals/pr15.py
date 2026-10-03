# Aim: To calculate and visualize Binomial and Poisson
# probability distributions using SciPy and Matplotlib.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson

# Binomial Distribution
n = int(input("Enter number of trials: "))
p = float(input("Enter probability of success (0 to 1): "))

if n < 0 or not 0 <= p <= 1:
    print("Invalid input.")
else:
    x = np.arange(0, n + 1)
    probabilities = binom.pmf(x, n, p)

    print("\nBinomial Probabilities:")
    for i, prob in zip(x, probabilities):
        print(i, ":", round(prob, 4))

    plt.subplot(1, 2, 1)
    plt.bar(x, probabilities)
    plt.title("Binomial Distribution")
    plt.xlabel("Number of Successes")
    plt.ylabel("Probability")

    # Poisson Distribution
    rate = float(input("\nEnter Poisson average rate: "))

    if rate < 0:
        print("Rate cannot be negative.")
    else:
        x2 = np.arange(0, max(10, int(rate * 3 + 1)) + 1)
        probabilities2 = poisson.pmf(x2, rate)

        print("\nPoisson Probabilities:")
        for i, prob in zip(x2, probabilities2):
            print(i, ":", round(prob, 4))

        plt.subplot(1, 2, 2)
        plt.bar(x2, probabilities2)
        plt.title("Poisson Distribution")
        plt.xlabel("Number of Events")
        plt.ylabel("Probability")

        plt.tight_layout()
        plt.show()