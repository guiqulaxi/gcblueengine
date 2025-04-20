import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='S002.Merchant Medium'
    dbObj.xSpeed_kts=[2.000000,8.250000,16.500000,33.000000]
    dbObj.ySL_dB=[110.000000,118.800003,137.199997,146.000000]
    dbObj.speedMinNL_kts=0.000000
    dbObj.NL_min=60.000000
    dbObj.speedMaxNL_kts=36.000000
    dbObj.NL_max=100.000000
    dbObj.cavitationOffset_kts=100.000000
    dbObj.cavitationSlope_ktsperft=0.000000
    dbObj.cavitationSL_dB=0.000000
    dbObj.snorkelingSL_dB=0.000000
    dbObj.BuildSLTable()
    return dbObj