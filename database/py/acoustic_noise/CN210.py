import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='CN210'
    dbObj.xSpeed_kts=[0.000000,7.360000,25.760000,36.799999]
    dbObj.ySL_dB=[82.199997,87.352776,123.422218,133.727768]
    dbObj.speedMinNL_kts=8.820000
    dbObj.NL_min=47.000000
    dbObj.speedMaxNL_kts=36.799999
    dbObj.NL_max=86.500000
    dbObj.cavitationOffset_kts=12.600000
    dbObj.cavitationSlope_ktsperft=0.006000
    dbObj.cavitationSL_dB=151.727768
    dbObj.snorkelingSL_dB=145.727768
    dbObj.BuildSLTable()
    return dbObj