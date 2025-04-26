# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='JK185'
    dbObj.xSpeed_kts=[0.000000,4.912000,17.191999,24.559999]
    dbObj.ySL_dB=[84.400002,88.142754,114.342026,121.827530]
    dbObj.speedMinNL_kts=9.380000
    dbObj.NL_min=47.240002
    dbObj.speedMaxNL_kts=24.559999
    dbObj.NL_max=90.599998
    dbObj.cavitationOffset_kts=13.400000
    dbObj.cavitationSlope_ktsperft=0.011960
    dbObj.cavitationSL_dB=139.827530
    dbObj.snorkelingSL_dB=133.827530
    dbObj.BuildSLTable()
    return dbObj