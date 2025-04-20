import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RK170'
    dbObj.xSpeed_kts=[0.000000,4.000000,14.000000,20.000000]
    dbObj.ySL_dB=[92.500000,97.392235,131.637894,141.422363]
    dbObj.speedMinNL_kts=7.175000
    dbObj.NL_min=49.700001
    dbObj.speedMaxNL_kts=20.000000
    dbObj.NL_max=90.199997
    dbObj.cavitationOffset_kts=10.250000
    dbObj.cavitationSlope_ktsperft=0.004625
    dbObj.cavitationSL_dB=159.422363
    dbObj.snorkelingSL_dB=153.422363
    dbObj.BuildSLTable()
    return dbObj