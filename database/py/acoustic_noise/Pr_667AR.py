import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Pr 667AR'
    dbObj.xSpeed_kts=[0.000000,8.400000,22.400000,28.000000]
    dbObj.ySL_dB=[97.099998,113.269997,148.000000,165.500000]
    dbObj.speedMinNL_kts=7.000000
    dbObj.NL_min=51.000000
    dbObj.speedMaxNL_kts=28.000000
    dbObj.NL_max=101.000000
    dbObj.cavitationOffset_kts=11.510000
    dbObj.cavitationSlope_ktsperft=0.017000
    dbObj.cavitationSL_dB=175.399994
    dbObj.snorkelingSL_dB=177.500000
    dbObj.BuildSLTable()
    return dbObj