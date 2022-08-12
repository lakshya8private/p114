# Importing the modules that are necessary for this project
import numpy as np
import pandas as pd
import plotly.express as px

# Reading the CSV file
df = pd.read_csv("main.csv")
TOEFL_Score = df["TOEFL Score"].tolist()
Chances_of_admit = df["Chance of Admit "].tolist()

# Creating a Scatter Plot For TOEFL Score and Chances of Admit
fig = px.scatter(x=TOEFL_Score, y=Chances_of_admit)
fig.show()

# Using the predefined computer algorithm for getting the best fit line and values for slopes.
TOEFL_array = np.array(TOEFL_Score)
Chances_array = np.array(Chances_of_admit)

m, c = np.polyfit(TOEFL_array, Chances_array, 1)
y = []
for x in TOEFL_array:
    y_value = m*x + c
    y.append(y_value)

fig = px.scatter(x=TOEFL_array, y=Chances_array)
fig.update_layout(shapes=[
    dict(
        type='line',
        y0=min(y), y1=max(y),
        x0=min(TOEFL_array), x1=max(TOEFL_array)
    )
])

fig.show()

# Prediction Code
x = 250
y = m*x + c
print(f"Chances of Admiting {x} is {y}")
