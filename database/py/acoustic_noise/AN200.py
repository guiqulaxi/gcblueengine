import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AN200'
    dbObj.xSpeed_kts=[0.000000,8.160000,28.559999,40.799999]
    dbObj.ySL_dB=[81.300003,86.191559,120.432495,130.215622]
    dbObj.speedMinNL_kts=10.780000
    dbObj.NL_min=45.599998
    dbObj.speedMaxNL_kts=40.799999
    dbObj.NL_max=88.000000
    dbObj.cavitationOffset_kts=15.400000
    dbObj.cavitationSlope_ktsperft=0.012050
    dbObj.cavitationSL_dB=148.215622
    dbObj.snorkelingSL_dB=142.215622
    dbObj.BuildSLTable()
    return dbObj