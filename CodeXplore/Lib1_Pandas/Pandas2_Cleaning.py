import pandas as pd

# The data set has following problems:
# some empty cells ("Date" in row 22, and "Calories" in row 18 and 28).
# wrong format ("Date" in row 26).
# wrong data ("Duration" in row 7).
# duplicates (row 11 and 12).

df = pd.read_csv('../data/data_cleaning.csv')
print(df.to_string())

# Remove empty cells: dropna() return a new Data Frame with no empty cells
new_df = df.dropna() # not change the original
# df.dropna(inplace = True) # change the original
print(new_df.to_string())

# Replace empty values: fillna() method allows us to replace empty cells with a value (Mean, Median, or Mode)
df.fillna(130, inplace = True) 
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True) # replace NULL values in column "Calories" with mean of it
