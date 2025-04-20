import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='BK210'
    dbObj.xSpeed_kts=[0.000000,5.582000,19.537001,27.910000]
    dbObj.ySL_dB=[77.839996,81.710648,108.805183,116.546478]
    dbObj.speedMinNL_kts=10.430000
    dbObj.NL_min=44.139999
    dbObj.speedMaxNL_kts=27.910000
    dbObj.NL_max=84.599998
    dbObj.cavitationOffset_kts=14.900000
    dbObj.cavitationSlope_ktsperft=0.015060
    dbObj.cavitationSL_dB=134.546478
    dbObj.snorkelingSL_dB=128.546478
    dbObj.BuildSLTable()
    return dbObj