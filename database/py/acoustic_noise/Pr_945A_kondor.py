import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Pr 945A kondor'
    dbObj.xSpeed_kts=[0.000000,10.500000,28.000000,35.000000]
    dbObj.ySL_dB=[89.400002,96.629997,110.500000,131.000000]
    dbObj.speedMinNL_kts=7.000000
    dbObj.NL_min=50.750000
    dbObj.speedMaxNL_kts=36.000000
    dbObj.NL_max=100.750000
    dbObj.cavitationOffset_kts=11.720000
    dbObj.cavitationSlope_ktsperft=0.023000
    dbObj.cavitationSL_dB=163.899994
    dbObj.snorkelingSL_dB=143.000000
    dbObj.BuildSLTable()
    return dbObj