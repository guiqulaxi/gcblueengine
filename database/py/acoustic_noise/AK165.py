# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AK165'
    dbObj.xSpeed_kts=[0.000000,3.656000,12.796000,18.280001]
    dbObj.ySL_dB=[88.839996,93.121628,123.093018,131.656281]
    dbObj.speedMinNL_kts=8.820000
    dbObj.NL_min=49.799999
    dbObj.speedMaxNL_kts=18.280001
    dbObj.NL_max=95.400002
    dbObj.cavitationOffset_kts=12.600000
    dbObj.cavitationSlope_ktsperft=0.008200
    dbObj.cavitationSL_dB=149.656281
    dbObj.snorkelingSL_dB=143.656281
    dbObj.BuildSLTable()
    return dbObj