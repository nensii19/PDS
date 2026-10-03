# Aim: To create line, bar, histogram, pie and scatter plots
# using Matplotlib subplots and figure properties.

import matplotlib.pyplot as plt

n = int(input("Enter number of data points: "))

if n <= 0:
    print("Enter a positive number of data points.")
else:
    labels = []
    values = []

    for i in range(n):
        labels.append(input(f"Enter label {i + 1}: "))
        values.append(float(input(f"Enter value {i + 1}: ")))

    fig, ax = plt.subplots(2, 3, figsize=(14, 8))

    # Line Plot
    ax[0, 0].plot(labels, values, marker="o")
    ax[0, 0].set_title("Line Plot")
    ax[0, 0].set_xlabel("Labels")
    ax[0, 0].set_ylabel("Values")

    # Bar Chart
    ax[0, 1].bar(labels, values)
    ax[0, 1].set_title("Bar Chart")
    ax[0, 1].set_xlabel("Labels")
    ax[0, 1].set_ylabel("Values")

    # Histogram
    ax[0, 2].hist(values, bins=min(5, n))
    ax[0, 2].set_title("Histogram")
    ax[0, 2].set_xlabel("Values")
    ax[0, 2].set_ylabel("Frequency")

    # Pie Chart
    if all(v >= 0 for v in values) and sum(values) > 0:
        ax[1, 0].pie(values, labels=labels, autopct="%1.1f%%")
        ax[1, 0].set_title("Pie Chart")
    else:
        ax[1, 0].text(
            0.5, 0.5,
            "Pie chart needs non-negative values\nwith positive total",
            ha="center", va="center"
        )
        ax[1, 0].set_title("Pie Chart")

    # Scatter Plot
    ax[1, 1].scatter(range(n), values)
    ax[1, 1].set_title("Scatter Plot")
    ax[1, 1].set_xlabel("Data Point Number")
    ax[1, 1].set_ylabel("Values")

    # Sixth subplot: display basic statistics
    ax[1, 2].axis("off")
    ax[1, 2].text(
        0.1, 0.7,
        f"Count: {n}\nMean: {sum(values) / n:.2f}\n"
        f"Maximum: {max(values)}\nMinimum: {min(values)}",
        fontsize=12
    )
    ax[1, 2].set_title("Summary")

    fig.suptitle("Data Visualization Dashboard")
    plt.tight_layout()
    plt.show()