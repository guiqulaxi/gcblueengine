import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FN205'
    dbObj.xSpeed_kts=[0.000000,8.400000,29.400000,42.000000]
    dbObj.ySL_dB=[80.900002,86.338310,124.406487,135.283112]
    dbObj.speedMinNL_kts=8.680000
    dbObj.NL_min=44.880001
    dbObj.speedMaxNL_kts=42.000000
    dbObj.NL_max=85.199997
    dbObj.cavitationOffset_kts=12.400000
    dbObj.cavitationSlope_ktsperft=0.010880
    dbObj.cavitationSL_dB=153.283112
    dbObj.snorkelingSL_dB=147.283112
    dbObj.BuildSLTable()
    return dbObj