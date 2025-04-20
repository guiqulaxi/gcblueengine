import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Pr 971 Shchuka-B(92)'
    dbObj.xSpeed_kts=[0.000000,10.500000,28.000000,35.000000]
    dbObj.ySL_dB=[89.400002,96.629997,110.500000,130.000000]
    dbObj.speedMinNL_kts=8.000000
    dbObj.NL_min=50.500000
    dbObj.speedMaxNL_kts=36.000000
    dbObj.NL_max=100.500000
    dbObj.cavitationOffset_kts=12.350000
    dbObj.cavitationSlope_ktsperft=0.025000
    dbObj.cavitationSL_dB=163.699997
    dbObj.snorkelingSL_dB=142.000000
    dbObj.BuildSLTable()
    return dbObj