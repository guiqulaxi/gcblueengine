import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Type 206'
    dbObj.xSpeed_kts=[0.000000,5.100000,13.600000,17.000000]
    dbObj.ySL_dB=[91.900002,101.019997,119.300003,128.600006]
    dbObj.speedMinNL_kts=7.000000
    dbObj.NL_min=47.000000
    dbObj.speedMaxNL_kts=17.000000
    dbObj.NL_max=97.500000
    dbObj.cavitationOffset_kts=12.220000
    dbObj.cavitationSlope_ktsperft=0.026000
    dbObj.cavitationSL_dB=163.399994
    dbObj.snorkelingSL_dB=140.600006
    dbObj.BuildSLTable()
    return dbObj