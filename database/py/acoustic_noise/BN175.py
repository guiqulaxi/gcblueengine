# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BN175'
    dbObj.xSpeed_kts=[0.000000,7.080000,24.780001,35.400002]
    dbObj.ySL_dB=[89.800003,96.282433,141.659439,154.624298]
    dbObj.speedMinNL_kts=8.960000
    dbObj.NL_min=48.480000
    dbObj.speedMaxNL_kts=35.400002
    dbObj.NL_max=98.400002
    dbObj.cavitationOffset_kts=12.800000
    dbObj.cavitationSlope_ktsperft=0.009720
    dbObj.cavitationSL_dB=172.624298
    dbObj.snorkelingSL_dB=166.624298
    dbObj.BuildSLTable()
    return dbObj