import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='SwK210'
    dbObj.xSpeed_kts=[0.000000,5.556000,19.445999,27.780001]
    dbObj.ySL_dB=[77.449997,81.136963,106.945717,114.319649]
    dbObj.speedMinNL_kts=10.885000
    dbObj.NL_min=44.139999
    dbObj.speedMaxNL_kts=27.780001
    dbObj.NL_max=83.949997
    dbObj.cavitationOffset_kts=15.550000
    dbObj.cavitationSlope_ktsperft=0.015840
    dbObj.cavitationSL_dB=132.319641
    dbObj.snorkelingSL_dB=126.319649
    dbObj.BuildSLTable()
    return dbObj