import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RK195'
    dbObj.xSpeed_kts=[0.000000,5.200000,18.200001,26.000000]
    dbObj.ySL_dB=[87.000000,90.277191,113.217560,119.771942]
    dbObj.speedMinNL_kts=8.750000
    dbObj.NL_min=47.200001
    dbObj.speedMaxNL_kts=26.000000
    dbObj.NL_max=80.199997
    dbObj.cavitationOffset_kts=12.500000
    dbObj.cavitationSlope_ktsperft=0.009175
    dbObj.cavitationSL_dB=137.771942
    dbObj.snorkelingSL_dB=131.771942
    dbObj.BuildSLTable()
    return dbObj