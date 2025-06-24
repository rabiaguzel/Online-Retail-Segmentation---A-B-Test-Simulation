import pandas as pd

df = pd.read_csv("data/Online_Retail.csv", encoding='latin1')
print(df.head())

df=df[df["Quantity"] >0]
df=df[df["UnitPrice"] >0]
df=df[df["CustomerID"] .notnull()]
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

df["InvoiceDate"]=pd.to_datetime(df["InvoiceDate"])
df["TotalPrice"]=df["Quantity"]*df["UnitPrice"]
df["CustomerID"]=df["CustomerID"].astype(int)

df.to_csv("data/cleaned_data.csv",index=False)

