import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AN210'
    dbObj.xSpeed_kts=[0.000000,8.640000,30.240000,43.200001]
    dbObj.ySL_dB=[77.900002,82.283760,112.970078,121.737602]
    dbObj.speedMinNL_kts=11.340000
    dbObj.NL_min=44.400002
    dbObj.speedMaxNL_kts=43.200001
    dbObj.NL_max=83.599998
    dbObj.cavitationOffset_kts=16.200001
    dbObj.cavitationSlope_ktsperft=0.013150
    dbObj.cavitationSL_dB=139.737595
    dbObj.snorkelingSL_dB=133.737595
    dbObj.BuildSLTable()
    return dbObj