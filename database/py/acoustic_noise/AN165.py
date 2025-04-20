import pygcb
def CreateDBObject():
    dbObj=pygcb.tcAcousticModel()
    dbObj.databaseClass='AN165'
    dbObj.xSpeed_kts=[0.000000,6.480000,22.680000,32.400002]
    dbObj.ySL_dB=[93.199997,100.163338,148.906723,162.833389]
    dbObj.speedMinNL_kts=8.820000
    dbObj.NL_min=49.799999
    dbObj.speedMaxNL_kts=32.400002
    dbObj.NL_max=103.400002
    dbObj.cavitationOffset_kts=12.600000
    dbObj.cavitationSlope_ktsperft=0.008200
    dbObj.cavitationSL_dB=180.833389
    dbObj.snorkelingSL_dB=174.833389
    dbObj.BuildSLTable()
    return dbObj