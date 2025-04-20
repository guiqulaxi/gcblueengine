import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Pr 949'
    dbObj.xSpeed_kts=[0.000000,8.400000,22.400000,28.000000]
    dbObj.ySL_dB=[93.199997,103.639999,125.000000,142.000000]
    dbObj.speedMinNL_kts=4.000000
    dbObj.NL_min=52.000000
    dbObj.speedMaxNL_kts=32.000000
    dbObj.NL_max=102.000000
    dbObj.cavitationOffset_kts=11.000000
    dbObj.cavitationSlope_ktsperft=0.023000
    dbObj.cavitationSL_dB=166.899994
    dbObj.snorkelingSL_dB=154.000000
    dbObj.BuildSLTable()
    return dbObj