import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Ship2'
    dbObj.xSpeed_kts=[0.000000,5.000000,10.000000,30.000000]
    dbObj.ySL_dB=[115.000000,115.000000,120.000000,137.000000]
    dbObj.speedMinNL_kts=5.000000
    dbObj.NL_min=75.000000
    dbObj.speedMaxNL_kts=30.000000
    dbObj.NL_max=100.000000
    dbObj.cavitationOffset_kts=99.000000
    dbObj.cavitationSlope_ktsperft=0.050000
    dbObj.cavitationSL_dB=100.000000
    dbObj.snorkelingSL_dB=100.000000
    dbObj.BuildSLTable()
    return dbObj