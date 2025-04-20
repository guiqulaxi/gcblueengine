import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Pr 705 Lira'
    dbObj.xSpeed_kts=[0.000000,13.200000,35.200001,44.000000]
    dbObj.ySL_dB=[96.699997,112.089996,145.000000,163.000000]
    dbObj.speedMinNL_kts=5.000000
    dbObj.NL_min=52.000000
    dbObj.speedMaxNL_kts=44.000000
    dbObj.NL_max=102.000000
    dbObj.cavitationOffset_kts=11.460000
    dbObj.cavitationSlope_ktsperft=0.018000
    dbObj.cavitationSL_dB=174.399994
    dbObj.snorkelingSL_dB=175.000000
    dbObj.BuildSLTable()
    return dbObj