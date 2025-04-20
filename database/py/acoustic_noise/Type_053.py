import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Type 053'
    dbObj.xSpeed_kts=[0.000000,4.500000,12.000000,15.000000]
    dbObj.ySL_dB=[95.900002,110.029999,140.000000,150.000000]
    dbObj.speedMinNL_kts=4.000000
    dbObj.NL_min=55.500000
    dbObj.speedMaxNL_kts=15.000000
    dbObj.NL_max=106.000000
    dbObj.cavitationOffset_kts=8.550000
    dbObj.cavitationSlope_ktsperft=0.020000
    dbObj.cavitationSL_dB=169.600006
    dbObj.snorkelingSL_dB=162.000000
    dbObj.BuildSLTable()
    return dbObj