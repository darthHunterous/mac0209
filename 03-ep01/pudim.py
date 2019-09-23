#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show() 

#%%
x, y, z = zip(*[tuple(line.split(sep=",", maxsplit=4)[:3]) for line in open("./data/mru.vitor.1.csv")][1:])
y

#%%
import ipywidgets as widgets

widgets.IntSlider(
    value=7,
    min=0,
    max=10,
    step=1,
    description='Test:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)