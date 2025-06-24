# 🛍️ Customer Segmentation & A/B Test Simulation

This project focuses on **segmenting e-commerce customers** using the **RFM (Recency, Frequency, Monetary)** model and simulating a basic **A/B test** on the *At Risk* customer group.

---

## 🎯 Project Objectives

- Segment customers into groups like *Loyal*, *At Risk*, and *Recent*
- Simulate a marketing campaign (e.g., discount) to observe behavior changes
- Evaluate the effectiveness using **A/B testing** and **t-test**
- Visualize outcomes via an interactive **Gradio interface**

---

## 🧰 Technologies Used

- Python 3.10  
- pandas, numpy  
- scipy  
- gradio  
- streamlit *(optional UI alternative)*  
- seaborn / matplotlib *(for visualizations)*

---

## 🚀 Run Locally

```bash
git clone https://github.com/yourusername/rfm-ab-test.git
cd rfm-ab-test
pip install -r requirements.txt
python app/streamlit_app.py  # or gradio version if available
