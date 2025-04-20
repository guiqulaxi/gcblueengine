import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='S004.Merchant Very Large'
    dbObj.xSpeed_kts=[2.000000,6.000000,12.000000,24.000000]
    dbObj.ySL_dB=[111.000000,120.400002,140.600006,150.000000]
    dbObj.speedMinNL_kts=0.000000
    dbObj.NL_min=60.000000
    dbObj.speedMaxNL_kts=36.000000
    dbObj.NL_max=100.000000
    dbObj.cavitationOffset_kts=100.000000
    dbObj.cavitationSlope_ktsperft=0.000000
    dbObj.cavitationSL_dB=0.000000
    dbObj.snorkelingSL_dB=0.000000
    dbObj.BuildSLTable()
    return dbObj