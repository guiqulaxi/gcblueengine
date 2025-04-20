import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='LA'
    dbObj.xSpeed_kts=[0.000000,9.600000,25.600000,32.000000]
    dbObj.ySL_dB=[89.599998,96.919998,111.000000,131.000000]
    dbObj.speedMinNL_kts=8.000000
    dbObj.NL_min=49.500000
    dbObj.speedMaxNL_kts=32.000000
    dbObj.NL_max=99.500000
    dbObj.cavitationOffset_kts=12.700000
    dbObj.cavitationSlope_ktsperft=0.028000
    dbObj.cavitationSL_dB=163.899994
    dbObj.snorkelingSL_dB=143.000000
    dbObj.BuildSLTable()
    return dbObj