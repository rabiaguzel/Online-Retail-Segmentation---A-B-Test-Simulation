import pandas as pd

df=pd.read_csv("data/cleaned_data.csv")
df["InvoiceDate"]=pd.to_datetime(df["InvoiceDate"])

today_date=df["InvoiceDate"].max()+pd.Timedelta(days=1)

rfm=df.groupby("CustomerID").agg({
    "InvoiceDate": lambda x: (today_date - x.max()).days,
    "InvoiceNo": "nunique",
    "TotalPrice": "sum"
})

rfm.columns=["Recency", "Frequency", "Monetary"]
rfm=rfm[rfm["Monetary"]>0]

rfm = rfm.dropna(subset=["Recency"])
print(rfm["Frequency"].isna().sum())
print(rfm["Frequency"].describe())
print(rfm.head())


rfm["R_score"] = pd.qcut(rfm["Recency"], 5, labels=[5,4,3,2,1], duplicates='drop')
rfm["F_score"]=pd.qcut(rfm["Frequency"].rank(method="first"), 5, labels=[1,2,3,4,5])
rfm["M_score"]=pd.qcut(rfm["Monetary"], 5, labels=[1,2,3,4,5])

rfm["RFM_Score"]= rfm["R_score"].astype(str) + rfm["F_score"].astype(str) + rfm["M_score"].astype(str)

rfm.to_csv("data/rfm_scores.csv")

