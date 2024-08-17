import pandas as pd
# Series ~ Column
calories = {"day1": 420, "day2": 380, "day3": 390}
mySeries = pd.Series(calories)
print(mySeries)
print(type(mySeries))
# DataFrame ~ Table
## Load a dictionary into a DataFrame:
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(type(df))
## Load a CSV file into a DataFrame:
df = pd.read_csv('../data/data.csv')

# loc: return rows
print(df) 
print(df.loc[0]) # return Series
print(df.loc[[0, 1]]) # return DataFrame (row 0, row 1)
print(df.to_string()) # return entire DataFrame
print(df.head(10)) # return the first 10 rows, default: 5
print(df.tail(10)) # return the last 10 rows, default: 5
print(df.info()) 

print(pd.options.display.max_rows)