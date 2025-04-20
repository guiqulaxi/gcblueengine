import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AK160'
    dbObj.xSpeed_kts=[0.000000,3.442000,12.047000,17.209999]
    dbObj.ySL_dB=[90.129997,94.418304,124.436440,133.013046]
    dbObj.speedMinNL_kts=8.540000
    dbObj.NL_min=50.400002
    dbObj.speedMaxNL_kts=17.209999
    dbObj.NL_max=96.599998
    dbObj.cavitationOffset_kts=12.200000
    dbObj.cavitationSlope_ktsperft=0.007650
    dbObj.cavitationSL_dB=151.013046
    dbObj.snorkelingSL_dB=145.013046
    dbObj.BuildSLTable()
    return dbObj