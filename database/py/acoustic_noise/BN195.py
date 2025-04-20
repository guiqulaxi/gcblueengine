import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BN195'
    dbObj.xSpeed_kts=[0.000000,8.120000,28.420000,40.599998]
    dbObj.ySL_dB=[83.000000,88.234108,124.872841,135.341049]
    dbObj.speedMinNL_kts=9.800000
    dbObj.NL_min=46.000000
    dbObj.speedMaxNL_kts=40.599998
    dbObj.NL_max=89.199997
    dbObj.cavitationOffset_kts=14.000000
    dbObj.cavitationSlope_ktsperft=0.012200
    dbObj.cavitationSL_dB=153.341049
    dbObj.snorkelingSL_dB=147.341049
    dbObj.BuildSLTable()
    return dbObj