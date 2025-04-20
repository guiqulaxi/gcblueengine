import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='SwK175'
    dbObj.xSpeed_kts=[0.000000,4.072000,14.252000,20.360001]
    dbObj.ySL_dB=[86.900002,91.129555,120.736435,129.195541]
    dbObj.speedMinNL_kts=9.170000
    dbObj.NL_min=48.480000
    dbObj.speedMaxNL_kts=20.360001
    dbObj.NL_max=92.699997
    dbObj.cavitationOffset_kts=13.100000
    dbObj.cavitationSlope_ktsperft=0.011080
    dbObj.cavitationSL_dB=147.195541
    dbObj.snorkelingSL_dB=141.195541
    dbObj.BuildSLTable()
    return dbObj