import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='GK195'
    dbObj.xSpeed_kts=[0.000000,5.360000,18.760000,26.799999]
    dbObj.ySL_dB=[79.599998,83.286240,109.089935,116.462418]
    dbObj.speedMinNL_kts=10.850000
    dbObj.NL_min=45.700001
    dbObj.speedMaxNL_kts=26.799999
    dbObj.NL_max=87.199997
    dbObj.cavitationOffset_kts=15.500000
    dbObj.cavitationSlope_ktsperft=0.013400
    dbObj.cavitationSL_dB=134.462418
    dbObj.snorkelingSL_dB=128.462418
    dbObj.BuildSLTable()
    return dbObj