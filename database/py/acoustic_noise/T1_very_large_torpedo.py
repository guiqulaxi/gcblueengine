import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='T1:very large torpedo'
    dbObj.xSpeed_kts=[10.000000,20.000000,40.000000,80.000000]
    dbObj.ySL_dB=[106.000000,106.000000,122.000000,154.000000]
    dbObj.speedMinNL_kts=30.000000
    dbObj.NL_min=70.000000
    dbObj.speedMaxNL_kts=60.000000
    dbObj.NL_max=71.000000
    dbObj.cavitationOffset_kts=999.000000
    dbObj.cavitationSlope_ktsperft=999.000000
    dbObj.cavitationSL_dB=154.000000
    dbObj.snorkelingSL_dB=154.000000
    dbObj.BuildSLTable()
    return dbObj