# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='SwK200'
    dbObj.xSpeed_kts=[0.000000,5.132000,17.962000,25.660000]
    dbObj.ySL_dB=[80.150002,84.020683,111.115471,118.856842]
    dbObj.speedMinNL_kts=10.395000
    dbObj.NL_min=45.380001
    dbObj.speedMaxNL_kts=25.660000
    dbObj.NL_max=86.449997
    dbObj.cavitationOffset_kts=14.850000
    dbObj.cavitationSlope_ktsperft=0.014480
    dbObj.cavitationSL_dB=136.856842
    dbObj.snorkelingSL_dB=130.856842
    dbObj.BuildSLTable()
    return dbObj