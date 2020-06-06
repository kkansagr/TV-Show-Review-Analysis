# -*- coding: utf-8 -*-

import pandas as pd
import itertools
from bokeh.layouts import row, widgetbox
from bokeh.models import Select
from bokeh.models import Div
from bokeh.io import show
from bokeh.application.handlers import FunctionHandler
from bokeh.application import Application
from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Select, Label
from bokeh.plotting import figure
from bokeh.io import show, output_file
from bokeh.models import FactorRange
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import *
from bokeh.layouts import column
from bokeh.models import CustomJS
from bokeh.plotting import Figure, output_file, show
from bokeh.io import curdoc
from bokeh.io import output_file, show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Dropdown
from bokeh.models.widgets import Panel, Tabs
from bokeh.plotting import figure
from bokeh.models import Legend, Label
from bokeh.models import FactorRange
from bokeh.plotting import figure

import pandas as pd

a = pd.read_csv('rtv.csv')
a["IMDB rating"] = (a["IMDB rating"]) * 10
a["RT audience score"] = (a["RT audience score"]).map(lambda x: x.strip('%'))
fruits = list(a)[1:]
counts = [int(a.iloc[0, 1]), int(a.iloc[0, 2]), int(a.iloc[0, 3])]
source = ColumnDataSource(data=dict(fruits=fruits, counts=counts, color=Spectral6[3:]))

p = figure(x_range=fruits, y_range=(0, 100), plot_height=450, plot_width=500, title="IMDB vs Rotten Tomatoes",
           toolbar_location=None, tools="")

p.vbar(x='fruits', top='counts', width=0.9, color='color', legend="fruits", source=source)

p.xgrid.grid_line_color = None
p.legend.orientation = "vertical"
tab1 = Panel(child=p, title="Overall")
p.legend.location = "top_center"

name = []
for i in range(len(list(a["TV show name"]))):
    name.append(a["TV show name"][i])
menu = Select(options=name,
              value='The Office', title='TV show name')


