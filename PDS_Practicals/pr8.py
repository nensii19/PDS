# Aim: To calculate mean, median, mode, variance, standard
# deviation, range, quartiles and IQR of a dataset.

import statistics

data = list(map(float, input(
    "Enter numbers separated by spaces: "
).split()))

if len(data) == 0:
    print("Dataset cannot be empty.")
else:
    data.sort()
    n = len(data)

    mean = statistics.mean(data)
    median = statistics.median(data)
    modes = statistics.multimode(data)
    data_range = max(data) - min(data)

    print("Sorted Data:", data)
    print("Mean:", mean)
    print("Median:", median)
    print("Mode(s):", modes)
    print("Range:", data_range)

    if n >= 2:
        print("Variance:", statistics.variance(data))
        print("Standard Deviation:", statistics.stdev(data))
    else:
        print("Variance and standard deviation need 2 values.")

    # Quartiles and IQR need at least 2 observations
    if n >= 2:
        q1, q2, q3 = statistics.quantiles(
            data, n=4, method="inclusive"
        )
        print("Q1:", q1)
        print("Q2:", q2)
        print("Q3:", q3)
        print("IQR:", q3 - q1)