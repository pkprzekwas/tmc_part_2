import os
import numpy as np


import plotly.plotly as py
import plotly.graph_objs as go


from data_visualize import project_dir


data_dir = os.path.join(project_dir, '../out')
year_file = os.path.join(data_dir, 'years', 'avg', '201405-201505.csv')
data = np.genfromtxt(year_file, delimiter=',')
trace = go.Heatmap(z=np.flipud(data))
out = [trace]
py.plot(out, filename='sth')

