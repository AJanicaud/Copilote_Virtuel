#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:12:15 2019

@author: alixjanicaud
"""

import rasterio
data = rasterio.open("OACI_23_L93_E100.jp2")

# Les coordonnées des quatre coins de la carte en Lambert 93
# (L93 dans le nom de fichier => projection Lambert93)
# https://epsg.io/2154
print(data.bounds)

from PIL import Image
import numpy as np
import time



tmps1=time.clock()

# Chargement du fond de carte, c'est un peu long
fname = 'OACI_23_L93_E100.jp2'
image = Image.open(fname)
arr = np.asarray(image)
tmps2=time.clock()

print(tmps2-tmps1)


import pandas as pd

# la trajectoire
traj_file = 'Trajectoire Lasbordes-Montauban.txt'
with open(traj_file) as fh:
    traj = eval("".join(p.strip() for p in fh.readlines()))
    traj = pd.DataFrame.from_records(traj, columns=['latitude', 'longitude'])

print(traj.head())



from traffic.core import Flight
from datetime import datetime

# on peut écrire Flight(traj) et le plot fonctionnerait
# mais la bibliothèque est contente
# si on a une colonne altitude et une colonne timestamp
now = datetime.now()
f = Flight(traj.assign(altitude=0, timestamp=now))

print(f)


#%matplotlib inline
import matplotlib.pyplot as plt

from traffic.drawing import Lambert93, rivers, location
from traffic.data import airac, airports

with plt.style.context('traffic'):
    fig, ax = plt.subplots(figsize=(15, 15), subplot_kw=dict(projection=Lambert93()))

    ax.imshow(  # fond de carte
        arr[::-1],
        extent=(
            data.bounds.left, data.bounds.right,
            data.bounds.bottom, data.bounds.top),
        alpha=.3  # transparence
    )
    
    ax.add_feature(rivers())
    # essayez différents extent
    ax.set_extent((1, 2, 43.5, 44))
    ax.set_extent(f.extent())

    # essayez différents paramètres, linestyle='dashed', linewidth=3 par exemple
    rep = f.plot(ax, color='red')
    
    location("Toulouse").plot(ax, linestyle='dashed')
    location("Montauban").plot(ax, linestyle='dashed')
    
    airports['LFBO'].plot(ax)
    
    f.at().plot(ax, marker='^')#, text_kw=dict(s='coucou'))
    f.assign(groundspeed=50, vertical_rate=0, track=90).comet(minutes=10).plot(ax, linestyle='dashed')
    
    #fig.savefig("example.pdf")

