#%%
import pandas as pd

# %%
# Load the original CSV file
original_csv_file = 'unicorn_startup_companies_cleaned.csv'
df = pd.read_csv(original_csv_file)

# %%
# Remove '$' symbol from the "Valuation ($B)" column and convert it to numeric
df['Valuation ($B)'] = df['Valuation ($B)'].str.replace('$', '').astype(float)

# %%
# Name the numbering column as "ID" (you can use any name you prefer)
df = df.rename(columns={df.columns[0]: 'ID'})

# Save the dataset with the updated column name
df.to_csv(original_csv_file, index=False)
# %%
# Load the mapping from a CSV file
country_to_continent_df = pd.read_csv('Countries_Continents.csv')

# Merge the mapping with the main DataFrame based on the 'Country' column
df = df.merge(country_to_continent_df, on='Country', how='left')

#%%
df[df.isna().any(axis=1)]
#%%
df['Country'] = df['Country'].replace('United States', 'United States of America')

#%%
df
# %%
# Save the cleaned data to a new CSV file
cleaned_csv_file = 'unicorn_startup_companies_cleaned.csv'
df.to_csv(cleaned_csv_file, index=False)

print(f"Cleaned data saved to {cleaned_csv_file}")
# %%
