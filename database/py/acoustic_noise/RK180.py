import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RK180'
    dbObj.xSpeed_kts=[0.000000,4.480000,15.680000,22.400000]
    dbObj.ySL_dB=[90.300003,95.349724,130.697815,140.797272]
    dbObj.speedMinNL_kts=7.805000
    dbObj.NL_min=48.700001
    dbObj.speedMaxNL_kts=22.400000
    dbObj.NL_max=86.199997
    dbObj.cavitationOffset_kts=11.150000
    dbObj.cavitationSlope_ktsperft=0.005275
    dbObj.cavitationSL_dB=158.797272
    dbObj.snorkelingSL_dB=152.797272
    dbObj.BuildSLTable()
    return dbObj