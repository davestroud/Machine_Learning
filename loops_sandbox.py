import pandas as pd

# Create a sample dataframe with missing values
data = {'A': [1, 2, 3, 4, None],
        'B': [None, 6, 7, 8, 9]}
df = pd.DataFrame(data)

# Define two lists to fill in the missing values
fill_A = [5, 10, 15, 20, 25]
fill_B = [100, 200, 300, 400, 500]

# Use nested for loops to fill in the missing values
for i, row in df.iterrows():
    for col in df.columns:
        if pd.isnull(row[col]):
            if col == 'A':
                df.at[i, col] = fill_A[i]
            elif col == 'B':
                df.at[i, col] = fill_B[i]

# Print the filled dataframe
print(df)
