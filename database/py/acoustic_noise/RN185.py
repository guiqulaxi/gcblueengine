# -*- coding: utf-8 -*-
import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RN185'
    dbObj.xSpeed_kts=[0.000000,7.440000,26.040001,37.200001]
    dbObj.ySL_dB=[89.599998,95.202789,134.422318,145.627899]
    dbObj.speedMinNL_kts=8.120000
    dbObj.NL_min=48.200001
    dbObj.speedMaxNL_kts=37.200001
    dbObj.NL_max=96.199997
    dbObj.cavitationOffset_kts=11.600000
    dbObj.cavitationSlope_ktsperft=0.006575
    dbObj.cavitationSL_dB=163.627899
    dbObj.snorkelingSL_dB=157.627899
    dbObj.BuildSLTable()
    return dbObj