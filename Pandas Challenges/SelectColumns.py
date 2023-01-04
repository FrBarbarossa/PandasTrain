# Task condition
import pandas as pd

df = pd.DataFrame({'name': ['Jeff', 'Esha', 'Jia'],
                   'age': [30, 56, 8]})


# Target:
# Now, you want to select just the name column from the DataFrame.
# Complete the function, name_column(df), by having it return only the name column.

def name_column(df):
    return df.name
