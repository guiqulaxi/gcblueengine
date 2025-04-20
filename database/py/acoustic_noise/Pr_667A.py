import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Pr 667A'
    dbObj.xSpeed_kts=[0.000000,9.000000,21.600000,27.000000]
    dbObj.ySL_dB=[97.099998,125.459999,148.000000,165.000000]
    dbObj.speedMinNL_kts=5.000000
    dbObj.NL_min=51.000000
    dbObj.speedMaxNL_kts=27.000000
    dbObj.NL_max=101.000000
    dbObj.cavitationOffset_kts=10.300000
    dbObj.cavitationSlope_ktsperft=0.017000
    dbObj.cavitationSL_dB=175.199997
    dbObj.snorkelingSL_dB=177.000000
    dbObj.BuildSLTable()
    return dbObj