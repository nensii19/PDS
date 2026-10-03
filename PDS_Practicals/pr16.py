# Aim: To plot Normal and Exponential distributions and
# demonstrate the Central Limit Theorem.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon

mean = float(input("Enter normal distribution mean: "))
sd = float(input("Enter standard deviation: "))
scale = float(input("Enter exponential scale (positive): "))

if sd <= 0 or scale <= 0:
    print("Standard deviation and scale must be positive.")
else:
    x = np.linspace(mean - 4 * sd, mean + 4 * sd, 200)

    # Normal Distribution
    plt.subplot(1, 3, 1)
    plt.plot(x, norm.pdf(x, mean, sd))
    plt.title("Normal Distribution")
    plt.xlabel("Value")
    plt.ylabel("Density")

    # Exponential Distribution
    x2 = np.linspace(0, scale * 5, 200)
    plt.subplot(1, 3, 2)
    plt.plot(x2, expon.pdf(x2, scale=scale))
    plt.title("Exponential Distribution")
    plt.xlabel("Value")
    plt.ylabel("Density")

    # Central Limit Theorem
    population = np.random.exponential(scale, 10000)
    sample_means = []

    for i in range(1000):
        sample = np.random.choice(population, size=30)
        sample_means.append(np.mean(sample))

    plt.subplot(1, 3, 3)
    plt.hist(sample_means, bins=30, density=True)
    plt.title("Central Limit Theorem")
    plt.xlabel("Sample Mean")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()

    print("Population Mean:", np.mean(population))
    print("Mean of Sample Means:", np.mean(sample_means))