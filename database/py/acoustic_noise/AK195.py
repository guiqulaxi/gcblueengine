# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AK195'
    dbObj.xSpeed_kts=[0.000000,4.940000,17.290001,24.700001]
    dbObj.ySL_dB=[81.099998,85.091141,113.029106,121.011383]
    dbObj.speedMinNL_kts=10.500000
    dbObj.NL_min=46.200001
    dbObj.speedMaxNL_kts=24.700001
    dbObj.NL_max=88.199997
    dbObj.cavitationOffset_kts=15.000000
    dbObj.cavitationSlope_ktsperft=0.011500
    dbObj.cavitationSL_dB=139.011383
    dbObj.snorkelingSL_dB=133.011383
    dbObj.BuildSLTable()
    return dbObj