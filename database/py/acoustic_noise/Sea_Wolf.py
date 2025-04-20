import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Sea Wolf'
    dbObj.xSpeed_kts=[0.000000,10.500000,28.000000,35.000000]
    dbObj.ySL_dB=[82.000000,86.500000,94.000000,121.000000]
    dbObj.speedMinNL_kts=12.000000
    dbObj.NL_min=46.000000
    dbObj.speedMaxNL_kts=40.000000
    dbObj.NL_max=96.000000
    dbObj.cavitationOffset_kts=13.870000
    dbObj.cavitationSlope_ktsperft=0.032000
    dbObj.cavitationSL_dB=162.000000
    dbObj.snorkelingSL_dB=133.000000
    dbObj.BuildSLTable()
    return dbObj