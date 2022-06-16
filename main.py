
#%% Import statements

import pandas as pd


#%% 1. Load Data --------------------------------------------------------------------------------------
 
# Read csv as a dataframe

path = 'Case_study_Crusher.csv'

df = pd.read_csv('Case_study_Crusher.csv', delimiter="\;", encoding = "utf-16", engine='python') # utf-8 does not work. "\;" and engine configuration to fix parser error.
df

#%% 2. Preprocessing ----------------------------------------------------------------------------------

# Remove unnecessary quotes (") from each cell

# Column names
df.columns = df.columns.str.replace('"', '')

# Cells
for i, col in enumerate(df.columns):
    df.iloc[:, i] = df.iloc[:, i].str.replace('"', '')
df

#%% Convert sensor data columns to float

numeric_cols = ['Z121_Rotation_speed_in_percent', 'H122_volumetric_flow_rate_in_m3_h']

# First replace ',' with '.' as the decimal, then, convert to float
for col in numeric_cols:
    df[col] = df[col].str.replace(',', '.').astype('float64')

df[numeric_cols]    


#%% Convert date strings to datetime to allow arithmetic operations

from datetime import datetime

dt_str = '09.05.2022 14:59:06'

dt_format = '%d.%m.%Y %H:%M:%S'

dt_obj = datetime.strptime(dt_str, dt_format)
print(dt_obj)

date_cols = ['Z121_Time', 'H122_Time']

for col in date_cols:
    df[col] = df[col].apply(lambda _: datetime.strptime(_,dt_format))
df[date_cols]


#%% 3. Analysis ---------------------------------------------------------------------------------------

# Check if Z121 and H122 times are the same

df[df.columns[0]].equals(df[df.columns[2]])


#%% Maintenance case
# The crusher is still operating but there is no waste
df[df.eval("Z121_Rotation_speed_in_percent != 0 & (H122_volumetric_flow_rate_in_m3_h == 0)")]

# %% Shift changes
# The crusher is not operating
