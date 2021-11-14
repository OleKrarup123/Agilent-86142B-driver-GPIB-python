# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 16:03:59 2021

@author: Bruger
"""
import pyvisa as pv #Library for sending GPIB commands via python
import time           
from Agilent_86142B_functions import *  #Custom library of functions for controlling the OSA
import numpy as np
import matplotlib.pyplot as plt
import warnings   
import pandas as pd
warnings.simplefilter("ignore", UserWarning) #Ignore spurious warnings 
from datetime import datetime

savename='OSA_spectrum_'        #Base name of saved spectrum
savepath='RecordedSpectra\\'    #Default save folder
saveformat='.csv' #.xls   .xlsx #Save data in various formats


GPIBname=pv.ResourceManager().list_resources()[0] #Get list of all devices connected via GPIB (only 1)
print(GPIBname)
OSA=pv.ResourceManager().open_resource(GPIBname) #Open connection to OSA

#doReset(OSA) #Resets OSA to default scan range. May take so long that connection times out


setStart(OSA,1300)      #Set scan Start in nm
setStop(OSA,1321.2)     #Set scan Stop in nm
setRes(OSA,0.06)        #Set Resolution in nm 
setMaxScale(OSA,15)  #Set Max Y-level in dBm
setLowScale(OSA,-50)    #Set Lowest Y-level in dBm. NOTE: Affects sweep rate 


time.sleep(2)

doSweep(OSA)            #Do sweep
WL,power=getData(OSA)   #Extract WL in m and power in dBm

plt.figure()
plt.locator_params(axis='x',nbins=5)
plt.plot(WL*1e6,power)
plt.xlabel('Wavelength [um]')
plt.ylabel('Pow [dBm]')
plt.show()



print('Save spectrum? Y/N')
x = input()
if x.upper()=='Y':
    
    savearray=np.array([WL,power]).T

    
    df = pd.DataFrame(savearray, columns=['WL', 'power'])
    now = datetime.now()
    now = now.strftime("%d-%m-%Y-%H-%M-%S")
    finalsavestring=savepath+savename+ now +saveformat
    df.to_csv(finalsavestring)
    print('Saved data in '+finalsavestring)

elif x.upper()=='N':
    print('Data not saved')