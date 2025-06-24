import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
import random
import gradio as gr
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/rfm_with_segments.csv") 

def run_ab_test(discount_effect=0.3, discount_increment=1):
    at_risk = df[df["Segment"] == "At Risk"].copy()
    at_risk = at_risk.sample(frac=1, random_state=42).reset_index(drop=True)

    mid_index = len(at_risk) // 2
    group_a = at_risk.iloc[:mid_index].copy()
    group_b = at_risk.iloc[mid_index:].copy()

    group_b["Frequency"] = group_b["Frequency"].apply(lambda x: x + discount_increment if random.random() < discount_effect else x)

    mean_a = group_a["Frequency"].mean()
    mean_b = group_b["Frequency"].mean()

    t_stat, p_val = ttest_ind(group_a["Frequency"], group_b["Frequency"])

    plt.figure(figsize=(8,5))
    sns.kdeplot(group_a["Frequency"], label="Group A (No Discount)")
    sns.kdeplot(group_b["Frequency"], label="Group B (Discount)")
    plt.xlabel("Frequency")
    plt.ylabel("Density")
    plt.title("A/B Test Frequency Distribution")
    plt.legend()

    plt.tight_layout()
    plt.savefig("ab_test_plot.png")
    plt.close()

    summary = (
        f"Total 'At Risk' customers: {len(at_risk)}\n"
        f"Group A size: {len(group_a)}\n"
        f"Group B size: {len(group_b)}\n"
        f"Group A mean Frequency: {mean_a:.3f}\n"
        f"Group B mean Frequency: {mean_b:.3f}\n"
        f"T-test p-value: {p_val:.4e}"
    )

    return summary, "ab_test_plot.png"

discount_effect_slider = gr.Slider(minimum=0, maximum=1, value=0.3, step=0.05, label="Discount Effect Probability")
discount_increment_slider = gr.Slider(minimum=0, maximum=5, value=1, step=0.1, label="Frequency Increment for Discounted Customers")

iface = gr.Interface(
    fn=run_ab_test,
    inputs=[discount_effect_slider, discount_increment_slider],
    outputs=["text", "image"],
    title="A/B Test Dashboard - Customer Frequency",
    description="Simulate an A/B test on 'At Risk' customer segment. Adjust discount effect and increment to see impact."
)

if __name__ == "__main__":
    iface.launch()
