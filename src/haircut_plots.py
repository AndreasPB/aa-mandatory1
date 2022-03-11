# %%
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

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
df_no_time.groupby("Married").mean().plot.bar()

# %% [markdown]
# Exploring the mean tip amount differences for married and unmarried customers, binned by their age.

# %%
# Married and not married split
df_m = df.drop(df.loc[df["Married"] == "NM"].index)
df_nm = df.drop(df.loc[df["Married"] == "M"].index)

# Binned by age in 10 year intervals
bins = pd.cut(df["Age"], list(range(0, 100, 10)))

df_nm.groupby(bins)["Tip amount"].mean().plot(linestyle="dotted")
df_m.groupby(bins)["Tip amount"].mean().plot.line().set_ylabel("Tipping amount")
plt.legend(["Not married", "Married"])
plt.savefig("tip_amount_by_age.pdf")

# %% [markdown]
# Exploring if culture has an impact on tip amounts

# %%
# If dividing into colours, remember the you cannot use everyother coloumn(missing values)
df.groupby(["Culture", "Married"])["Tip amount"].mean().plot.bar().set_ylabel(
    "Tipping amount"
)

plt.savefig("culture_impact.pdf", bbox_inches="tight")

# %% [markdown]
# Exploring if the time of day has an impact on tip amounts and the age of the customer

# %%
df.groupby("Time")["Age"].mean().plot(linestyle="dotted").set_ylabel(
    "Age", color="orange"
)
df.groupby("Time")["Tip amount"].mean().plot.line(secondary_y=True).set_ylabel(
    "Tip amount", color="#1f77b4"
)
age_line = mlines.Line2D([], [], color="orange")
tip_amount_line = mlines.Line2D([], [], linestyle="dotted", color="#1f77b4")
plt.legend([age_line, tip_amount_line], ["Age", "Tip amount"], loc=[0.1, 0.8])
plt.savefig("time_of_day_and_age.pdf")
