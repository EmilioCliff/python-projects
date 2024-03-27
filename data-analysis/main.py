import pandas as pd
df = pd.read_csv("salaries_by_college_major.csv")
new_df = df.dropna()
# name_with_lowest = new_df['Undergraduate Major'].loc[new_df['Mid-Career Median Salary'].idxmax()]
# spread = new_df['Mid-Career 90th Percentile Salary'] - new_df['Mid-Career 10th Percentile Salary']
# new_df.insert(1, "Spread", spread)
# updated_df = new_df[['Undergraduate Major', 'Spread']].head()
# highest_potential = new_df.sort_values(by="Mid-Career 90th Percentile Salary", ascending=False)[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()
# highest_spread = new_df.sort_values(by='Spread', ascending=False)[['Undergraduate Major', 'Spread']].head()
# print(highest_potential)
# print(highest_spread)
group = new_df.groupby("Group")
print(group.count())
for group_name, group_data in group:
    print(f"Grouped {group_name} : {group_data}")
