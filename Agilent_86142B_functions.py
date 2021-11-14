# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 13:58:48 2021

@author: Bruger
"""
import time
import numpy as np











def getStart(OSA):
    A=OSA.write("sens:wav:star?")
    A=float(OSA.read("sens:wav:star?"))
    time.sleep(0.2)
    return A

def setStart(OSA,wavelength):

    OSA.write('sens:wav:star '+str(wavelength)+'nm') #Set start wavelength in nm
    time.sleep(0.2)
    print('Requested Start is '+str(wavelength)+'nm. Set Start to '+str(getCenter(OSA))+'nm')

def getCenter(OSA):
    A=OSA.write("sens:wav:cent?")
    time.sleep(0.2)
    A=float(OSA.read("sens:wav:cent?"))
    return A
    
def setCenter(OSA,wavelength):
    
    OSA.write('sens:wav:star '+str(wavelength)+'nm') #Set center wavelength in nm
    time.sleep(0.2)
    print('Requested Center is '+str(wavelength)+'nm. Set Center to '+str(getCenter(OSA))+'nm')
    
def getStop(OSA):
    A=OSA.write("sens:wav:stop?")
    A=float(OSA.read("sens:wav:stop?"))
    time.sleep(0.2)
    return A    
 
def setStop(OSA,wavelength):
    OSA.write('sens:wav:stop '+str(wavelength)+'nm') #Set stop wavelength in nm
    OSA.write('*WAI')
    print('Requested Stop is '+str(wavelength)+'nm. Set Stop to '+str(getStop(OSA))+'nm')

def getSpan(OSA):
    A=OSA.write("sens:wav:span?")
    A=float(OSA.read("sens:wav:span?"))
    time.sleep(0.2)
    return A

def setSpan(OSA,span):
    
    OSA.write('sens:wav:span '+str(span)+'nm')#Span in nm
    time.sleep(0.2)
    print('Requested Span is '+str(span)+'nm. Set Span to '+str(getSpan(OSA))+'nm')

def getRes(OSA):
    A=OSA.write('sens:band:res?')
    A=float(OSA.read('sens:band:res?') )*1e9 #Resolution in nm
    time.sleep(0.2)
    return A

def setRes(OSA,Res):
    OSA.write('sens:band:res '+str(Res)+'nm')#Resolution in nm
    OSA.write('*WAI')
    print('Requested Resolution is '+str(Res)+'nm. Set Resolution to '+str(getRes(OSA))+'nm')
    
def getLowScale(OSA):
    OSA.write('POW:RANG:LOW?')
    A=float(OSA.read('POW:RANG:LOW?'))
    time.sleep(0.2)
    return A
    
    
def setLowScale(OSA,val):
    
    OSA.write('POW:RANG:LOW '+str(val)+' DBM')
    time.sleep(0.2)
    print('Requested Low scale is '+str(val)+'dBm. Set Low Scale to '+str(getLowScale(OSA))+'dBm')

def getMaxScale(OSA):
    OSA.write('DISP:TRAC:Y:RLEV?')
    A=float(OSA.read('DISP:TRAC:Y:RLEV?'))   
    time.sleep(0.2)
    return A     
    
    
    
def setMaxScale(OSA,val):
    OSA.write('DISP:TRAC:Y:RLEV '+str(val)+' DBM')
    time.sleep(0.2)    
    print('Requested Max scale is '+str(val)+'dBm. Set Max Scale to '+str(getMaxScale(OSA))+'dBm')
    
    
    
    
    
def doReset(OSA):
    print('Resetting OSA to default state.')
    
    OSA.write('*RST')
    time.sleep(0.2)    
    
def doSweep(OSA):
    print('Running Single Sweep')
    OSA.write('INIT')
    time.sleep(0.2)
    
def getData(OSA):
    print('Getting data from OSA')
    OSA.write('form ascii')
    OSA.write('trac:data:y? tra')
    d=OSA.read('trac:data:y? tra')
    d=d.replace('\n','')
    d=d.split(',')
    d=np.array(d)
    power=d.astype(float)
    
    WL=np.linspace(getStart(OSA),getStop(OSA),len(power))
    return WL, power
    
    
    
    
    
    

    
    