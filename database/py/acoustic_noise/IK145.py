import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='IK145'
    dbObj.xSpeed_kts=[0.000000,2.700000,9.450000,13.500000]
    dbObj.ySL_dB=[96.000000,100.252502,130.020004,138.524994]
    dbObj.speedMinNL_kts=7.700000
    dbObj.NL_min=52.200001
    dbObj.speedMaxNL_kts=13.500000
    dbObj.NL_max=100.199997
    dbObj.cavitationOffset_kts=11.000000
    dbObj.cavitationSlope_ktsperft=0.005000
    dbObj.cavitationSL_dB=156.524994
    dbObj.snorkelingSL_dB=150.524994
    dbObj.BuildSLTable()
    return dbObj