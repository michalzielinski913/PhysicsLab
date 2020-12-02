import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go
x1 = np.array([7.4, 7.52, 8, 5.3, 4.86, 5.14, 25.84, 22.72, 46.08, 21.3])
y1 = np.array([2.28, 2.52, 2.62, 1.68, 1.56, 1.52, 8.12, 7.16, 14.62, 6.52])
ex = [0.10389,
0.10389,
0.0878,
0.0878,
0.06801,
0.06801,
0.06782,
0.10389,
0.10389,
0.12417,
]
ey=[0.10389,
0.10389,
0.10389,
0.10389,
0.06801,
0.10389,
0.10389,
0.11106,
0.10389,
0.10389,
]
#Converting x matrix in order to fit tensor
xr=np.array(x1).reshape((-1, 1))
yr=np.array(y1)
#Passing x and y values to linear regression sklearn ML model
# https://scikit-learn.org/stable/modules/linear_model.html
model = LinearRegression().fit(xr, yr)
#Generating 100 points in range <0, biggest measured x>
x_range = np.linspace(0, xr.max(), 100)
#Preditcting y values for 100 points given above
y_range = model.predict(x_range.reshape(-1, 1))
#coeficient is 1/Pi so we need to calculate (1/Pi)^-1 in order to get our result
print("Predicted Pi value: ", model.coef_**-1)

#Graph generation
fig = px.scatter(x=x1, y=y1, error_x=ex, error_y=ey)
fig.add_traces(go.Scatter(x=x_range, y=y_range, name='Linear regression'))
fig.update_xaxes(showline=True, linewidth=2, linecolor='black', gridcolor='Grey', title_text='Circumference')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black', gridcolor='Grey', title_text='Diameter')
fig.show()
