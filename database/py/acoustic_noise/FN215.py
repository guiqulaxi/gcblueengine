import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FN215'
    dbObj.xSpeed_kts=[0.000000,8.880000,31.080000,44.400002]
    dbObj.ySL_dB=[77.300003,82.219048,116.652397,126.490494]
    dbObj.speedMinNL_kts=8.960000
    dbObj.NL_min=43.660000
    dbObj.speedMaxNL_kts=44.400002
    dbObj.NL_max=80.699997
    dbObj.cavitationOffset_kts=12.800000
    dbObj.cavitationSlope_ktsperft=0.011860
    dbObj.cavitationSL_dB=144.490494
    dbObj.snorkelingSL_dB=138.490494
    dbObj.BuildSLTable()
    return dbObj