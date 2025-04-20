import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FK200'
    dbObj.xSpeed_kts=[0.000000,5.032000,17.612000,25.160000]
    dbObj.ySL_dB=[81.040001,85.343132,115.465042,124.071304]
    dbObj.speedMinNL_kts=8.540000
    dbObj.NL_min=45.490002
    dbObj.speedMaxNL_kts=25.160000
    dbObj.NL_max=87.220001
    dbObj.cavitationOffset_kts=12.200000
    dbObj.cavitationSlope_ktsperft=0.010390
    dbObj.cavitationSL_dB=142.071304
    dbObj.snorkelingSL_dB=136.071304
    dbObj.BuildSLTable()
    return dbObj