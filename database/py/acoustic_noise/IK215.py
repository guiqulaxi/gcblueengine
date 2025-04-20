import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='IK215'
    dbObj.xSpeed_kts=[0.000000,5.668000,19.837999,28.340000]
    dbObj.ySL_dB=[77.239998,80.994049,107.272423,114.780525]
    dbObj.speedMinNL_kts=10.052000
    dbObj.NL_min=43.660000
    dbObj.speedMaxNL_kts=28.340000
    dbObj.NL_max=83.260002
    dbObj.cavitationOffset_kts=14.360000
    dbObj.cavitationSlope_ktsperft=0.012980
    dbObj.cavitationSL_dB=132.780533
    dbObj.snorkelingSL_dB=126.780525
    dbObj.BuildSLTable()
    return dbObj