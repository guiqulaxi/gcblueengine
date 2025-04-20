import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='CN205'
    dbObj.xSpeed_kts=[0.000000,7.130000,24.955000,35.650002]
    dbObj.ySL_dB=[84.050003,89.432053,127.106438,137.870544]
    dbObj.speedMinNL_kts=8.505000
    dbObj.NL_min=47.500000
    dbObj.speedMaxNL_kts=35.650002
    dbObj.NL_max=88.500000
    dbObj.cavitationOffset_kts=12.150000
    dbObj.cavitationSlope_ktsperft=0.006000
    dbObj.cavitationSL_dB=155.870544
    dbObj.snorkelingSL_dB=149.870544
    dbObj.BuildSLTable()
    return dbObj