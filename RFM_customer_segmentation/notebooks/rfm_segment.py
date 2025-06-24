import pandas as pd
from segment_naming import segment

df = pd.read_csv("data/rfm_scores.csv")

df['Segment'] = df.apply(segment, axis=1)

df.to_csv("rfm_with_segments.csv", index=False)
