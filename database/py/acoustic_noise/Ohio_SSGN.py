import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Ohio SSGN'
    dbObj.xSpeed_kts=[0.000000,8.400000,22.400000,28.000000]
    dbObj.ySL_dB=[75.300003,79.709999,87.000000,105.000000]
    dbObj.speedMinNL_kts=8.000000
    dbObj.NL_min=49.500000
    dbObj.speedMaxNL_kts=28.000000
    dbObj.NL_max=99.500000
    dbObj.cavitationOffset_kts=12.700000
    dbObj.cavitationSlope_ktsperft=0.028000
    dbObj.cavitationSL_dB=161.300003
    dbObj.snorkelingSL_dB=117.000000
    dbObj.BuildSLTable()
    return dbObj