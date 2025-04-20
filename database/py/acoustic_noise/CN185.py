import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='CN185'
    dbObj.xSpeed_kts=[0.000000,6.210000,21.735001,31.049999]
    dbObj.ySL_dB=[91.449997,97.745911,141.817276,154.409088]
    dbObj.speedMinNL_kts=7.245000
    dbObj.NL_min=49.500000
    dbObj.speedMaxNL_kts=31.049999
    dbObj.NL_max=96.500000
    dbObj.cavitationOffset_kts=10.350000
    dbObj.cavitationSlope_ktsperft=0.005500
    dbObj.cavitationSL_dB=172.409088
    dbObj.snorkelingSL_dB=166.409088
    dbObj.BuildSLTable()
    return dbObj