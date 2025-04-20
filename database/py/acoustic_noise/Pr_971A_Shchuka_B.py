import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Pr 971A Shchuka-B'
    dbObj.xSpeed_kts=[0.000000,10.500000,28.000000,35.000000]
    dbObj.ySL_dB=[88.900002,95.830002,109.000000,128.000000]
    dbObj.speedMinNL_kts=9.000000
    dbObj.NL_min=49.000000
    dbObj.speedMaxNL_kts=36.000000
    dbObj.NL_max=99.000000
    dbObj.cavitationOffset_kts=13.050000
    dbObj.cavitationSlope_ktsperft=0.026000
    dbObj.cavitationSL_dB=163.300003
    dbObj.snorkelingSL_dB=140.000000
    dbObj.BuildSLTable()
    return dbObj