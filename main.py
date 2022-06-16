
#%% Import statements

import pandas as pd


#%% Read csv as a dataframe

path = 'Case_study_Crusher.csv'

df = pd.read_csv('Case_study_Crusher.csv', delimiter="\;", encoding = "utf-16", engine='python') # utf-8 does not work. "\;" and engine configuration to fix parser error.
df

#%%





# %%
