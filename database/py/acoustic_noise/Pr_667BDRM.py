import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='Pr 667BDRM'
    dbObj.xSpeed_kts=[0.000000,7.200000,19.200001,24.000000]
    dbObj.ySL_dB=[93.599998,104.519997,127.000000,144.000000]
    dbObj.speedMinNL_kts=7.000000
    dbObj.NL_min=50.750000
    dbObj.speedMaxNL_kts=24.000000
    dbObj.NL_max=100.750000
    dbObj.cavitationOffset_kts=11.810000
    dbObj.cavitationSlope_ktsperft=0.017000
    dbObj.cavitationSL_dB=167.600006
    dbObj.snorkelingSL_dB=156.000000
    dbObj.BuildSLTable()
    return dbObj