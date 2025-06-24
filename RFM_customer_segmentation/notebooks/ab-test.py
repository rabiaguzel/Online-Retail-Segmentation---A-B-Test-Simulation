import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

df = pd.read_csv("data/rfm_with_segments.csv")

at_risk = df[df["Segment"] == "At Risk"].copy()

np.random.seed(42)
at_risk["group"] = np.where(np.random.rand(len(at_risk)) < 0.5, "A", "B")


at_risk.loc[at_risk["group"]=="B", "Frequency"] *= 1.20
at_risk.loc[at_risk["group"]=="B", "Monetary"] *= 1.15

mean_freq_a = at_risk[at_risk["group"]=="A"]["Frequency"].mean()
mean_freq_b = at_risk[at_risk["group"]=="B"]["Frequency"].mean()

mean_monetary_a = at_risk[at_risk["group"]=="A"]["Monetary"].mean()
mean_monetary_b = at_risk[at_risk["group"]=="B"]["Monetary"].mean()

t_stat_freq, p_val_freq = ttest_ind(
    at_risk[at_risk["group"]=="A"]["Frequency"],
    at_risk[at_risk["group"]=="B"]["Frequency"]
)

t_stat_mon, p_val_mon = ttest_ind(
    at_risk[at_risk["group"]=="A"]["Monetary"],
    at_risk[at_risk["group"]=="B"]["Monetary"]
)

print(f"Group A mean Frequency: {mean_freq_a:.2f}")
print(f"Group B mean Frequency: {mean_freq_b:.2f}")
print(f"Frequency T-test p-value: {p_val_freq:.4f}")

print(f"Group A mean Monetary: {mean_monetary_a:.2f}")
print(f"Group B mean Monetary: {mean_monetary_b:.2f}")
print(f"Monetary T-test p-value: {p_val_mon:.4f}")
