import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='RN180'
    dbObj.xSpeed_kts=[0.000000,7.200000,25.200001,36.000000]
    dbObj.ySL_dB=[91.400002,99.515633,156.325058,172.556320]
    dbObj.speedMinNL_kts=7.805000
    dbObj.NL_min=48.700001
    dbObj.speedMaxNL_kts=36.000000
    dbObj.NL_max=98.199997
    dbObj.cavitationOffset_kts=11.150000
    dbObj.cavitationSlope_ktsperft=0.005275
    dbObj.cavitationSL_dB=190.556320
    dbObj.snorkelingSL_dB=184.556320
    dbObj.BuildSLTable()
    return dbObj