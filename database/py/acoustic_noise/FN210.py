import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FN210'
    dbObj.xSpeed_kts=[0.000000,8.640000,30.240000,43.200001]
    dbObj.ySL_dB=[79.099998,84.274162,120.493317,130.841644]
    dbObj.speedMinNL_kts=8.820000
    dbObj.NL_min=44.270000
    dbObj.speedMaxNL_kts=43.200001
    dbObj.NL_max=82.949997
    dbObj.cavitationOffset_kts=12.600000
    dbObj.cavitationSlope_ktsperft=0.011370
    dbObj.cavitationSL_dB=148.841644
    dbObj.snorkelingSL_dB=142.841644
    dbObj.BuildSLTable()
    return dbObj