import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='CN190'
    dbObj.xSpeed_kts=[0.000000,6.440000,22.540001,32.200001]
    dbObj.ySL_dB=[89.599998,95.670166,138.161301,150.301620]
    dbObj.speedMinNL_kts=7.560000
    dbObj.NL_min=49.000000
    dbObj.speedMaxNL_kts=32.200001
    dbObj.NL_max=94.500000
    dbObj.cavitationOffset_kts=10.800000
    dbObj.cavitationSlope_ktsperft=0.006000
    dbObj.cavitationSL_dB=168.301620
    dbObj.snorkelingSL_dB=162.301620
    dbObj.BuildSLTable()
    return dbObj