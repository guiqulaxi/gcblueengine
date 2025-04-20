import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='VasterGotland'
    dbObj.xSpeed_kts=[0.000000,6.000000,16.000000,20.000000]
    dbObj.ySL_dB=[91.000000,99.550003,116.500000,125.599998]
    dbObj.speedMinNL_kts=11.000000
    dbObj.NL_min=46.000000
    dbObj.speedMaxNL_kts=20.000000
    dbObj.NL_max=96.000000
    dbObj.cavitationOffset_kts=12.220000
    dbObj.cavitationSlope_ktsperft=0.026000
    dbObj.cavitationSL_dB=162.199997
    dbObj.snorkelingSL_dB=134.500000
    dbObj.BuildSLTable()
    return dbObj