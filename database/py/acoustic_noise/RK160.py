import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RK160'
    dbObj.xSpeed_kts=[0.000000,3.520000,12.320000,17.600000]
    dbObj.ySL_dB=[94.699997,99.371407,132.071243,141.414062]
    dbObj.speedMinNL_kts=6.545000
    dbObj.NL_min=50.700001
    dbObj.speedMaxNL_kts=17.600000
    dbObj.NL_max=94.199997
    dbObj.cavitationOffset_kts=9.350000
    dbObj.cavitationSlope_ktsperft=0.003975
    dbObj.cavitationSL_dB=159.414062
    dbObj.snorkelingSL_dB=153.414062
    dbObj.BuildSLTable()
    return dbObj