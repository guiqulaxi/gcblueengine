import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='S003.Merchant Large'
    dbObj.xSpeed_kts=[2.000000,7.500000,15.000000,30.000000]
    dbObj.ySL_dB=[110.500000,119.599998,138.899994,148.000000]
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