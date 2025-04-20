import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='JK145'
    dbObj.xSpeed_kts=[0.000000,3.200000,11.200000,16.000000]
    dbObj.ySL_dB=[96.000000,100.000000,128.000000,136.000000]
    dbObj.speedMinNL_kts=7.700000
    dbObj.NL_min=52.200001
    dbObj.speedMaxNL_kts=16.000000
    dbObj.NL_max=100.199997
    dbObj.cavitationOffset_kts=11.000000
    dbObj.cavitationSlope_ktsperft=0.007000
    dbObj.cavitationSL_dB=154.000000
    dbObj.snorkelingSL_dB=148.000000
    dbObj.BuildSLTable()
    return dbObj