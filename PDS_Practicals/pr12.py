# Aim: To calculate statistical measures and perform
# statistical tests using SciPy.

from scipy import stats

data = list(map(float, input(
    "Enter dataset values separated by spaces: "
).split()))

if len(data) == 0:
    print("Dataset cannot be empty.")
else:
    print("Mean:", stats.tmean(data))
    print("Median:", stats.scoreatpercentile(data, 50))
    print("Mode:", stats.mode(data, keepdims=True).mode[0])
    print("Variance:", stats.tvar(data) if len(data) >= 2 else "Need 2 values")
    print("Standard Deviation:",
          stats.tstd(data) if len(data) >= 2 else "Need 2 values")

    # One-sample t-test
    if len(data) >= 2:
        population_mean = float(input(
            "Enter hypothesized population mean: "
        ))

        t_stat, p_value = stats.ttest_1samp(
            data, population_mean
        )

        print("\nT-statistic:", t_stat)
        print("P-value:", p_value)

        alpha = 0.05
        if p_value < alpha:
            print("Reject the null hypothesis.")
        else:
            print("Fail to reject the null hypothesis.")

    # Normality test
    if len(data) >= 8:
        statistic, p = stats.normaltest(data)
        print("\nNormality Test P-value:", p)
    else:
        print("\nNormality test requires at least 8 observations.")