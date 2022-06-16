
#%% 1. Load Data --------------------------------------------------------------------------------------
 
import pandas as pd

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

date_cols = ['Z121_Time', 'H122_Time']
dt_format = '%d.%m.%Y %H:%M:%S'

for col in date_cols:
    df[col] = df[col].apply(lambda _: datetime.strptime(_,dt_format))
df[date_cols]


#%% 3. Visualization

from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Use a smaller partition of the data
df2 = df[0:10000]

fig = make_subplots(rows=2, cols=1)

fig.append_trace(go.Scatter(
    x=df2['Z121_Time'], 
    y=df2['Z121_Rotation_speed_in_percent'],
    name='Z121'
), row=1, col=1)

fig.append_trace(go.Scatter(
    x=df2['H122_Time'], 
    y=df2['H122_volumetric_flow_rate_in_m3_h'],
    name='H122'
), row=2, col=1)

fig.update_yaxes(title_text="Z121_Rotation_speed", row=1, col=1)
fig.update_yaxes(title_text="H122_volumetric_flow_rate", row=2, col=1)


fig.update_layout(height=600, width=600)
fig.show()


#%% 4. Analysis ---------------------------------------------------------------------------------------

# Check if Z121 and H122 times are the same

df[df.columns[0]].equals(df[df.columns[2]])


#%% Maintenance case
# The crusher is still operating but there is no waste
df[df.eval("Z121_Rotation_speed_in_percent != 0 & (H122_volumetric_flow_rate_in_m3_h == 0)")]

# %% Shift changes
# The crusher is not operating
