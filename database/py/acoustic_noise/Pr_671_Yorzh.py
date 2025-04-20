import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Pr 671 Yorzh'
    dbObj.xSpeed_kts=[0.000000,9.300000,24.799999,31.000000]
    dbObj.ySL_dB=[97.099998,113.269997,148.000000,165.500000]
    dbObj.speedMinNL_kts=4.000000
    dbObj.NL_min=54.000000
    dbObj.speedMaxNL_kts=32.000000
    dbObj.NL_max=104.000000
    dbObj.cavitationOffset_kts=10.540000
    dbObj.cavitationSlope_ktsperft=0.016000
    dbObj.cavitationSL_dB=175.399994
    dbObj.snorkelingSL_dB=177.500000
    dbObj.BuildSLTable()
    return dbObj