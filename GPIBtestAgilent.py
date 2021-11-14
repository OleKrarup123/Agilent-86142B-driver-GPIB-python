# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 12:01:13 2021

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


GPIBlist=pv.ResourceManager().list_resources() #Get list of all devices connected via GPIB (only 1)
print(GPIBlist)

GPIBname=GPIBlist[0]
print(GPIBname)


OSA=pv.ResourceManager().open_resource(GPIBname) 

#doReset(OSA)


setStart(OSA,1300)
setStop(OSA,1321.2)

print(getStart(OSA))
print(getStop(OSA))
print((getStop(OSA)-getStart(OSA)))
print(getSpan(OSA))


setLowScale(OSA,-50)
doSweep(OSA)


time.sleep(2)
setCenter(OSA,1313)
setSpan(OSA,6.2)
setRes(OSA,500/1000)
doSweep(OSA)

time.sleep(2)
setRes(OSA,60/1000)
doSweep(OSA)
WL,power=getData(OSA)

plt.figure()
plt.locator_params(axis='x',nbins=5)
plt.plot(WL*1e6,power)
plt.xlabel('Wavelength [um]')
plt.ylabel('Pow [dB]')
plt.show()


