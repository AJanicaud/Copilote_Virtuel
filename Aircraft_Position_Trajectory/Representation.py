# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 10:49:28 2018

@author: Esther
"""
import rasterio
from PIL import Image
import numpy as np
import pandas as pd
def Representation():
    data = rasterio.open('OACI_23_L93_E100.jp2')
    data.bounds
    
    fname='OACI_23_L93_E100.jp2'
    image=Image.open(fname)
    arr=np.asarray(image)
def Traj_file():
    traj_file='test.txt'
    
    with open(traj_file) as fh:
        traj = eval("".join(p.strip() for p in fh.readlines()))
        traj = pd.DataFrame.from_records(traj, columns=['latitude', 'longitude'])

    return traj.head()