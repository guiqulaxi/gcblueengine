import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Hai lung'
    dbObj.xSpeed_kts=[0.000000,6.000000,16.000000,20.000000]
    dbObj.ySL_dB=[91.099998,99.620003,116.500000,125.699997]
    dbObj.speedMinNL_kts=4.000000
    dbObj.NL_min=51.000000
    dbObj.speedMaxNL_kts=20.000000
    dbObj.NL_max=101.000000
    dbObj.cavitationOffset_kts=10.740000
    dbObj.cavitationSlope_ktsperft=0.016000
    dbObj.cavitationSL_dB=162.800003
    dbObj.snorkelingSL_dB=137.699997
    dbObj.BuildSLTable()
    return dbObj