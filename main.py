
#%% Import statements

import pandas as pd


#%% Read csv as a dataframe

path = 'Case_study_Crusher.csv'

df = pd.read_csv('Case_study_Crusher.csv', delimiter="\;", encoding = "utf-16", engine='python', quoting=3) # utf-8 does not work. "\;" and engine configuration to fix parser error.
df

#%% Preprocessing

# Remove unnecessary quotes (") from each cell

# Column names
df.columns = df.columns.str.replace('"', '')

# Cells
for i, col in enumerate(df.columns):
    df.iloc[:, i] = df.iloc[:, i].str.replace('"', '')
df


#%% Check if Z121 and H122 times are the same
df[df.columns[0]].equals(df[df.columns[2]])





# %%
df.columns
# %%
