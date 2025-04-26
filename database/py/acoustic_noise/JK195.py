# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='JK195'
    dbObj.xSpeed_kts=[0.000000,5.340000,18.690001,26.700001]
    dbObj.ySL_dB=[81.500000,85.095253,110.262047,117.452560]
    dbObj.speedMinNL_kts=9.800000
    dbObj.NL_min=46.000000
    dbObj.speedMaxNL_kts=26.700001
    dbObj.NL_max=88.199997
    dbObj.cavitationOffset_kts=14.000000
    dbObj.cavitationSlope_ktsperft=0.013200
    dbObj.cavitationSL_dB=135.452560
    dbObj.snorkelingSL_dB=129.452560
    dbObj.BuildSLTable()
    return dbObj