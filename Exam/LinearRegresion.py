
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go

class LinearRegresion:

    def __init__(self):
        self.x1=np.array([])
        self.y1=np.array([])
        self.ex=np.array([])
        self.ey=np.array([])
        self.model = None

    def appendX(self, *args):
        for x in args:
            self.x1=np.append(self.x1, x)

    def appendY(self, *args):
        for x in args:
            self.y1=np.append(self.y1, x)

    def appendEX(self, *args):
        for x in args:
            self.ex=np.append(self.ex, x)

    def appendEY(self, *args):
        for x in args:
            self.ey=np.append(self.ey, x)

    def isOk(self):
        if(self.x1.size == self.y1.size):
            return True
        return False

    def generateModel(self, b=False):
        self.xr = np.array(self.x1).reshape((-1, 1))
        self.yr = np.array(self.y1)
        self.model = LinearRegression(fit_intercept=b).fit(self.xr, self.yr)


    def defaultPlot(self):
        if(self.x1.size != self.ex.size):
            self.ex=np.zeros(self.x1.size)

        if(self.y1.size != self.ey.size):
            self.ey=np.zeros(self.y1.size)

        fig = px.scatter(x=self.x1, y=self.y1, error_x=self.ex, error_y=self.ey)
        # fig.update_xaxes(showline=True, linewidth=2, linecolor='black', gridcolor='Grey', title_text='Circumference')
        fig.update_xaxes(showline=True, linewidth=2, linecolor='black', gridcolor='Grey')
        fig.update_yaxes(showline=True, linewidth=2, linecolor='black', gridcolor='Grey')
        fig.show()

    def linearPlot(self):
        x_range = np.linspace(0, self.xr.max(), 100)
        # Preditcting y values for 100 points given above
        y_range = self.model.predict(x_range.reshape(-1, 1))
        if (self.x1.size != self.ex.size):
            self.ex = np.zeros(self.x1.size)

        if (self.y1.size != self.ey.size):
            self.ey = np.zeros(self.y1.size)

        fig = px.scatter(x=self.x1, y=self.y1, error_x=self.ex, error_y=self.ey)
        fig.add_traces(go.Scatter(x=x_range, y=y_range, name='Linear regression'))
        # fig.update_xaxes(showline=True, linewidth=2, linecolor='black', gridcolor='Grey', title_text='Circumference')
        fig.update_xaxes(showline=True, linewidth=2, linecolor='black', gridcolor='Grey')
        fig.update_yaxes(showline=True, linewidth=2, linecolor='black', gridcolor='Grey')

        fig.show()

    def getM(self):
        return self.model.coef_