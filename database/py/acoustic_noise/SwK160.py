import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='SwK160'
    dbObj.xSpeed_kts=[0.000000,3.436000,12.026000,17.180000]
    dbObj.ySL_dB=[90.949997,95.274460,125.545654,134.194565]
    dbObj.speedMinNL_kts=8.435000
    dbObj.NL_min=50.340000
    dbObj.speedMaxNL_kts=17.180000
    dbObj.NL_max=96.449997
    dbObj.cavitationOffset_kts=12.050000
    dbObj.cavitationSlope_ktsperft=0.009040
    dbObj.cavitationSL_dB=152.194565
    dbObj.snorkelingSL_dB=146.194565
    dbObj.BuildSLTable()
    return dbObj