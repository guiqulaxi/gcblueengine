import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='FN175'
    dbObj.xSpeed_kts=[0.000000,6.960000,24.360001,34.799999]
    dbObj.ySL_dB=[91.699997,98.893555,149.248444,163.635559]
    dbObj.speedMinNL_kts=7.840000
    dbObj.NL_min=48.540001
    dbObj.speedMaxNL_kts=34.799999
    dbObj.NL_max=98.699997
    dbObj.cavitationOffset_kts=11.200000
    dbObj.cavitationSlope_ktsperft=0.007940
    dbObj.cavitationSL_dB=181.635559
    dbObj.snorkelingSL_dB=175.635559
    dbObj.BuildSLTable()
    return dbObj