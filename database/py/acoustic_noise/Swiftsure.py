import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Swiftsure'
    dbObj.xSpeed_kts=[0.000000,9.300000,24.799999,31.000000]
    dbObj.ySL_dB=[92.099998,101.519997,120.500000,138.500000]
    dbObj.speedMinNL_kts=8.000000
    dbObj.NL_min=50.500000
    dbObj.speedMaxNL_kts=32.000000
    dbObj.NL_max=100.500000
    dbObj.cavitationOffset_kts=12.350000
    dbObj.cavitationSlope_ktsperft=0.024000
    dbObj.cavitationSL_dB=165.899994
    dbObj.snorkelingSL_dB=150.500000
    dbObj.BuildSLTable()
    return dbObj