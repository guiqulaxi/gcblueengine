# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AK215'
    dbObj.xSpeed_kts=[0.000000,5.796000,20.285999,28.980000]
    dbObj.ySL_dB=[75.940002,79.596031,105.188232,112.500290]
    dbObj.speedMinNL_kts=11.620000
    dbObj.NL_min=43.799999
    dbObj.speedMaxNL_kts=28.980000
    dbObj.NL_max=83.400002
    dbObj.cavitationOffset_kts=16.600000
    dbObj.cavitationSlope_ktsperft=0.013700
    dbObj.cavitationSL_dB=130.500290
    dbObj.snorkelingSL_dB=124.500290
    dbObj.BuildSLTable()
    return dbObj