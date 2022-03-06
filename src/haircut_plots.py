# %%
import matplotlib.pyplot as plt
import pandas as pd

# %% [markdown]
# # Read the cleaned data

# %%
df = pd.read_excel("../haircut_cleanup.xlsx")
df.head()

# %% [markdown]
# Exploring the differences between married and unmarried customers

# %%
df.groupby("Married").mean()

# %%
df_no_time = df.drop(columns=["Time"])
df_no_time.groupby("Married").mean().plot.bar(stacked=True)

# %% [markdown]
# Exploring the mean tip amount differences for married and unmarried customers, binned by their age.

# %%
# Married and not married split
df_m = df.drop(df.loc[df["Married"] == "NM"].index)
df_nm = df.drop(df.loc[df["Married"] == "M"].index)

# Binned by age in 10 year intervals
bins = pd.cut(df["Age"], list(range(0, 100, 10)))

df_nm.groupby(bins)["Tip amount"].mean().plot.line()
df_m.groupby(bins)["Tip amount"].mean().plot.line()
plt.legend(["Not married", "Married"])

# %% [markdown]
# Exploring if culture has an impact on tip amounts

# %%
df_nm.groupby("Culture")["Tip amount"].mean().plot.bar()
df_m.groupby("Culture")["Tip amount"].mean().plot.bar(color="orange")
plt.legend(["Not married", "Married"])

# %% [markdown]
# Exploring if the time of day has an impact on tip amounts and the age of the customer

# %%
df.groupby("Time").mean().plot.line(stacked=True)
