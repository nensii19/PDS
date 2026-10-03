# Aim: To perform a one-sample t-test and interpret the
# result using the p-value and significance level.

from scipy.stats import ttest_1samp

data = list(map(float, input(
    "Enter sample values separated by spaces: "
).split()))

if len(data) < 2:
    print("Enter at least two sample values.")
else:
    hypothesized_mean = float(input(
        "Enter hypothesized population mean: "
    ))
    alpha = float(input(
        "Enter significance level (e.g. 0.05): "
    ))

    if not 0 < alpha < 1:
        print("Significance level must be between 0 and 1.")
    else:
        t_stat, p_value = ttest_1samp(
            data, hypothesized_mean
        )

        print("\nT-statistic:", t_stat)
        print("P-value:", p_value)
        print("Significance Level:", alpha)

        if p_value < alpha:
            print("Reject the null hypothesis.")
            print("The sample provides evidence against the hypothesized mean.")
        else:
            print("Fail to reject the null hypothesis.")
            print("There is insufficient evidence against the hypothesized mean.")