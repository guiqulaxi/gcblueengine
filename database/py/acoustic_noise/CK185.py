import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='CK185'
    dbObj.xSpeed_kts=[0.000000,4.490000,15.715000,22.450001]
    dbObj.ySL_dB=[91.139999,95.414589,125.336693,133.885864]
    dbObj.speedMinNL_kts=7.245000
    dbObj.NL_min=49.500000
    dbObj.speedMaxNL_kts=22.450001
    dbObj.NL_max=96.500000
    dbObj.cavitationOffset_kts=10.350000
    dbObj.cavitationSlope_ktsperft=0.005500
    dbObj.cavitationSL_dB=151.885864
    dbObj.snorkelingSL_dB=145.885864
    dbObj.BuildSLTable()
    return dbObj