import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("QueryResults.csv", names=['DATE', 'TAG', 'POSTS'], header=0)
df.DATE = pd.to_datetime(df.DATE)
reshaped_df = df.pivot(index="DATE", columns="TAG", values="POSTS")
reshaped_df.fillna(0, inplace=True)
nan_found = reshaped_df.isna().values.any()
plt.xlabel('YEARS', fontsize=14)
plt.ylabel('POSTS', fontsize=14)
plt.ylim(0, 35000)
roll_df = reshaped_df.rolling(window=12).mean()
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], label=roll_df[column].name, linewidth=3)

plt.legend(fontsize=8)
plt.show()
