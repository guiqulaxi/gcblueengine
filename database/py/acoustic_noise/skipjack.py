import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='skipjack'
    dbObj.xSpeed_kts=[0.000000,10.000000,24.799999,31.000000]
    dbObj.ySL_dB=[97.099998,127.860001,148.000000,171.000000]
    dbObj.speedMinNL_kts=5.000000
    dbObj.NL_min=51.599998
    dbObj.speedMaxNL_kts=31.000000
    dbObj.NL_max=101.400002
    dbObj.cavitationOffset_kts=10.300000
    dbObj.cavitationSlope_ktsperft=0.019000
    dbObj.cavitationSL_dB=177.500000
    dbObj.snorkelingSL_dB=183.000000
    dbObj.BuildSLTable()
    return dbObj