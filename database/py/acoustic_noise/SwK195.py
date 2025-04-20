import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='SwK195'
    dbObj.xSpeed_kts=[0.000000,4.920000,17.219999,24.600000]
    dbObj.ySL_dB=[81.500000,85.456062,113.148514,121.060638]
    dbObj.speedMinNL_kts=10.150000
    dbObj.NL_min=46.000000
    dbObj.speedMaxNL_kts=24.600000
    dbObj.NL_max=87.699997
    dbObj.cavitationOffset_kts=14.500000
    dbObj.cavitationSlope_ktsperft=0.013800
    dbObj.cavitationSL_dB=139.060638
    dbObj.snorkelingSL_dB=133.060638
    dbObj.BuildSLTable()
    return dbObj