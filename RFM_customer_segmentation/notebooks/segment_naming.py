import pandas as pd

rfm=pd.read_csv("data/rfm_scores.csv",index_col="CustomerID")

def segment(row):
    rfm_str=str(rfm["RFM_Score"])
    if rfm_str=="555":
        return "Champion"
    elif row["R_score"]== 5:
        return "Recent Customer"
    elif row["F_score"]== 5:
        return "Loyal Customer"
    elif row["R_score"]== 1:
        return "At Risk"
    else:
        return "Others"

rfm["Segment"]= rfm.apply(segment, axis=1)

rfm.to_csv("model/rfm_segment_labels.csv")