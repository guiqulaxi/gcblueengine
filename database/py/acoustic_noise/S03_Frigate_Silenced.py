# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='S03.Frigate Silenced'
    dbObj.xSpeed_kts=[6.000000,10.000000,20.000000,40.000000]
    dbObj.ySL_dB=[103.000000,106.959999,118.839996,122.800003]
    dbObj.speedMinNL_kts=0.000000
    dbObj.NL_min=52.000000
    dbObj.speedMaxNL_kts=40.000000
    dbObj.NL_max=92.000000
    dbObj.cavitationOffset_kts=100.000000
    dbObj.cavitationSlope_ktsperft=0.000000
    dbObj.cavitationSL_dB=0.000000
    dbObj.snorkelingSL_dB=0.000000
    dbObj.BuildSLTable()
    return dbObj