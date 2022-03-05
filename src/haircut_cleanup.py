# %%
# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# %%
df = pd.read_excel("../haircut.xlsx", header=[2])
df.head()

# %%
df.drop(df.columns[6:], axis=1, inplace=True)
df.drop([114, 115], inplace=True)
df[110:120]

# %%
df["Married"].replace(to_replace="Kid", value="NM", inplace=True)
df["Day"].replace(to_replace="Tues", value="Tue", inplace=True)


def cap_first_letter(word):
    return word[0].upper() + word[1:].lower()


df["Day"] = df["Day"].apply(cap_first_letter)

df.loc[df["Day"] == "mon"]  # Should be empty

# %%
df["Time"] = df["Time"].apply(lambda x: x + 12 if 1 <= x <= 8 else x)
df[20:30]

# %%
df["Time"] = df["Time"].astype(int)
df["Age"] = df["Age"].astype(int)
df.head()

# %%
df.to_excel("../haircut_cleanup.xlsx")
