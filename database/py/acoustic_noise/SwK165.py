import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='SwK165'
    dbObj.xSpeed_kts=[0.000000,3.648000,12.768000,18.240000]
    dbObj.ySL_dB=[89.599998,93.906616,124.052917,132.666153]
    dbObj.speedMinNL_kts=8.680000
    dbObj.NL_min=49.720001
    dbObj.speedMaxNL_kts=18.240000
    dbObj.NL_max=95.199997
    dbObj.cavitationOffset_kts=12.400000
    dbObj.cavitationSlope_ktsperft=0.009720
    dbObj.cavitationSL_dB=150.666153
    dbObj.snorkelingSL_dB=144.666153
    dbObj.BuildSLTable()
    return dbObj