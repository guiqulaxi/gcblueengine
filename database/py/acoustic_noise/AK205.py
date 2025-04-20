import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AK205'
    dbObj.xSpeed_kts=[0.000000,5.368000,18.788000,26.840000]
    dbObj.ySL_dB=[78.519997,82.352112,109.176880,116.841103]
    dbObj.speedMinNL_kts=11.060000
    dbObj.NL_min=45.000000
    dbObj.speedMaxNL_kts=26.840000
    dbObj.NL_max=85.800003
    dbObj.cavitationOffset_kts=15.800000
    dbObj.cavitationSlope_ktsperft=0.012600
    dbObj.cavitationSL_dB=134.841110
    dbObj.snorkelingSL_dB=128.841110
    dbObj.BuildSLTable()
    return dbObj