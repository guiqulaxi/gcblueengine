import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='SwK205'
    dbObj.xSpeed_kts=[0.000000,5.344000,18.704000,26.719999]
    dbObj.ySL_dB=[78.800003,82.580681,109.045471,116.606834]
    dbObj.speedMinNL_kts=10.640000
    dbObj.NL_min=44.759998
    dbObj.speedMaxNL_kts=26.719999
    dbObj.NL_max=85.199997
    dbObj.cavitationOffset_kts=15.200000
    dbObj.cavitationSlope_ktsperft=0.015160
    dbObj.cavitationSL_dB=134.606842
    dbObj.snorkelingSL_dB=128.606842
    dbObj.BuildSLTable()
    return dbObj