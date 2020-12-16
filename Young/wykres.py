import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go
#Weight in N
x1 = np.array([0, 0.19262, 0.142245, 0.096138, 0.478728, 0.125568, 0.251136, 0.066708, 0.06867, 0.0981, 0.063765 ])
#Rubber extension in cm
y1 = np.array([0, 1.32, 0.88, 0.28, 3.68, 0.5, 1.62, 0.08, 0.02, 0.32, 0.04])

#delta l
ey=np.array([0.0721,
0.1196311,
0.1196311,
0.1196311,
0.1196311,
0.1349712,
0.0883299,
0.0883299,
0.0883299,
0.1196311,
0.0954151
])
#Convert cm to m
ey=ey/100
y1=y1/100

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
#coeficient is 1/k so we need to calculate (1/k)^-1 in order to get our result
print("Predicted k value: ", model.coef_**-1)
print("Predicted E value: ", model.coef_)

#Graph generation
fig = px.scatter(x=x1, y=y1, error_y=ey)
fig.add_traces(go.Scatter(x=x_range, y=y_range, name='Linear regression'))
fig.update_xaxes(showline=True, linewidth=2, linecolor='black', gridcolor='Grey', title_text='Weight')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black', gridcolor='Grey', title_text='delta l')
fig.show()
