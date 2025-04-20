import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='GK145'
    dbObj.xSpeed_kts=[0.000000,3.200000,11.200000,16.000000]
    dbObj.ySL_dB=[90.000000,94.000000,122.000000,130.000000]
    dbObj.speedMinNL_kts=7.700000
    dbObj.NL_min=52.200001
    dbObj.speedMaxNL_kts=16.000000
    dbObj.NL_max=100.199997
    dbObj.cavitationOffset_kts=11.000000
    dbObj.cavitationSlope_ktsperft=0.007000
    dbObj.cavitationSL_dB=148.000000
    dbObj.snorkelingSL_dB=142.000000
    dbObj.BuildSLTable()
    return dbObj