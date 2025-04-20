import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Pr 877V'
    dbObj.xSpeed_kts=[0.000000,5.100000,13.600000,17.000000]
    dbObj.ySL_dB=[90.699997,98.889999,115.000000,120.500000]
    dbObj.speedMinNL_kts=8.000000
    dbObj.NL_min=48.500000
    dbObj.speedMaxNL_kts=20.000000
    dbObj.NL_max=98.500000
    dbObj.cavitationOffset_kts=13.930000
    dbObj.cavitationSlope_ktsperft=0.030000
    dbObj.cavitationSL_dB=161.899994
    dbObj.snorkelingSL_dB=132.500000
    dbObj.BuildSLTable()
    return dbObj