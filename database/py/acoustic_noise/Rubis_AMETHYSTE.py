import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Rubis AMETHYSTE'
    dbObj.xSpeed_kts=[0.000000,8.100000,21.600000,27.000000]
    dbObj.ySL_dB=[88.599998,95.320000,108.000000,130.000000]
    dbObj.speedMinNL_kts=8.000000
    dbObj.NL_min=49.000000
    dbObj.speedMaxNL_kts=22.000000
    dbObj.NL_max=100.000000
    dbObj.cavitationOffset_kts=12.520000
    dbObj.cavitationSlope_ktsperft=0.021000
    dbObj.cavitationSL_dB=163.699997
    dbObj.snorkelingSL_dB=142.000000
    dbObj.BuildSLTable()
    return dbObj