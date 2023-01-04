# Task condition
import pandas as pd

df = pd.DataFrame({'name': ['Jeff', 'Esha', 'Jia'],
                   'age': [30, 56, 8]},
                  index=[132, 156, 27])


# Target:
# Complete the function, select_Jia_row(df), by having it return the row with Jia in it.
# This should involve hard-coding the index value associated with Jia.


def name_column(df):
    return df.loc[27]

print(name_column(df))