def change(i):
    import pandas as pd
    import numpy as np

    import os

    tvclouds = []
    for root, dirs, files in os.walk("Wordclouds"):
        for filename in files:
            tvclouds.append(filename)

    #tab1 analysis

    fruits = list(a)[1:]
    counts = [int(a.iloc[i, 1]), int(a.iloc[i, 2]), int(a.iloc[i, 3])]
    source = ColumnDataSource(data=dict(fruits=fruits, counts=counts, color=Spectral6[3:]))

    p = figure(x_range=fruits, y_range=(0, 100), plot_height=450, plot_width=500,
               title="IMDB vs Rotten Tomatoes ratings",
               toolbar_location=None, tools="")

    p.vbar(x='fruits', top='counts', width=0.9, color='color', legend="fruits", source=source)

    p.xgrid.grid_line_color = None
    p.legend.orientation = "vertical"
    tab1 = Panel(child=p, title="Overall")

    #tab 2 analysis

    excel = pd.read_csv('season.csv', header=None, usecols=[0, 1, 2, 3])

    df2 = excel.set_index(0, drop=True)
    df2[3] = (df2[3]) * 10
    df2[2] = (df2[2]).map(lambda x: str(x).strip('%'))


    df3 = df2.loc[a["TV show name"][i]:a["TV show name"][i]]
    sea = df3[1].map(lambda x: str(x)).tolist()
    imdbr = df3[2].tolist()

    fruits2 = sea
    counts2 = imdbr
    source2 = ColumnDataSource(data=dict(fruits=fruits2, counts=counts2))

    p2 = figure(x_range=fruits2, y_range=(0, 100), plot_height=450, plot_width=500, title="Season-wise ratings",
                toolbar_location=None, tools="")

    p2.vbar(x='fruits', top='counts', width=0.9, color='pink', legend="fruits", source=source2)

    p2.xgrid.grid_line_color = None
    p2.legend.orientation = "vertical"

    tab2 = Panel(child=p2, title="Season ratings")

    #tab3 analysis

    excel1 = pd.read_csv('season.csv', header=None)

    df21 = excel1.set_index(0, drop=True)

    df31 = df21.loc[a["TV show name"][i]:a["TV show name"][i]]
    sea1 = df31[1].tolist()
    sea1 = df31[1].map(lambda x: str(int(x))).tolist()

    import itertools
    epi = df21.loc[a["TV show name"][i]:a["TV show name"][i], 4:]

    epi = epi.dropna(thresh=1)

    seasonsize = len(epi[4])

    b = []
    epilen = []
    for o in range(0, seasonsize):
        incoms = list(epi.iloc[o])
        incoms = [incom for incom in incoms if str(incom) != 'nan']
        epilen.append(len(incoms))
        b.append(incoms)
    flat_list = [item for sublist in b for item in sublist]

    l = []
    d = []
    for s in range(0, len(epilen)):
        l.append([d for d in range(1, epilen[s] + 1)])
    # flat_list1 = [item for sublist in l for item in sublist]
    for f in range(0, len(sea1)):
        c = list(itertools.product(str(sea1[f]), l[f]))
        d.append(c)
    flat_list1 = [item for sublist in d for item in sublist]
    flat_list2 = []
    for y, j in flat_list1:
        flat_list2.append((y, str(j)))

    factors = flat_list2

    p3 = figure(x_range=FactorRange(*factors), plot_height=350, plot_width=800,
                toolbar_location=None, tools="",title="Episodic analysis")

    xy = flat_list
    p3.vbar(x=factors, top=xy, width=0.9, alpha=0.5)

    import pandas as pd
    import numpy as np

    p3.y_range.start = 0
    p3.x_range.range_padding = 0.1
    p3.xaxis.major_label_orientation = 1
    p3.xgrid.grid_line_color = None


    txt = figure(x_range=(0, 100), y_range=(0, 100), plot_width=400, plot_height=40, toolbar_location=None, tools="")
    mytext = Label(x=0, y=40, text='Here\'s what people are talking about the show')
    txt.axis.visible = False
    txt.add_layout(mytext)
    txt.xgrid.grid_line_color = None
    txt.ygrid.grid_line_color = None
    txt.outline_line_color = None


    tab3 = Panel(child=p3, title="Episodic analysis")
    tabs = Tabs(tabs=[tab1, tab2, tab3])

    posneg = pd.read_csv('twitterdata.csv', usecols=[0, 4, 5,6])
    all = posneg[np.isfinite(posneg['positive_percentage'])]
    positive = all.iloc[i][1]
    negative=all.iloc[i][2]
    pos = figure(x_range=(0, 100), y_range=(0, 100), plot_width=400, plot_height=40, toolbar_location=None, tools="")
    postext = Label(x=0, y=40, text='Percent of positive reviews: ' + str(positive))
    pos.axis.visible = False
    pos.add_layout(postext)
    pos.xgrid.grid_line_color = None
    pos.ygrid.grid_line_color = None
    pos.outline_line_color = None

    neg = figure(x_range=(0, 100), y_range=(0, 100), plot_width=400, plot_height=40, toolbar_location=None, tools="")
    negtext = Label(x=0, y=40, text='Percent of negative reviews: ' + str(negative))
    neg.axis.visible = False
    neg.add_layout(negtext)
    neg.xgrid.grid_line_color = None
    neg.ygrid.grid_line_color = None
    neg.outline_line_color = None

    k = figure(x_range=(0, 200), y_range=(0, 200), plot_width=350, plot_height=350, toolbar_location=None, tools="")
    k.image_url(url=[all.iloc[i][3]],
                x=1, y=1, w=200, h=200, anchor="bottom_left")
    k.axis.visible = False

    m=row(column(txt,k,pos,neg),tabs)
    return m


def callback(attr, old, new):
    a = pd.read_csv('rtv.csv')
    unique_index = pd.Index(list(a['TV show name']))
    for h in unique_index:
        if menu.value==h:
            layout.children[1]= change(unique_index.get_loc(h))

mm = menu.on_change('value', callback)
tab1 = Panel(child=p, title="Overall")

excel = pd.read_csv('season.csv', header=None, usecols=[0, 1, 2, 3])

df2 = excel.set_index(0, drop=True)
df2[3] = (df2[3]) * 10
df2[2] = (df2[2]).map(lambda x: str(x).strip('%'))

df3 = df2.loc["The Office":"The Office"]
sea = df3[1].tolist()
imdbr = df3[2].tolist()
sea = df3[1].map(lambda x: str(x)).tolist()

