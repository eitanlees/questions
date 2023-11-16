import random
import string
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

random.seed(0)

N = 100

start, end = datetime(2022, 1, 1), datetime(2023, 1, 1)

df = pd.DataFrame({
    'Date':[start + timedelta(seconds=random.randint(0, int((end - start).total_seconds()))) for _ in range(N)],
    'Name':[''.join(random.choices(string.ascii_uppercase, k=5)) for _ in range(N)],
    'Value': [random.random() for _ in range(N)]
})

# Sprinkle in some nan's for good measure
mask = np.random.randint(2, size=len(df))
df.loc[mask, 'Value'] = np.nan

df.to_csv('data.csv', index=False)