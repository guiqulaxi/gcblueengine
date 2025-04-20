import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='CK180'
    dbObj.xSpeed_kts=[0.000000,4.260000,14.910000,21.299999]
    dbObj.ySL_dB=[92.260002,97.868233,137.125885,148.342346]
    dbObj.speedMinNL_kts=6.930000
    dbObj.NL_min=50.000000
    dbObj.speedMaxNL_kts=21.299999
    dbObj.NL_max=98.500000
    dbObj.cavitationOffset_kts=9.900000
    dbObj.cavitationSlope_ktsperft=0.005000
    dbObj.cavitationSL_dB=166.342346
    dbObj.snorkelingSL_dB=160.342346
    dbObj.BuildSLTable()
    return dbObj