fruits2 = sea
counts2 = imdbr
source2 = ColumnDataSource(data=dict(fruits=fruits2, counts=counts2))

p2 = figure(x_range=fruits2, y_range=(0, 100), plot_height=450, plot_width=500, title="Season-wise ratings",
            toolbar_location=None, tools="")

p2.vbar(x='fruits', top='counts', width=0.9, color='pink', legend="fruits", source=source2)

p2.xgrid.grid_line_color = None
p2.legend.orientation = "vertical"

tab2 = Panel(child=p2, title="Season ratings")


k = figure(x_range=(0, 200), y_range=(0, 200), plot_width=350, plot_height=350, toolbar_location=None, tools="")
k.image_url(url=["https://i.ibb.co/Y3zKQBj/The-Office.png"],
            x=1, y=1, w=200, h=200, anchor="bottom_left")
k.axis.visible = False

txt = figure(x_range=(0, 100), y_range=(0, 100), plot_width=400, plot_height=40, toolbar_location=None, tools="")
mytext = Label(x=0, y=40, text='Here\'s what people are talking about the show')
txt.axis.visible = False
txt.add_layout(mytext)
txt.xgrid.grid_line_color = None
txt.ygrid.grid_line_color = None
txt.outline_line_color = None

import pandas
excel1 = pd.read_csv('season.csv', header=None)


df21 = excel1.set_index(0, drop = True)
df31=df21.loc["The Office":"The Office"]
sea1=df31[1].tolist()
sea1=df31[1].map(lambda x: str(int(x))).tolist()
import itertools
epi=df21.loc["The Office":"The Office",4:]

epi=epi.dropna(thresh=1)

seasonsize=len(epi[4])

b=[]
epilen=[]
for i in range(0,seasonsize):
    incoms=list(epi.iloc[i])
    incoms = [incom for incom in incoms if str(incom) != 'nan']
    epilen.append(len(incoms))
    b.append(incoms)
flat_list = [item for sublist in b for item in sublist]

l=[]
d=[]
for i in range(0,len(epilen)):
     l.append([i for i in range(1,epilen[i]+1)])
for i in range(0,len(sea1)):
    c = list(itertools.product(str(sea1[i]), l[i]))
    d.append(c)
flat_list1 = [item for sublist in d for item in sublist]
flat_list2=[]
for i,j in flat_list1:
    flat_list2.append((i,str(j)))

factors=flat_list2

p3 = figure(x_range=FactorRange(*factors), plot_height=350,plot_width=800,
                toolbar_location=None, tools="",title="Episodic analysis")

xy = flat_list
p3.vbar(x=factors, top=xy, width=0.9, alpha=0.5)


import pandas as pd
import numpy as np

p3.y_range.start = 0
p3.x_range.range_padding = 0.1
p3.xaxis.major_label_orientation = 1
p3.xgrid.grid_line_color = None


posneg = pd.read_csv('twitterdata.csv', usecols=[0, 4, 5])
all = posneg[np.isfinite(posneg['positive_percentage'])]
positive = all.iloc[0][1]
negative = all.iloc[0][2]
pos = figure(x_range=(0, 100), y_range=(0, 100), plot_width=400, plot_height=40, toolbar_location=None, tools="")
postext = Label(x=0, y=40, text='Percent of positive reviews: ' + str(positive))
pos.axis.visible = False
pos.add_layout(postext)
pos.xgrid.grid_line_color = None
pos.ygrid.grid_line_color = None
pos.outline_line_color = None

neg = figure(x_range=(0, 100), y_range=(0, 100), plot_width=400, plot_height=40, toolbar_location=None, tools="")
negtext = Label(x=0, y=40, text='Percent of negative reviews: ' + str(negative))
neg.axis.visible = False
neg.add_layout(negtext)
neg.xgrid.grid_line_color = None
neg.ygrid.grid_line_color = None
neg.outline_line_color = None


tab3 = Panel(child=p3, title="Episodic analysis")


tabs = Tabs(tabs=[tab1, tab2, tab3])
m=row(column(txt,k,pos,neg),tabs)

layout = column(menu, m)


curdoc().add_root(layout)

